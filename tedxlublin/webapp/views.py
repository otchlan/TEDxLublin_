from django.shortcuts import render


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

def custom_404(request, exception):
    return render(request, '404.html', status=404)