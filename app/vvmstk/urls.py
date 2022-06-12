from django.urls import path
from . import views

from vvmstk.views import GroupsListView

urlpatterns = [
    path('', views.Main, name='index'),
    path('groups/', GroupsListView.as_view(), name='groups'),
]