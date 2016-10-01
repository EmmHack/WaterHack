from django.conf.urls import url

from api.views import AddListConsumers, ListCreateConsumerAddress, \
    ListCreateConsumptionReadings

urlpatterns = [
    url(r'^consumers/$', AddListConsumers.as_view(), name='get_create_consumer'),
    url(r'^set_consumers_address/$', ListCreateConsumerAddress.as_view(),
        name='set_consumer_address'),
    url(r'^create_consumption_reading/$', ListCreateConsumptionReadings.as_view(),
        name='create_consumption_reading'),
]
