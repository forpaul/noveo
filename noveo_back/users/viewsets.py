from django.http import HttpResponse
from rest_framework import viewsets
from .serializers import *
from .models import User, State, Group
from passlib.hash import pbkdf2_sha256

class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    model = User

    def get_queryset(self):
        return self.model.objects.prefetch_related('groups').all()

    def create(self, request, *args, **kwargs):
        email = request.data.get('email')
        password = request.data.get('password')
        first_name = request.data.get('first_name')
        last_name = request.data.get('last_name')
        groups = request.data.get('groups')
        state = request.data.get('state')
        encrypt_password = password
        #  pbkdf2_sha256.encrypt(password, rounds=120000, salt_size=32)
        new_user = User.objects.create(email=email, password=encrypt_password, first_name=first_name, last_name=last_name, state=state)
        new_user.groups.set(groups)
        return HttpResponse('ssssss')


class StateViewSet(viewsets.ModelViewSet):
    queryset = State.objects.all()
    serializer_class = StateSerializer

class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
