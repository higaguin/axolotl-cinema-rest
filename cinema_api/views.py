from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings

from django.contrib.auth.models import User
from cinema_api.serializers import UserSerializer
from rest_framework.authentication import TokenAuthentication
from cinema_api.permissions import IsLoggedInUserOrAdmin, IsAdminUser


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    authentication_classes = (TokenAuthentication,)

    def get_permissions(self):
        permission_classes = []
        if self.action == 'create':
            permission_classes = [AllowAny]
        elif self.action == 'retrieve' or self.action == 'update' or self.action == 'partial_update':
            permission_classes = [IsLoggedInUserOrAdmin]
        # elif self.action == 'list' or self.action == 'destroy':
        #     permission_classes = [IsAdminUser]
        return [permission() for permission in permission_classes]

class UserLoginApiView(ObtainAuthToken):
    """HANDLE CREATING USER AUTHETICATION TOKENS"""
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES