from django.conf.urls import url

from api.views import GetCreateConsumer

urlpatterns = [
    url(r'^consumers/$', GetCreateConsumer.as_view(), name='get_create_consumer'),
]
