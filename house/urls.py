from django.urls import path
from .views import *

urlpatterns = [
    path('create',HouseCreateView.as_view(),name='house_create'),
    path('list',HouseListView.as_view(),name='house_list'),
]