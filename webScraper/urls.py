'''
Created on Jul 13, 2020

@author: amiwill
'''
from django.urls import path
from . import views

urlpatterns = [
    path('', views.job_list, name="list"),
    ]