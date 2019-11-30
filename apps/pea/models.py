from django.db import models
from datetime import datetime

# Create your models here.
class PEA(models.Model):

    date = models.DateTimeField(null=True, blank=True)
    id_pea = models.IntegerField(null=True, blank=True)
    name_pea = models.CharField(max_length=200, null=True, blank=True)
    description = models.CharField(max_length=200, null=True, blank=True)
    current_value =  models.FloatField(null=True, blank=True)
    currency = models.CharField(max_length=5, null=True, blank=True)
    risk = models.IntegerField(null=True, blank=True)
    user_username = models.CharField(max_length=150, null=True, blank=True)


    def __unicode__(self):
        return "{0}".format(self.code, )

class PEAHistory(models.Model):

    date = models.DateTimeField(null=True, blank=True)
    id_pea = models.IntegerField(null=True, blank=True)
    name_pea = models.CharField(max_length=200, null=True, blank=True)
    value =  models.FloatField(null=True, blank=True)
    currency = models.CharField(max_length=5, null=True, blank=True)
    risk = models.IntegerField(null=True, blank=True)
    user_username = models.CharField(max_length=150, null=True, blank=True)


    def __unicode__(self):
        return "{0}".format(self.code, )

class Order(models.Model):

    buying_date = models.DateTimeField(null=True, blank=True)
    date = models.DateTimeField(default=datetime.now, null=True, blank=True)
    selling_date = models.DateTimeField(null=True, blank=True)
    date = models.DateTimeField(null=True, blank=True)
    id_order = models.IntegerField(null=True, blank=True)
    id_pea = models.IntegerField(null=True, blank=True)
    name_pea = models.CharField(max_length=200, null=True, blank=True)
    id_asset = models.CharField(max_length=70, null=True, blank=True)
    initial_amount = models.FloatField(null=True, blank=True) 
    current_value =  models.FloatField(null=True, blank=True)
    currency = models.CharField(max_length=5, null=True, blank=True)
    live = models.IntegerField(null=True, blank=True)
    user_username = models.CharField(max_length=150, null=True, blank=True)


    def __unicode__(self):
        return "{0}".format(self.code, )