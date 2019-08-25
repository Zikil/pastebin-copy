from django.urls import path
from django.contrib import auth
from django.urls import include


from .views import *

urlpatterns = [
    path('register/', MyRegisterFormView.as_view(), name='register_url'),
    path('', include('django.contrib.auth.urls')),
]
