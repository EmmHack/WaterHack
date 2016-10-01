from django.conf.urls import url
from views import Home, SignUp, Login, UploadFixture

urlpatterns = [
    url(r'^$', Home.as_view(), name='home'),
    url(r'^home', Home.as_view(), name='home'),
    url(r'^signup', SignUp.as_view(), name='signup'),
    url(r'^login', Login.as_view(), name='login'),
    url(r'^upload_fixture', UploadFixture.as_view(), name='upload_fixture'),
]
