"""instaclone URL Configuration

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
from django.conf.urls import url,include
from django.contrib import admin
from . import views
from django.contrib.auth import views as viewauth
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.welcome, name="welcome"),
    url(r'^index/', views.home, name="home"),
    url(r'^profile/\d+', views.profile, name="profile"),
    url(r'^search/', views.search, name="search_results"),
    url(r'^accounts/', include('registration.backends.simple.urls')),
    url(r'^logout/', viewauth.logout, {"next_page":'/index'}),
    url(r'^tinymce/', include('tinymce.urls')),
    url(r'^new/post$', views.new_post, name="new_post"),
    url(r'^update/profile$', views.update_profile, name="update_profile"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)