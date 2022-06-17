from django.urls import path
from . import views

from vvmstk.views import GroupsListView

urlpatterns = [
    path('', views.Main, name='index'),
    path('groups/', GroupsListView.as_view(), name='groups'),
    # path('students/', StudentListView.as_view(), name='students'),
    path('students/<str:pk>/', views.student_list_view, name='students'),
    path('groups_by_kateg/<str:pk>/', views.groups_by_kategory, name='groups_by_kateg'),
]