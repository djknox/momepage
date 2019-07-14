from django.urls import path
from . import views

urlpatterns = [
    path('', views.today, name='index'),
    path('today', views.today, name='today'),
    path('previous-day/', views.previous_day, name='previous-day'),
    path('next-day/', views.next_day, name='next-day'),
]