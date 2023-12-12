from datetime import timedelta

from dj_rest_auth.registration.views import RegisterView
from dj_rest_auth.views import LoginView

from django.conf import settings
from django.utils.translation import gettext_lazy as _

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics

from apps.users.api.serializers import UserPasswordChangeSerializer, UserSerializer

# Create your views here.
class CustomRegisterView(RegisterView):
    def get_response_data(self, user):
        return UserSerializer(user).data
    
class CustomPasswordChange(generics.GenericAPIView):
    
    serializer_class=UserPasswordChangeSerializer
    
    def post(self, request, *args, **kwargs):
        user = self.request.user
        serializer = UserPasswordChangeSerializer(data=self.request.data, context={"user": user})
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"detail": _("New password has been saved.")})