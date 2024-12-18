"""
URL configuration for litrevu project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from django.contrib.auth.views import LoginView

from authentification import views
import review.views

urlpatterns = [
    path("admin/", admin.site.urls),
    path(
        "",
        LoginView.as_view(
            template_name="authentification/login.html",
            redirect_authenticated_user=True,
        ),
        name="login",
    ),
    path("logout", views.logout_user, name="logout"),
    path("home/", review.views.home, name="home"),
    path("signup", views.signup_page, name="signup"),
    path("ticket/", review.views.ticket_list, name="ticket_list"),
    path("ticket/add/", review.views.ticket_create, name="ticket_create"),
    path("ticket/<int:id>/update/", review.views.ticket_update, name="ticket_update"),
    path("ticket/<int:id>/delete/", review.views.ticket_delete, name="ticket_delete"),
    path("review/", review.views.review_list, name="review_list"),
    path("review/add/", review.views.review_create, name="review_create"),
    path("review/<int:id>/update/", review.views.review_update, name="review_update"),
    path("review/<int:id>/delete/", review.views.review_delete, name="review_delete"),
    path("user-followed/", review.views.user_followed_list, name="user_followed_list"),
    path(
        "user-followed/add/",
        review.views.user_followed_create,
        name="user_followed_create",
    ),
    path(
        "user-followed/<int:id>/delete/",
        review.views.user_followed_delete,
        name="user_followed_delete",
    ),
    path("photo/upload/", review.views.photo_upload, name="photo_upload"),
    path("posts/", review.views.post_ticket_review, name="posts"),
    path("flux/", review.views.flux, name="flux"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
