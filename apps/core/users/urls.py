from django.urls import include, path

from . import views

urlpatterns = [
    path("register", views.CreateUserAPI.as_view()),
    path("me", views.MyProfileAPI.as_view()),
]
