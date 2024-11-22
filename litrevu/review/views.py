from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from review.models import Ticket, Review, UserFollows
from review.forms import TicketForm, ReviewForm, UserFollowsForm

# =========== Home and User Flux ===========

@login_required
def home(request):
    """
    View function for the home page, displaying all tickets.

    Args:
        request: The HTTP request object.

    Returns:
        HttpResponse: Renders the 'review/home.html' template with all tickets.
    """
    tickets= Ticket.objects.all()
    return render(request, 'review/home.html', context={'tickets': tickets})

@login_required
def post_ticket_review(request):
    """
    View function to display tickets and reviews created by the current user.

    Args:
        request: The HTTP request object.

    Returns:
        HttpResponse: Renders the 'bookreview/posts.html' template with the user's posts.
    """
    tickets = Ticket.objects.filter(user=request.user)
    reviews = Review.objects.filter(user=request.user)
    posts = list(tickets) + list(reviews)

    # Tri des posts par date de création
    posts.sort(key=lambda x: x.time_created, reverse=True)

    context = {
        "posts": posts,
    }

    return render(request, "review/posts.html", context)

@login_required
def flux(request):
    """
    View function to display the feed of tickets and reviews for the user, including 
    those from followed users.

    Args:
        request: The HTTP request object.

    Returns:
        HttpResponse: Renders the 'bookreview/flux.html' template with the user's feed.
    """
    tickets = Ticket.objects.filter(user=request.user)
    reviews = Review.objects.filter(user=request.user)

    posts_set = set(tickets) | set(reviews)

    follows = UserFollows.objects.filter(user=request.user)

    for follow in follows:
        tickets_followed = Ticket.objects.filter(user=follow.followed_user)
        reviews_followed = Review.objects.filter(user=follow.followed_user)
        posts_set |= set(tickets_followed) | set(reviews_followed)

    user_reviews = Review.objects.filter(ticket__user=request.user)
    posts_set |= set(user_reviews)

    posts = sorted(posts_set, key=lambda x: x.time_created, reverse=True)

    context = {
        "posts": posts,
    }

    return render(request, "review/flux.html", context)

# =========== Ticket ===========

def ticket_list(request):
    """
    View function to list all tickets.

    Args:
        request: The HTTP request object.

    Returns:
        HttpResponse: Renders the 'review/ticket_list.html' template with all tickets.
    """
    tickets = Ticket.objects.all()
    return render(request, 'review/ticket_list.html',
                  {'tickets':tickets})


def ticket_create(request): 
    """
    View function to create a new ticket.

    Args:
        request: The HTTP request object.

    Returns:
        HttpResponse: Renders the 'review/ticket_create.html' template with the ticket creation form.
    """
    form = TicketForm()
    if request.method == "POST":
        form = TicketForm(request.POST, request.FILES)
        if form.is_valid():
            ticket = form.save(commit=False)
            ticket.user = request.user
            ticket.save()
            return redirect("ticket_list")
        else:
            form = TicketForm()
    return render(request, "review/ticket_create.html", {"form": form})


def ticket_update(request, id):
    """
    View function to update an existing ticket.

    Args:
        request: The HTTP request object.
        id (int): The ID of the ticket to be updated.

    Returns:
        HttpResponse: Renders the 'review/ticket_update.html' template with the update form.
    """
    ticket = Ticket.objects.get(id=id)
    form = TicketForm(instance=ticket)
    
    if request.method == "POST":
        form = TicketForm(request.POST, request.FILES, instance=ticket)
        if form.is_valid():
            form.save()
            return redirect("flux")
    return render(request, "review/ticket_update.html", {"form": form, "ticket": ticket})


def ticket_delete(request, id):
    """
    View function to delete an existing ticket.

    Args:
        request: The HTTP request object.
        id (int): The ID of the ticket to be deleted.

    Returns:
        HttpResponse: Renders the 'review/ticket_delete.html' template or redirects to ticket list.
    """
    ticket = Ticket.objects.get(id=id)
    
    if request.method == "POST":
        ticket.delete()
        return redirect("ticket_list")
    
    return render(request, "review/ticket_delete.html", {"ticket": ticket})

def photo_upload(request):
    """
    View function to upload a photo when creating a ticket.

    Args:
        request: The HTTP request object.

    Returns:
        HttpResponse: Renders the 'review/photo_upload.html' template with the photo upload form.
    """
    form = TicketForm()
    if request.method == "POST":
        form = TicketForm(request.POST, request.FILES)
        if form.is_valid():
            ticket = form.save(commit=False)
            ticket.uploader = request.user
            ticket.save()
            return redirect('home')
    return render(request, 'review/photo_upload.html', context={'form': form})


# =========== Review ===========


def review_list(request):
    """
    View function to list all reviews.

    Args:
        request: The HTTP request object.

    Returns:
        HttpResponse: Renders the 'review/review_list.html' template with all reviews.
    """
    review = Review.objects.all()
    return render(request, 'review/review_list.html',
                  {'reviews':review})

def review_create(request):
    """
    View function to create a new review.
    """
    if request.method == "POST":
        # Récupération des données POST pour la critique
        ticket_title = request.POST.get("ticket_title")
        ticket_description = request.POST.get("ticket_description")
        ticket_image = request.FILES.get("ticket_image")

        headline = request.POST.get("headline")
        body = request.POST.get("body")
        rating = request.POST.get("rating")

        if ticket_title and headline and rating is not None:
            # Créer un ticket associé si nécessaire
            ticket = Ticket.objects.create(
                title=ticket_title,
                description=ticket_description,
                image=ticket_image,
                user=request.user
            )

            # Créer la critique associée au ticket
            review = Review.objects.create(
                ticket=ticket,
                headline=headline,
                body=body,
                rating=rating,
                user=request.user
            )

            # Ajouter un message de confirmation
            messages.success(request, "Votre critique a été créée avec succès !")
            return redirect("review_list")
        else:
            messages.error(request, "Tous les champs obligatoires doivent être remplis.")

    return render(request, "review/review_create.html")


def review_update(request, id):
    """
    View function to update an existing review.

    Args:
        request: The HTTP request object.
        id (int): The ID of the review to be updated.

    Returns:
        HttpResponse: Renders the 'review/review_update.html' template with the update form.
    """
    review = Review.objects.get(id=id)
    if request.method == "POST":
        form = ReviewForm(request.POST, instance=review)
        if form.is_valid():
            form.save()
            return redirect("review_list")
        else:
            form = ReviewForm(instance=review)
    return render(request, "review/review_update.html", {"form": form})


def review_delete(request, id):
    """
    View function to delete an existing review.

    Args:
        request: The HTTP request object.
        id (int): The ID of the review to be deleted.

    Returns:
        HttpResponse: Renders the 'review/review_delete.html' template or redirects to review list.
    """
    review = Review.objects.get(id=id)
    
    if request.method == "POST":
        review.delete()
        return redirect("review_list")
    
    return render(request, "review/review_delete.html", {"review": review})


# =========== UserFollow ===========

def user_followed_list(request):
    """
    View function to list all user follow relationships.

    Args:
        request: The HTTP request object.

    Returns:
        HttpResponse: Renders the 'review/user_followed_list.html' template with all followed users.
    """
    user = request.user
    users_followed = UserFollows.objects.filter(user=user)
    followers = UserFollows.objects.filter(followed_user=user)

    return render(request, 'review/user_followed_list.html', {
        'users_followed': users_followed,
        'followers': followers,
    })

def user_followed_create(request):
    """
    View function to create a new user follow relationship.
    """
    if request.method == "POST":
        form = UserFollowsForm(request.POST, user=request.user)
        if form.is_valid():
            user_follow = form.save(commit=False)  # Ne pas enregistrer immédiatement
            user_follow.user = request.user  # Assigner l'utilisateur connecté
            user_follow.save()
            return redirect("home")
    else:
        form = UserFollowsForm(user=request.user)
    return render(request, "review/user_followed_create.html", context={"form": form})

def user_followed_delete(request, id):
    """
    View function to delete an existing user follow relationship.

    Args:
        request: The HTTP request object.
        id (int): The ID of the user follow relationship to be deleted.

    Returns:
        HttpResponse: Renders the 'review/user_followed_delete.html' template or redirects to followed list.
    """
    user_followed = UserFollows.objects.get(id=id)
    
    if request.method == "POST":
        user_followed.delete()
        return redirect("user_followed_list")
    
    return render(request, "review/user_followed_delete.html", {"user_followed": user_followed})
