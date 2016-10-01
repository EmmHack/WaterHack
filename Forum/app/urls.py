from django.conf.urls import url
from views import Home, login,register
from django.contrib.auth import views

urlpatterns = [
    url(r'^$', Home.as_view(), name='home'),
    url(r'^home', Home.as_view(), name='home'),
    url(r'^signup/{0,1}$', register, name='signup'),
    url(r'^(?:accounts/){0,1}log((?:in)|(?:out))/{0,1}$', login,name='loginout'),
]
