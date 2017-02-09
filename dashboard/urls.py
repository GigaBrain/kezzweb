__author__ = 'ripundeep'


from django.conf.urls import url
from dashboard import views
from rest_framework.urlpatterns import format_suffix_patterns


urlpattern= [
    url(r'^login',views.index,name='login'),
    url(r'^home',views.dashboard,name='dashboard'),
    url(r'^logout',views.subscriber_logout,name = 'logout'),
    url(r'^add_user',views.add_user,name = 'add_user'),

]
urlpatterns = format_suffix_patterns(urlpattern)
