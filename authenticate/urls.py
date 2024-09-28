from django.urls import path

from . import views

app_name = 'authenticate'

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('login/', views.custom_login, name='login/'),
    path('register/', views.)
]