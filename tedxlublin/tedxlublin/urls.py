<<<<<<< HEAD
=======
#tedxlublin/urls.py
>>>>>>> 4d329a1 (Dodane podstrony /newsletter /game m.in.)
"""
URL configuration for tedxlublin project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
<<<<<<< HEAD
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from django.contrib.staticfiles.storage import staticfiles_storage
from django.views.generic.base import RedirectView


urlpatterns = [
    path('favicon.ico', RedirectView.as_view(url=staticfiles_storage.url('img/favicon.ico'))),
    path('admin/', admin.site.urls),
    path('<str:lang>/', include('webapp.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
=======
from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.storage import staticfiles_storage
from django.views.generic.base import RedirectView
from webapp import views

urlpatterns = [
    path('', RedirectView.as_view(url='/pl/', permanent=True), name='root'),  # Redirects to English by default
    path('favicon.ico', RedirectView.as_view(url=staticfiles_storage.url('img/favicon.ico'))),
    path('admin/', admin.site.urls),
    path('<str:lang>/', include('webapp.urls')),
    path('<lang>/subscribe/', views.subscribeNewsletter, name='subscribeNewsletter'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
>>>>>>> 4d329a1 (Dodane podstrony /newsletter /game m.in.)
