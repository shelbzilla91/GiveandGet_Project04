from django.urls import path
from . import views

urlpatterns = [
    path('', views.User_index, name='User_index'),
]