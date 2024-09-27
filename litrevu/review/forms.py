from django import forms

from review.models import Ticket
from review.models import Review
from review.models import UserFollows


class TicketForm(forms.ModelForm):
    class Meta:
        model = Ticket
        #fields = '__all__'
        exclude = ('user', 'time_created')


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        #fields = '__all__'
        exclude = ('user', 'time_created', 'ticket')
        

class UserFollowsForm(forms.ModelForm):
    class Meta:
        model = UserFollows
        #fields = '__all__'
        exclude = ('user')