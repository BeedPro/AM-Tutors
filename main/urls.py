from django.urls import path
from main import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('tuition/', views.tuition, name='tuition'),
    path('reviews/', views.reviews, name='reviews'),
    path('pricing/', views.pricing, name='pricing'),
    path('contacts/', views.contacts, name='contacts'),
]