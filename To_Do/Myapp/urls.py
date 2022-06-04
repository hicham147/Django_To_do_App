from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home,name='home'),
    path('update/<int:pk>/', views.Update_task,name='update_task'),

]
