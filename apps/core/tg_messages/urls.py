from django.urls import include, path

from . import views

urlpatterns = [
    path("", views.ListCreateMessageAPI.as_view()),
]
