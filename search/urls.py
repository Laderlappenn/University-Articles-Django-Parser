from django.urls import path
from . import views

urlpatterns = [
    path('', views.search, name='search'),
    path('download/', views.download_xls, name='download'),

]