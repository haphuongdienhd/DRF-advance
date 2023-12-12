from django.urls import include, path

from apps.blogs.api import views

urlpatterns = [
    path("", views.BlogListCreateAPIView.as_view(), name="list-or-create-blog"),
    path("<uuid:blog_id>", views.BlogRetrieveUpdateDestroyAPIView.as_view(), name="retrive-update-delete-blog"),
]
