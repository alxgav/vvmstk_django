from django.urls import path
from . import views

urlpatterns = [
    path('', views.Main, name='index'),
    path('groups/', views.Groups, name='groups'),
]