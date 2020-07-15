'''
Created on Jul 13, 2020

@author: amiwill
'''
from django.urls import path
from . import views

urlpatterns = [
    path('', views.job_list, name="list"),
    path('delete/<id>', views.delete_offre, name="delete from list")
    ]