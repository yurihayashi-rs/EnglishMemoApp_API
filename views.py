from django.shortcuts import render
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics
from django.contrib.auth.models import User
from .models import Task, HealthBody, SocialRelationship, Travel, SchoolWork, Nature
from rest_framework import viewsets
from .serializers import TaskSerializer, UserSerializer, HealthBodySerializer,SocialRelationshipSerializer, TravelSerializer, SchoolWorkSerializer,NatureSerializer
from .ownpermissions import ProfilePermission

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (ProfilePermission,)


class ManageUserView(generics.RetrieveUpdateAPIView):
    serializer_class = UserSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def get_object(self):
        return self.request.user


class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    authentication_classes = TokenAuthentication,
    permission_classes = (IsAuthenticated,)

class HealthBodyViewSet(viewsets.ModelViewSet):
        queryset = HealthBody.objects.all()
        serializer_class = HealthBodySerializer
        authentication_classes = TokenAuthentication,
        permission_classes = (IsAuthenticated,)


class SocialRelationshipViewSet(viewsets.ModelViewSet):
    queryset = SocialRelationship.objects.all()
    serializer_class = SocialRelationshipSerializer
    authentication_classes = TokenAuthentication,
    permission_classes = (IsAuthenticated,)

class TravelViewSet(viewsets.ModelViewSet):
    queryset = Travel.objects.all()
    serializer_class = TravelSerializer
    authentication_classes = TokenAuthentication,
    permission_classes = (IsAuthenticated,)

class SchoolWorkViewSet(viewsets.ModelViewSet):
    queryset = SchoolWork.objects.all()
    serializer_class = SchoolWorkSerializer
    authentication_classes = TokenAuthentication,
    permission_classes = (IsAuthenticated,)

class NatureViewSet(viewsets.ModelViewSet):
    queryset = Nature.objects.all()
    serializer_class = NatureSerializer
    authentication_classes = TokenAuthentication,
    permission_classes = (IsAuthenticated,)