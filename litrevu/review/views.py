from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from review.models import Ticket, Review, UserFollows

@login_required
def home(request):
    return render(request, 'review/home.html')


def ticket(request):
    ticket = Ticket.objects.all()
    return render(request, 'review/ticket.html',
                  {'ticket':ticket})
    

def review(request):
    review = Review.objects.all()
    return render(request, 'review/review.html',
                  {'review':review})

def user_follow(request):
    user_follow = UserFollows.objects.all()
    return render(request, 'review/user_follow.html')