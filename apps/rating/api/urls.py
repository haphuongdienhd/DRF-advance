from django.urls import include, path

from apps.rating.api import views

urlpatterns = [
    path("", views.RatingListCreateAPIView.as_view(), name="list-or-create-rating"),
    path("<uuid:rating_id>", views.RatingRetrieveUpdateDestroyAPIView.as_view(), name="retrive-update-delete-rating"),
]