from django.contrib import admin
from django.urls import path
from . import views
from demoapp.views import *
urlpatterns = [

    #Text To HTML
    path('editor', views.editor, name='editor'),

]
