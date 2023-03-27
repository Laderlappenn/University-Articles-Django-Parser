from django.urls import path
from . import views, views_htmx

urlpatterns = [
    path('', views.acts, name='acts'),
    path('1/', views.tables_1, name='tables_1'),
    path('2/', views.tables_2, name='tables_2'),
    path('3/', views.tables_3, name='tables_3'),
    path('4/', views.tables_4, name='tables_4'),
    path('5/', views.tables_5, name='tables_5'),
    path('6/', views.tables_6, name='tables_6'),


    path('create/1', views.create_1, name='create_1'),
    path('create/2', views.create_2, name='create_2'),
    path('create/3', views.create_3, name='create_3'),
    path('create/4', views.create_4, name='create_4'),
    path('create/5', views.create_5, name='create_5'),
    path('create/6', views.create_6, name='create_6'),

    path('<int:pkey>/', views.act, name='act'),
    path('search', views.act_search),  # POST
    path('search/', views.act_search),  # GET


    path('tables/', views.tables, name='tables'),
    path('tables/first/<int:pkey>/', views.tables_first, name='tables_first'),
    path('tables/second/<int:pkey>/', views.tables_second, name='tables_second'),
    path('tables/first/table', views.tables, name='table_first'),
    path('tables/first/table', views.tables, name='table_second'),

    path('<int:pkey>/edit/', views_htmx.act_edit_form, name='act-edit-form'),
    path('<int:pkey>/edit/save', views_htmx.act_edit),
    path('status/', views_htmx.act_status),
    path('<int:pkey>/accept', views_htmx.accept_or_return_act, name='accept-or-return-act'),
]
