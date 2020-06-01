from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('boxes/', views.boxes, name='boxes'),
    path('catalog/', views.catalog, name='catalog'),
    path('form/', views.form, name='form'),
    path('', views.index, name='index'),
    path('index/', views.index, name='index'),
    path('ready/', views.ready, name='ready'),
    path('review/', views.review, name='review'),
    path('sleep/', views.sleep, name='sleep'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('sign_up/', views.sign_up, name='sign_up'),
    path('profile/', views.profile, name='profile')
]