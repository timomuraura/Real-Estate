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
]
