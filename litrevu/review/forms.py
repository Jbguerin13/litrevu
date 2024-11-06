from django import forms
from django.contrib.auth import get_user_model

from review.models import Ticket
from review.models import Review
from review.models import UserFollows

User = get_user_model()

class TicketForm(forms.ModelForm):
    """
    A form for creating and updating a Ticket instance.

    Attributes:
        model (Ticket): The model associated with this form.
        exclude (tuple): Fields to exclude from the form, specifically 'user' 
                         and 'time_created'.
    """
    class Meta:
        model = Ticket
        #fields = '__all__'
        exclude = ('user', 'time_created')


class ReviewForm(forms.ModelForm):
    """
    A form for creating and updating a Review instance.
    
    Attributes:
        model (Review): The model associated with this form.
        exclude (tuple): Fields to exclude from the form, specifically 'user', 
                         'time_created', and 'ticket'.
    """
    class Meta:
        model = Review
        #fields = '__all__'
        exclude = ('user', 'time_created', 'ticket')
        

class UserFollowsForm(forms.ModelForm):
    """
    A form for managing user follow relationships.
    
    Attributes:
        model (User): The model associated with this form.
        exclude (tuple): Fields to exclude from the form, specifically 'user'.
    """
    class Meta:
        model = User
        #fields = '__all__'
        exclude = ('user',)
