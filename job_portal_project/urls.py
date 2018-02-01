"""job_portal_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.conf.urls import include 
from django.conf import settings
from django.contrib.auth import views as auth_views
from django.conf.urls.static import static
from django.contrib.auth.forms import PasswordChangeForm
from registration.backends.simple.views import RegistrationView

from jportal import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^admin/', admin.site.urls),
    url(r'^jportal/', include('jportal.urls')), 
    url(r'^chaining/', include('smart_selects.urls')),
    url(r'^employer_page/$', views.employer_page, name='employer_page'),
    #url(r'^login/$', auth_views.login, name='login'),
    #url(r'^logout/$', auth_views.logout, {'next_page': '/'}, name='logout'),
    url(r'^accounts/', include('django.contrib.auth.urls')),
    #url(r'^accounts/', include('registration.backends.simple.urls')),
    url(r'^captcha/', include('captcha.urls')),
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
