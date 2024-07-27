from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('accelerate/', views.accelerate, name='event'),
    path('about/', views.about, name='about'),
    path('team/', views.team, name='team'),
    path('partners/', views.partners, name='partners'),
    path('contact/', views.contact, name='contact'),
    path('contact/speakers/', views.contact_speakers, name='contact_speakers'),
    path('contact/partners/', views.contact_partners, name='contact_partners'),
    path('contact/volunteers/', views.contact_volunteers, name='contact_volunteers'),
    path('tickets/', views.tickets, name='tickets'),
]
