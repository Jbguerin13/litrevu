from django import forms
from django.contrib.auth import get_user_model

from review.models import Ticket
from review.models import Review
from review.models import UserFollows

User = get_user_model()

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
        model = User
        #fields = '__all__'
        exclude = ('user',)
