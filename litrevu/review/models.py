from django.core.validators import MinValueValidator, MaxValueValidator
from django.conf import settings
from django.db import models
from authentification.models import User


class Ticket(models.Model):
    """
    Model Ticket can be created by a User.
    
    Attributes:
        title (char)): The title of the ticket.
        description (text): An optional description of the ticket.
        user (ForeignKey): The user who created the ticket, linked to the AUTH_USER_MODEL.
        image (ImageField): An optional image related to the movie talked about.
        time_created (DateTimeField): The timestamp of when the ticket was created.
    """
    title = models.CharField(max_length=128)
    description = models.TextField(max_length=2048, blank=True)
    user = models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    image = models.ImageField(null=True, blank=True)
    time_created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        """
        Returns:
            str: The title of the ticket.
        """
        return self.title

    def has_review(self):
        """        
        Returns:
            bool: True if there is at least one review, False otherwise.
        """

        return self.review_set.exists()


class Review(models.Model):
    """
    Model Review related to a ticket.
    
    Attributes:
        ticket (ForeignKey): The ticket being reviewed.
        rating (PositiveSmallIntegerField): The rating for the review, between 0 and 5.
        headline (char): The headline of the review, limited to 128 characters.
        body (text): The body content of the review, optional and limited to 8192 characters.
        user (ForeignKey): The user who created the review.
        time_created (datetime): The timestamp of when the review was created.
        contributors (ManyToManyField): A list of users who contributed to the review.
    """
    ticket = models.ForeignKey(to=Ticket, on_delete=models.CASCADE)
    rating = models.PositiveSmallIntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(5)])
    headline = models.CharField(max_length=128)
    body = models.TextField(max_length=8192, blank=True)
    user = models.ForeignKey(
        to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)
    time_created = models.DateTimeField(auto_now_add=True)
    contributors = models.ManyToManyField(
        settings.AUTH_USER_MODEL, 
        through='ReviewContributor', 
        related_name='contributions')
    
    def __str__(self):
        """
        Returns:
            str: The headline of the review.
        """
        return self.headline

class UserFollows(models.Model):
    """
    Model representing the relationship of one user following another.
    
    Attributes:
        user (ForeignKey): The user who is following someone.
        followed_user (ForeignKey): The user being followed.
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='following')
    followed_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='followers')

    class Meta:
        unique_together = ('user', 'followed_user')

    def __str__(self):
        """
        Returns:
            str: A string in the format "{user} is following {followed_user}".
        """
        return f"{self.user.username} is following {self.followed_user.username}"


class ReviewContributor(models.Model):
    review =  models.ForeignKey(Review, on_delete=models.CASCADE)
    contributor = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    contributions = models.CharField(max_length=255, blank=True)
    
    class Meta:
        unique_together = ('review', 'contributor')
