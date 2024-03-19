
from django.urls import path ,include
from . import views
from .models import UserModels


urlpatterns = [
    path('',views.getUser, name='getUser'),
    path('data/<int:pk>/',views.userDetail, name= 'userDetail')
    ]