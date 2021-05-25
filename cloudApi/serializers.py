from django.contrib.auth.models import User, Group
from django.db.models import fields
from cloudApi.models import AzurePrices, AmazonPrices
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']

class AzureApiSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = AzurePrices
        fields = '__all__'

class AmazonApiSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = AmazonPrices
        fields = '__all__'