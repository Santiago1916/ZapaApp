from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:pk>/', views.msg_details, name='msg_details'),
]