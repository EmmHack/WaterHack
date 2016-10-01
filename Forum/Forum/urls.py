from django.conf.urls import include, url
from Thread.views import login, register, edit_profile, thread, edit_post
from django.contrib import admin
admin.autodiscover()
from api.views import AddListConsumers, ListCreateConsumerAddress, \
    ListCreateConsumptionReadings, ListAvgMunicConsumption

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^register/{0,1}$', register),
    url(r'^edit-profile/{0,1}$', edit_profile),
    url(r'^()$', login),
    url(r'^(?:accounts/){0,1}log((?:in)|(?:out))/{0,1}$', login),
    url(r'^(?:home)|(?:thread)/{0,1}$', thread),
    url(r'^edit-post/$', edit_post),
    url(r'^consumers/$', AddListConsumers.as_view(), name='get_create_consumer'),
    url(r'^set_consumers_address/$', ListCreateConsumerAddress.as_view(),
        name='set_consumer_address'),
    url(r'^create_consumption_reading/$', ListCreateConsumptionReadings.as_view(),
        name='create_consumption_reading'),
    url(r'^avg_munic_consumption/(?P<munic_name>[a-zA-Z]+[a-zA-Z0-9]?)/(?P<date>[0-9]{4}-[0-9]{2}-[0-9]{2})$', ListAvgMunicConsumption.as_view(),
        name='avg_munic_consumption'),
]
