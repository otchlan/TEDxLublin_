from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.clickjacking import xframe_options_exempt
import logging

import requests
import re

logger = logging.getLogger( __name__ )
logger.setLevel(logging.DEBUG)
logger.debug("Loaded views logger")

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
    logger.debug("Tickets view")
    return render(request, f'{lang}/tickets.html')

@xframe_options_exempt
def tickets_iframe(request):
    url = "https://app.evenea.pl/event/tedxlublin2024/?out=1&source=organizer_frame"
    response = requests.get(url)
    logger.debug(f"Response status code: {response.status_code}")
    
    if response.status_code == 200:
        content = response.text
        
        # Define your custom CSS
        custom_css = '''
        .well {
            background-color: #FBFBFB !important;
        }
        
        .ticket-header {
            background-color: #eb0028 !important;
        }
        
    '''
        # new_href = '/assets/bootstrap/css/bootstrap.min.css'
        # Regex pattern to find the specific <link> tag with href containing 'main.css'
        # main_css_pattern = r'(<link\s+[^>]*href="https:\/\/app[^"]*main\.css")([^>]*>)'
        
        # Replace the href attribute with the new href link
        # modified_content = re.sub(main_css_pattern, rf'\1{new_href}\2', content)
        modified_content = content.replace('</body>', f'<style>{custom_css}</style></body>')
        return HttpResponse(modified_content)
    else:
        return HttpResponse('Error fetching the content', status=response.status_code)

def faq(request, lang):
    return render(request, f'{lang}/faq.html')

def custom_404(request, exception):
    return render(request, '404.html', status=404)
