
from django.urls import path
from . import views

urlpatterns = [
    path('', views.welcome, name='welcome'),           
    path('users/', views.users, name='users'),
    path('form/', views.form, name='form'),
    # path('formsubmited/', views.form, name='form'),
]
