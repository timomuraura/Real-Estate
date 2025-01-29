from django.urls import path
from . import views

urlpatterns = [
    path('', views.user_list, name='user_list'),
    path('create/', views.user_create, name='user_create'),
    path('update/<int:pk>/', views.user_update, name='user_update'),
    path('delete/<int:pk>/', views.user_delete, name='user_delete'),

     # PropertyType URLs
    path('property-types/create/', views.property_type_create, name='property_type_create'),
    path('property-types/', views.property_type_list, name='property_type_list'),
    path('property-types/update/<int:pk>/', views.property_type_update, name='property_type_update'),
    path('property-types/delete/<int:pk>/', views.property_type_delete, name='property_type_delete'),

    #views urls
    path('views/create/', views.view_create, name='view_create'),
    path('views/',views.view_list, name='view_list'), 
    path('views/update/<int:pk>/', views.view_update, name='view_update'),
    path('views/delete/<int:pk>/', views.view_delete, name='view_delete'),

    #feature urls
    path('features/create/', views.feature_create, name='feature_create'),
    path('features/', views.feature_list, name='feature_list'), 
    path('features/update/<int:pk>/', views.feature_update, name='feature_update'),
    path('features/delete/<int:pk>/', views.feature_delete, name='feature_delete'),

    #Property URLs
    path('properties/create/', views.property_create, name='property_create'),
    path('properties/', views.property_list, name='property_list'),
    path('properties/update/<int:pk>/', views.property_update, name='property_update'),
    path('properties/delete/<int:pk>/', views.property_delete, name='property_delete'),

]
