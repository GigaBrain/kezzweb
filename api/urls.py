__author__ = 'ripundeep'

from rest_framework.urlpatterns import format_suffix_patterns
from api import views
from django.conf.urls import url
from django.views.decorators.csrf import csrf_exempt

urlpattern = [
    url(r'^PostSubscriber/$', csrf_exempt(views.CreateSubscriber.as_view())),
    url(r'^GetSubscriberProfileByID/(?P<user_id>[a-z0-9]+)/$',
        csrf_exempt(views.RetrieveOrUpdateOrDeleteSubscriber.as_view())),
    ]
