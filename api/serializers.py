__author__ = 'ripundeep'

from rest_framework_mongoengine import serializers
from mongoengine.django.auth import User


class SubscriberSerializer(serializers.DocumentSerializer):
    # A Meta class is a container class with some options or metadata attached to the serializer
    class Meta:
        # Here we specify the model to which this serializer is linked to.
        model = User
        # Here we define a tuple of fields or column names within the said model to be serialized
        fields = ('id', 'username', 'first_name', 'last_name', 'email', 'password', 'is_active', 'is_staff', 'is_superuser')