from django.urls import path
from . import views



urlpatterns = [

    path('login', views.index, name='login'),
    path('task/<int:pk>/', views.task, name='task'),
    path('taske', views.taske, name='taske'),
    path('', views.home, name='home'),
    path('account', views.account, name='account'),

]
