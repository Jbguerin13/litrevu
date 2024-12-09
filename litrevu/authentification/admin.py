from django.contrib import admin
from authentification.models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ("role",)


# Register your models here.
