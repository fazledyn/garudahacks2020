from django.shortcuts import render
from rest_framework import viewsets

from django.contrib.auth.models import User
from api.models import Donor, Newsletter

from api.serializers import (
    DonorSerializer, 
    NewsletterSerializer, 
    UserSerializer
)


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class DonorViewSet(viewsets.ModelViewSet):
    queryset = Donor.objects.all()
    serializer_class = DonorSerializer


class NewsletterViewSet(viewsets.ModelViewSet):
    queryset = Newsletter.objects.all()
    serializer_class = NewsletterSerializer