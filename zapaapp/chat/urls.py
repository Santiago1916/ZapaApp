from django.urls import path
from . import views
'''
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:pk>/', views.msg_details, name='msg_details'),
]
'''



# path -> listings/urls.py

from django.urls import path 
from .import views

app_name = 'listings'

urlpatterns = [
    path('signup/', views.signup, name='signup'),
]
