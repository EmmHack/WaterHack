import json

from django.test import TestCase
from django.shortcuts import reverse
from rest_framework.test import APITestCase


class AppTest(TestCase):

    def test_upload_fixture(self):
       url = reverse('upload_fixture')  
       response = self.client.get(url)
       result = json.loads(response.content)
       self.assertTrue(result['result'], 'data uploaded successfully')

