from django.urls import path
from . import views

urlpatterns = [
    path('', views.index,),
    path('about-us', views.about,),
    path('all_currency', views.all_currency)
]
