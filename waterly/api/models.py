from __future__ import unicode_literals

from django.db import models


class Address(models.Model):
    building_name = models.CharField(max_length=30)
    street_no = models.IntegerField()
    suburb_name = models.CharField(max_length=30)
    municipality_name = models.CharField(max_length=30)
    province_name = models.CharField(max_length=30)


class Consumer(models.Model):
    meter_no = models.CharField(max_length=15, primary_key=True)
    name = models.CharField(max_length=30)
    address = models.OneToOneField(
            Address,
            on_delete=models.CASCADE,
    )
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)


class Consumption(models.Model):
    meter_no = models.CharField(max_length=15)
    value = models.FloatField()
    consumer = models.ForeignKey(Consumer, on_delete=models.CASCADE)
    date = models.DateField()
