from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from review.models import Ticket, Review, UserFollows
from review.forms import TicketForm
from review.forms import ReviewForm

@login_required
def home(request):
    return render(request, 'review/home.html')


def ticket_list(request):
    tickets = Ticket.objects.all()
    return render(request, 'review/ticket_list.html',
                  {'tickets':tickets})


def ticket_create(request):
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


def review_list(request):
    review = Review.objects.all()
    return render(request, 'review/review_list.html',
                  {'review':review})

def review_create(request):
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


def user_follow(request):
    user_follow = UserFollows.objects.all()
    return render(request, 'review/user_follow.html')