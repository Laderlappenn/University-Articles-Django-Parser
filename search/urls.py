from django.urls import path
from . import views

urlpatterns = [
    path('', views.search, name='search'),
    path('new/<int:num>/<int:id>/', views.search_new, name='search_new'),
    path('articles/', views.search_articles, name='search_articles'),

    path('download/', views.download_xls, name='download'),

]