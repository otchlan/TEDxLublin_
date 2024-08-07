from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.clickjacking import xframe_options_exempt

import requests
import re


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
