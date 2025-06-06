from django.urls import path
from django.contrib.auth.views import LogoutView 
from . import views

urlpatterns = [
    path("login/", views.login, name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("profile/", views.profile, name="profile"),
]