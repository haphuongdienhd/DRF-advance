from django.urls import include, path

from apps.friendships.api import views

urlpatterns = [
    path("", views.BlogListCreateAPIView.as_view(), name="list-friendships"),
    path("me", views.BlogListCreateAPIView.as_view(), name="list-my-friendships"),
    path("<uuid:friendships_id>", views.BlogRetrieveUpdateDestroyAPIView.as_view(), name="retrive-delete-friendships"),
    path("requests", views.BlogListCreateAPIView.as_view(), name="list-requests-to-me"),
    path("requests/new", views.BlogListCreateAPIView.as_view(), name="list-new-requests-to-me"),
    path("requests/me", views.BlogListCreateAPIView.as_view(), name="list-my-requests"),    
    path("requests/<uuid:friendships_id>", views.BlogListCreateAPIView.as_view(), name="retrive-delete-requests"),
]
