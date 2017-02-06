__author__ = 'ripundeep'

from django.forms import *
from api.models import *

class SignupForm(ModelForm):
    class Meta:
        model = Signup
        fields = ['first_name','last_name','email','username','password','confirm_password']
        widgets = {
            'first_name':TextInput(attrs={'ng-model':'user_info.first_name'}),
            'last_name':TextInput(attrs={'ng-model':'user_info.last_name'}),
            'email':TextInput(attrs={'ng-model':'user_info.email'}),
            'username':TextInput(attrs={'ng-model':'user_info.username'}),
            'password':PasswordInput(attrs={'ng-model':'user_info.pwd'}),
            'confirm_password':PasswordInput(attrs={'ng-model':'user_info.cpwd'}),
        }

class LoginForm(ModelForm):
    class Meta:
        model = Login
        fields = ['username','password']
        widgets = {
            'username':TextInput(attrs={'ng-model':'login_info.username'}),
            'password':PasswordInput(attrs={'ng-model':'login_info.pwd'}),
        }
