from django.urls import path
from . import views




urlpatterns = [
    path('', views.home_view, name=''),
    path('login', views.login, name='login'),
    path("signup/", views.signup, name="signup"),
    path('home', views.home_view, name='home'),
    path('user', views.user_homepage_view, name='user'),
    path('artisan', views.artisan_homepage_view, name='artisan'),
    path('submit_request/', views.submit_request, name='submit_request'),  
    path('submit_feedback/', views.submit_feedback, name='submit_feedback'),
    path('logout/', views.logout_view, name='logout'),
    path('get-artisans/', views.get_artisans, name='get_artisans'),
    path('get_requests_and_feedback/', views.get_requests_and_feedback, name='get_requests_and_feedback'),
]