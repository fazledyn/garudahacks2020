from rest_framework import serializers

#Models
from django.contrib.auth.models import User
from api.models import Donor, Newsletter


class UserSerializer(serializers.HyperlinkedModelSerializer):
    username = serializers.ReadOnlyField()
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']


class DonorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Donor
        exclude = []


class NewsletterSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Newsletter
        exclude =[]