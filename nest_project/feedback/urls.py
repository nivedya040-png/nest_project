from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('feedback/', views.submit_feedback, name='feedback'),
    path('success/', views.success, name='success'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
]