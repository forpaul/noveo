from django.urls import path

from .viewsets import UserViewSet, StateViewSet, GroupViewSet
from django.urls import path, include
from rest_framework import routers
from django.conf import settings

router = routers.DefaultRouter()
router.register('users', UserViewSet, base_name='users')
router.register('states', StateViewSet, base_name='states')
router.register('groups', GroupViewSet, base_name='groups')


urlpatterns = [
    path('', include(router.urls)),
]
