from django.urls import include, path

from apps.friendships.api import views

urlpatterns = [
    path("", views.FriendShipListAPIView.as_view(), name="list-friendships"),
    path("me", views.MyFriendShipListAPIView.as_view(), name="list-my-friendships"),
    path("<uuid:friendship_id>", views.FriendShipRetrieveDestroyAPIView.as_view(), name="retrive-delete-friendships"),
    path("requests", views.RequestToMeListAPIView.as_view(), name="list-requests-to-me"),
    path("requests/new", views.NewRequestToMeListAPIView.as_view(), name="list-new-requests-to-me"),
    path("requests/me", views.MyRequestListAPIView.as_view(), name="list-my-requests"),    
    path("requests/<uuid:request_id>", views.RequestRetrieveDestroyAPIView.as_view(), name="retrive-delete-requests"),
]
