from django.conf.urls import url
from django.conf.urls import include
from rest_framework import routers
from cinema_api.views import UserViewSet

from . import views

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^login/', views.UserLoginApiView.as_view()),
]