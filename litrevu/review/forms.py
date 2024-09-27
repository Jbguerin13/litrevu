from django import forms

from review.models import Ticket
from review.models import Review

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