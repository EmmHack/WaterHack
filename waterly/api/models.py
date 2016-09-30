from __future__ import unicode_literals

from django.db import models


class Address(models.Model):
    building_name = models.CharField(max_length=30)
    street_no = models.IntegerField()
    suburb_name = models.CharField(max_length=30)
    municipality_name = models.CharField(max_length=30)
    province_name = models.CharField(max_length=30)


class Meter(models.Model):
    meter_no = models.CharField(max_length=15, primary_key=True)
    daily_consumption = models.FloatField()


class Consumer(models.Model):
    name = models.CharField(max_length=30)
    meter = models.OneToOneField(
            Meter,
            on_delete=models.CASCADE,
            primary_key=True,
    )
    address = models.OneToOneField(
            Address,
            on_delete=models.CASCADE,
    )
