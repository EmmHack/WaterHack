from __future__ import unicode_literals
from django.db import models
from django import forms


class submit_post(forms.Form):
    text = forms.CharField(widget=forms.Textarea)


class register_form(forms.Form):
    username = forms.CharField(required=True)
    password = forms.CharField(widget=forms.PasswordInput, required=True)
    first_name = forms.CharField()
    last_name = forms.CharField()
    email = forms.CharField()

# Create your models here.
class Post(models.Model):
    username = models.CharField(max_length=140)
    text = models.CharField(max_length=140)
    time = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        try:
            self.clean_fields()
            super(Post, self).save()
        except:
            raise ValueError()
