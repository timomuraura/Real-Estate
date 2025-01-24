from django.contrib import admin
from django.urls import path, include
from users import views  # Import the views from the `users` app

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.user_list, name='home'),  # Map the root URL to `user_list`
    path('users/', include('users.urls')),  # Keep other `users/` routes
]
