from django.http import HttpResponse
from rest_framework import viewsets
from .serializers import *
from .models import User, State, Group
from passlib.hash import pbkdf2_sha256

class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    model = User

    def get_queryset(self):
        return self.model.objects.select_related('group', 'state').all()


class StateViewSet(viewsets.ModelViewSet):
    queryset = State.objects.all()
    serializer_class = StateSerializer

class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
