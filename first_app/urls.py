from django.conf.urls import url
from django.urls import path
from first_app import views

# from django.contrib import admin
# from django.urls import include

urlpatterns = [
    path('', views.index, name='index'),
]
