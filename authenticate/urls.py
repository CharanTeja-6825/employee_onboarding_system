from django.urls import path

from authenticate import views

urlpatterns = [
    path('', views.homepage, name='homepage'),

]