from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.clickjacking import xframe_options_exempt
from django.views.decorators.csrf import csrf_exempt
from datetime import datetime
from django.shortcuts import redirect
from django.http import JsonResponse
from .forms import NewsletterForm
import requests
import re

import os

import logging
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

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

def privacy_policy(request, lang):
    return render(request, f'{lang}/privacy_policy.html')

def terms_and_conditions(request, lang):
    return render(request, f'{lang}/terms_and_conditions.html')


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

def faq(request, lang):
    return render(request, f'{lang}/faq.html')

def custom_404(request, exception):
    return render(request, '404.html', status=404)


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
            logger.debug(f'MailerLite API response: {response.status_code}')

            return redirect(request.META.get('HTTP_REFERER', 'default-redirect-url'), lang='pl')


        else:
            # If form is not valid, return the form with errors as JSON
              return redirect(request.META.get('HTTP_REFERER', 'default-redirect-url'), lang='pl')

    return JsonResponse({'success': False, 'error': 'Invalid request method'})


