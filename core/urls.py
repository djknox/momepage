from django.urls import path
from . import views

urlpatterns = [
    path('', views.today, name='index'),
    path('today', views.today, name='today'),
    path('yesterday/', views.yesterday, name='yesterday'),
    path('tomorrow/', views.tomorrow, name='tomorrow'),
]