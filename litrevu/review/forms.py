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
        # fields = '__all__'
        exclude = ("user", "time_created")


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
        exclude = (
            "user",
            "time_created",
            "ticket",
            "contributors",
        )  # Exclure les champs gérés automatiquement


class UserFollowsForm(forms.ModelForm):
    """
    A form for selecting a user to follow.
    """

    followed_user = forms.ModelChoiceField(
        queryset=User.objects.all(), label="Nom de l'utilisateur à suivre"
    )

    class Meta:
        model = UserFollows
        fields = ["followed_user"]

    def __init__(self, *args, **kwargs):
        user = kwargs.pop("user", None)  # Récupérer l'utilisateur actuel
        super().__init__(*args, **kwargs)
        if user:
            # Exclure l'utilisateur actuel de la liste des choix
            self.fields["followed_user"].queryset = User.objects.exclude(id=user.id)
