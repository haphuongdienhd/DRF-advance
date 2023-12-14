from django.urls import include, path

from apps.friendships.api import views

urlpatterns = [
    path("", views.FriendListAPIView.as_view(), name="list-my-friends"),
    path("<uuid:friendship_id>/", views.FriendShipRetrieveDestroyAPIView.as_view(), name="retrive-delete-friendships"),
    path("requests/", views.MyRequestListCreateAPIView.as_view(), name="list-my-requests"),
    path("requests/new/", views.NewRequestToMeListAPIView.as_view(), name="list-new-requests-to-me"),
    path("requests/me/", views.RequestToMeListAPIView.as_view(), name="list-requests-to-me"),
    path("requests/<str:action>/", views.RequestActionAPIView.as_view(), name="retrive-delete-requests"),
]
