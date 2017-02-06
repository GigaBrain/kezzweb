__author__ = 'ripundeep'


from django.conf.urls import url
from dashboard import views
from rest_framework.urlpatterns import format_suffix_patterns


urlpattern= [
    url(r'^login',views.index,name='login'),
    url(r'^home',views.dashboard,name='dashboard'),
    url(r'^check_auth',views.check_auth,name='auth')
    # url(r'^subscribe/',views.signup,name='signup'),

]
urlpatterns = format_suffix_patterns(urlpattern)
