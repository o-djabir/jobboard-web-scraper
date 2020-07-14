'''
Created on Jul 13, 2020

@author: amiwill
'''
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('', views.index2, name='index2'),
    ]