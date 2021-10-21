from . import views
from django.urls import path

urlpatterns = [
    path('', views.homepage, name='home'),
    path('about', views.about, name='about'),
    path('services', views.services, name='services'),
    path('contact', views.contact, name='contact'),
]
