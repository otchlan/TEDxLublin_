from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.clickjacking import xframe_options_exempt
from django.views.decorators.csrf import csrf_exempt
from datetime import datetime
from django.shortcuts import redirect
from django.http import JsonResponse
from django.contrib import messages
from .forms import NewsletterForm
import requests
import re

import os

import logging
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

def index(request, lang):
    
    context = {
        'active_page': 'index'
    }
    
    return render(request, f'{lang}/index.html', context=context)


def event(request, lang):
        
    context = {
        'active_page': 'event'
    }
    return render(request, f'{lang}/event.html', context=context)


def about(request, lang):
    
    context = {
        'active_page': 'about'
    }
    return render(request, f'{lang}/about.html', context=context)


def team(request, lang):
    
    context = {
        'active_page': 'team'
    }
    return render(request, f'{lang}/team.html', context=context)


def contact(request, lang):
    
    context = {
        'active_page': 'contact'
    }
    return render(request, f'{lang}/contact.html', context=context)


def contact_speakers(request, lang):
    
    context = {
        'active_page': 'contact'
    }
    return render(request, f'{lang}/forms/speaker_form.html', context=context)


def contact_partners(request, lang):
    
    context = {
        'active_page': 'contact'
    }
    return render(request, f'{lang}/forms/partner_form.html', context=context)


def contact_volunteers(request, lang):
    
    context = {
        'active_page': 'contact'
    }
    return render(request, f'{lang}/forms/volunteer_form.html', context=context)


def partners(request, lang):
    
    context = {
        'active_page': 'partners'
    }
    return render(request, f'{lang}/partners.html', context=context)


def tickets(request, lang):
    
    context = {
        'active_page': 'tickets'
    }
    return render(request, f'{lang}/tickets.html', context=context)

def privacy_policy(request, lang):
    
    context = {
        'active_page': 'privacy_policy'
    }
    return render(request, f'{lang}/privacy_policy.html', context=context)

def terms_and_conditions(request, lang):
    
    context = {
        'active_page': 'terms_and_conditions'
    }
    return render(request, f'{lang}/terms_and_conditions.html', context=context)

def faq(request, lang):
    
    context = {
        'active_page': 'faq'
    }
    return render(request, f'{lang}/faq.html', context=context)

def custom_404(request, exception):
    
    context = {
        'active_page': '404'
    }
    return render(request, '404.html', status=404, context=context)


@xframe_options_exempt
def tickets_iframe(request):
    url = "https://app.evenea.pl/event/tedxlublin2024/?out=1&source=organizer_frame"
    response = requests.get(url)
    
    if response.status_code == 200:
        content = response.text
        
        js_script = '''
        <script>
        function sendHeight() {
            var height = document.body.scrollHeight;
            window.parent.postMessage(height, '*');
            }

        window.onload = sendHeight;
        const selectElement = document.querySelector(".input-small");
        
        selectElement.addEventListener('change', (event) => {
            setTimeout(sendHeight, 50);
        });
        </script>
        '''
        
        modified_content = re.sub(r'</body>', js_script + '</body>', content)
       
        return HttpResponse(modified_content)
    else:
        return HttpResponse('Error fetching the content', status=response.status_code)


@csrf_exempt
def subscribe_newsletter(request):
    logger.debug('POST request received')

    if request.method == 'POST':
        form = NewsletterForm(request.POST)
        if form.is_valid():
            # Extract cleaned data from the form
            email = form.cleaned_data['email']
            name = form.cleaned_data['name']
            privacy_policy = form.cleaned_data['privacy_policy']
            marketing_consent = form.cleaned_data['marketing_consent']
            
            
            logger.debug(os.environ.get("MAILERLITE_GROUPS_IDS").split(" "))
            # Define the data payload
            payload = {
                "email": email,
                "fields": {
                    "name": name,
                },
                "groups": os.environ.get("MAILERLITE_GROUPS_IDS").split(" "),  # Replace with actual group IDs
                "opted_in_at": datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
                "ip_address": request.META.get('REMOTE_ADDR'),
                "status": "active" if marketing_consent else "unconfirmed"
            }

            # MailerLite API request
            mailerlite_url = 'https://connect.mailerlite.com/api/subscribers'
            headers = {
                'Content-Type': 'application/json',
                'Authorization': f'Bearer {os.environ.get("MAILERLITE_API_KEY")}'
            }

            response = requests.post(mailerlite_url, headers=headers, json=payload)
            
            #save to context response status code to pass it as context to the template to display proper message in polish language
            if response.status_code == 200 or response.status_code == 201:
                messages.success(request, 'Dziękujemy za zapisanie się na newsletter!')
            else:
                messages.error(request, 'Nie udało się zapisać na newsletter. Spróbuj ponownie później.')

            logger.debug(f'MailerLite API response: {response.status_code}')

            return redirect(request.META.get('HTTP_REFERER', 'default-redirect-url'), lang='pl')


        else:
            # If form is not valid, return the form with errors as JSON
              return redirect(request.META.get('HTTP_REFERER', 'default-redirect-url'), lang='pl')

    return JsonResponse({'success': False, 'error': 'Invalid request method'})


