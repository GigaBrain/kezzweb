from django.shortcuts import render, redirect
from django.http import HttpResponse,HttpResponseRedirect
from mongoengine.django.auth import User
from api.forms import *
from api.models import *
from api.serializers import *
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import login, authenticate,logout
from django.contrib.auth.decorators import login_required
from django.template.context_processors import csrf
from mongoengine.queryset import DoesNotExist
from datetime import datetime
import json
import pdb

# Create your views here.


@csrf_exempt
def index(request):
    loginform = LoginForm()
    if request.method == "POST":
        csrf_dict = {}
        csrf_dict.update(csrf(request))
        username =  request.POST.get('username','')
        password = request.POST.get('password','')
        try:
            user = User.objects.get(username=username)
            if user.check_password(password):
                user.backend = 'mongoengine.django.auth.MongoEngineBackend'
                user = authenticate(username=username, password=password)
                login(request, user)
                request.session.set_expiry(60*60 * 1)
                user_id = str(user.pk)
                if request.POST.has_key('next'):
                    return redirect(request.POST['next'])
                else:
                    return redirect('/dashboard/home')
            else:
                return render(request,'index.html',{'form':loginform})
        except DoesNotExist:
            return render(request,'index.html',{'form':loginform})
    else:
        return render(request,'index.html',{'form':loginform})


@login_required(login_url='/dashboard/login')
@csrf_exempt
def dashboard(request):
    csrf_dict = {}
    csrf_dict.update(csrf(request))
    host = request.META['HTTP_HOST']
    return render(request, 'dashboard_template/template.html')

@csrf_exempt
def subscriber_logout(request):
    logout(request)
    response = HttpResponse()
    response.content = str(HttpResponse.status_code)
    return response



# @csrf_exempt
# def signup(request):
#     signupform = SignupForm()
#     admin = User()
#     admin.first_name =  'Admin'
#     admin.last_name = 'Kezz'
#     admin.username = 'admin'
#     admin.set_password('admin@123')
#     admin.email = 'hundrel@outlook.com'
#     admin.is_active = True
#     admin.is_staff = True
#     admin.is_superuser = True
#     admin.date_joined = datetime.now()
#     admin.last_login = datetime.now()
#     admin.save()
#     return render(request,'signup.html',{'form':signupform})


#125794027