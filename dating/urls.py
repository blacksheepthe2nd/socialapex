from django.urls import path 
from django.contrib.auth import views as auth_views 
from . import views 
 
urlpatterns = [
    path('profile/<int:pk>/', views.profile_detail, name='profile_detail'), 
    path('login/', views.login_view, name='login'), 
    path('register/', views.register_view, name='register'), 
    path('logout/', auth_views.LogoutView.as_view(next_page='/'), name='logout'), 
    path('dashboard/', views.dashboard, name='dashboard'), 
    path('individual/', views.individual_view, name='individual_view'), 
    path('grid/', views.grid_view, name='grid_view'), 
    path('create-profile/', views.create_profile, name='create_profile'), 
    path('edit-profile/', views.edit_profile, name='edit_profile'), 
] 
