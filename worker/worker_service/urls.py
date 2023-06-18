
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('data/update/', views.update),
    path('data/get/', views.get),
    path('data/delete/', views.delete),
    path('data/create/', views.create),
]