from django.urls import include, path

from apps.users.api import views

urlpatterns = [
    path("me/", views.UserProfileView.as_view(), name="me"),
]
