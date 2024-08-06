<<<<<<< HEAD
from django.shortcuts import render
=======
#webapp/views.py
from django.shortcuts import render
from django.conf import settings
from django.http import JsonResponse
from airtable import Airtable
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt
>>>>>>> 4d329a1 (Dodane podstrony /newsletter /game m.in.)


def index(request, lang):
    return render(request, f'{lang}/index.html')


def accelerate(request, lang):
    return render(request, f'{lang}/accelerate.html')


def about(request, lang):
    return render(request, f'{lang}/about.html')


def team(request, lang):
    return render(request, f'{lang}/team.html')


def contact(request, lang):
    return render(request, f'{lang}/contact.html')


def contact_speakers(request, lang):
    return render(request, f'{lang}/forms/speaker_form.html')


def contact_partners(request, lang):
    return render(request, f'{lang}/forms/partner_form.html')


def contact_volunteers(request, lang):
    return render(request, f'{lang}/forms/volunteer_form.html')


def partners(request, lang):
    return render(request, f'{lang}/partners.html')


def tickets(request, lang):
    return render(request, f'{lang}/tickets.html')

def faq(request, lang):
    return render(request, f'{lang}/faq.html')

<<<<<<< HEAD
def custom_404(request, exception):
    return render(request, '404.html', status=404)
=======
def game(request, lang):
    return render(request, f'{lang}/game.html')

def newsletter(request, lang):
    # Make sure lang is not None or empty
    if not lang:
        lang = 'pl'
    return render(request, f'{lang}/newsletter.html', {'lang': lang})


def custom_404(request, exception):
    return render(request, '404.html', status=404)

@require_http_methods(["POST"])
def subscribeNewsletter(request, lang):
    # Get data from the form
    name = request.POST.get('name')
    email = request.POST.get('email')
    
    # Initialize Airtable client
    airtable = Airtable(settings.AIRTABLE_BASE_ID, settings.AIRTABLE_TABLE_NAME, api_key=settings.AIRTABLE_API_KEY)
    
    # Insert data into Airtable
    record = airtable.insert({'Name': name, 'Email': email})
    
    # You could add error handling here to check if the insertion was successful

    return JsonResponse({"message": "Thank you for subscribing!", "lang": lang})
>>>>>>> 4d329a1 (Dodane podstrony /newsletter /game m.in.)
