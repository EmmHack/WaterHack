"""waterly URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
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
from django.conf.urls import url, include
from Thread.views import login, register, edit_profile, thread, edit_post
from django.contrib import admin

urlpatterns = [

    url(r'^$',include('Thread.urls')),
    url(r'^app',include('Thread.urls')),
    url(r'^(?:accounts/){0,1}log((?:in)|(?:out))/{0,1}$', login),
    url(r'^(?:forum)|(?:thread)/{0,1}$', thread),
    url(r'^signup/{0,1}$', register),
    url(r'^edit-profile/{0,1}$', edit_profile),
    url(r'^edit-post/$', edit_post),
    url(r'^api/',include('api.urls')),
    url(r'^admin/', admin.site.urls),
]
