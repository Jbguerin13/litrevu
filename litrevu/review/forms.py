from django import forms

from review.models import Ticket

class TicketForm(forms.ModelForm):
    class Meta:
        model = Ticket
        #fields = '__all__'
        exclude = ('user', 'time_created')