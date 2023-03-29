from django.urls import path
from . import views

urlpatterns = [
    path('', views.search, name='search'),
    path('new/', views.search_new, name='search_new'),
    path('download/', views.download_xls, name='download'),

]