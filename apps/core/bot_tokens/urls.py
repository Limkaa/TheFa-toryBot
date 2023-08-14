from django.urls import include, path

from . import views

urlpatterns = [
    path("", views.UserTokenAPI.as_view()),
]
