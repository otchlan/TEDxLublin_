<<<<<<< HEAD
from django.urls import path

=======
# webapp/urls.py
from django.urls import path
>>>>>>> 4d329a1 (Dodane podstrony /newsletter /game m.in.)
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('accelerate/', views.accelerate, name='event'),
    path('about/', views.about, name='about'),
    path('team/', views.team, name='team'),
    path('partners/', views.partners, name='partners'),
    path('contact/', views.contact, name='contact'),
    path('tickets/', views.tickets, name='tickets'),
<<<<<<< HEAD
=======
    path('game/', views.game, name='game'),
    path('newsletter/', views.newsletter, name='newsletter'),
>>>>>>> 4d329a1 (Dodane podstrony /newsletter /game m.in.)
    path('faq/', views.faq, name='faq'),
    path('contact/speakers/', views.contact_speakers, name='contact_speakers'),
    path('contact/partners/', views.contact_partners, name='contact_partners'),
    path('contact/volunteers/', views.contact_volunteers, name='contact_volunteers'),
<<<<<<< HEAD
]
=======
    path('subscribe/', views.subscribeNewsletter, name='subscribeNewsletter'),
]
>>>>>>> 4d329a1 (Dodane podstrony /newsletter /game m.in.)
