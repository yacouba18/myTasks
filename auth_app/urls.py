from django.contrib import admin
from django.urls import path
from auth_app import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/',auth_views.LoginView.as_view(template_name='login.html'), name = 'login'),
    path('logout/',auth_views.LogoutView.as_view(template_name='logout.html'), name = 'logout'),
    path('register/', views.register, name='register'),
]