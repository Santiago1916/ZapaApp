from django.urls import path
from . import views



urlpatterns = [
    path('', views.home, name='home'),
    path('<str:canal>/', views.canal, name='canal'),
    path('check_canal', views.check_canal, name='check_canal'),
    path('send', views.send, name='send'),
    path('getMessages/<str:canal>/', views.getMessages, name='getMessages'),
]
