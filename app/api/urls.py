from django.urls import path
from . import views

urlpatterns = [
    path('', views.getApi),
    path('groups', views.getGroups, name='Groups list'),
    path('group-detail/<str:pk>/', views.getGroupDetail, name='Groups detail'),
    path('group-create/', views.addGroup, name='add Group'),
    path('group-update/<str:pk>/', views.groupUpdate, name='update group'),
    path('group-delete/<str:pk>/', views.groupDelete, name='delete group'),
]


