from django.urls import include, path

urlpatterns = [
    path("users/", include("apps.users.api.urls")),
    path("auth/", include("apps.users_auth.api.urls")),
    path("blogs/", include("apps.blogs.api.urls")),
]
