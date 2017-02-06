from django.shortcuts import render

# Create your views here.

from rest_framework_mongoengine import generics

from api.serializers import *

class CreateSubscriber(generics.CreateAPIView):
    # Here we have defined which serializer to use when we send a request to this view.
    # The inherited class and the serializer handle the client request in coordination.
    serializer_class = SubscriberSerializer

    def get_queryset(self):
        user_id = self.kwargs['user_id']
        return User.objects.filter(owner=user_id)

class RetrieveOrUpdateOrDeleteSubscriber(generics.RetrieveUpdateDestroyAPIView):
    # Here we have defined which serializer to use when we send a request to this view.
    # The inherited class and the serializer handle the client request in coordination.
    serializer_class = SubscriberSerializer

    # Here we have override an in-built function to retrieve, update or delete a subscriber profile using subscriber ID.
    # The subscriber ID is passed as a parameter in the api URL.
    def get_object(self):
        return User.objects.get(pk=self.kwargs['id'])
