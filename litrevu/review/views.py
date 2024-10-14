from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from review.models import Ticket, Review, UserFollows
from review.forms import TicketForm, ReviewForm, UserFollowsForm


@login_required
def home(request):
    tickets= Ticket.objects.all()
    return render(request, 'review/home.html', context={'tickets': tickets})


def ticket_list(request):
    tickets = Ticket.objects.all()
    return render(request, 'review/ticket_list.html',
                  {'tickets':tickets})


def ticket_create(request):
    form = TicketForm()
    if request.method == "POST":
        form = TicketForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("ticket_list")
        else:
            form = TicketForm()
    return render(request, "review/ticket_create.html", {"form": form})


def ticket_update(request, id):
    ticket = Ticket.objects.get(id=id)
    if request.method == "POST":
        form = TicketForm(request.POST, instance=ticket)
        if form.is_valid():
            form.save()
            return redirect("ticket_list")
        else:
            form = TicketForm(instance=ticket)
    return render(request, "review/ticket_update.html", {"form": form})


def ticket_delete(request, id):
    ticket = Ticket.objects.get(id=id)
    
    if request.method == "POST":
        ticket.delete()
        return redirect("ticket_list")
    
    return render(request, "review/ticket_delete.html", {"ticket": ticket})

def photo_upload(request):
    form = TicketForm()
    if request.method == "POST":
        form = TicketForm(request.POST, request.FILES)
        if form.is_valid():
            ticket = form.save(commit=False)
            ticket.uploader = request.user
            ticket.save()
            return redirect('home')
    return render(request, 'review/photo_upload.html', context={'form': form})


def review_list(request):
    review = Review.objects.all()
    return render(request, 'review/review_list.html',
                  {'reviews':review})

def review_create(request):
    form = ReviewForm()
    if request.method == "POST":
        form = ReviewForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("review_list")
        else:
            form = ReviewForm()
    return render(request, "review/review_create.html", {"form": form})


def review_update(request, id):
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
    review = Review.objects.get(id=id)
    
    if request.method == "POST":
        review.delete()
        return redirect("review_list")
    
    return render(request, "review/review_delete.html", {"review": review})


def user_followed_list(request):
    user_followed = UserFollows.objects.all()
    return render(request, 'review/user_followed_list.html', {'users_followed':user_followed})

def user_followed_create(request):
    form = UserFollowsForm(instance=request.user)
    if request.method == "POST":
        form = UserFollowsForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect("home")
    else:
        form = UserFollowsForm()
    return render(request, "review/user_followed_create.html", context={"form": form})

def user_followed_delete(request, id):
    user_followed = UserFollows.objects.get(id=id)
    
    if request.method == "POST":
        user_followed.delete()
        return redirect("user_followed_list")
    
    return render(request, "review/user_followed_delete.html", {"user_followed": user_followed})
