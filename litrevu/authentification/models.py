from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    # ajouter un field many-to-many ici pour qu'il creer une ligne dans la table user follow automatiquement
    pass