from django.urls import path 
from . import views 
 
urlpatterns = [ 
    path('', views.dashboard, name='dashboard'), 
    path('register/', views.register, name='register'), 
    path('create-profile/', views.create_profile, name='create_profile'), 
    path('grid/', views.profiles_grid, name='profiles_grid'), 
    path('matches/', views.matches, name='matches'), 
] 
