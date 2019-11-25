from django.db import models
from datetime import datetime

# Create your models here.
class fundsCA(models.Model):

    date = models.DateTimeField(default=datetime.now, null=True, blank=True)
    date_dernier_cours = models.DateTimeField(null=True, blank=True)

    id_fund = models.CharField(max_length=100, null=True, blank=True)
    url = models.URLField(max_length=300, null=True, blank=True)
    name = models.CharField(max_length=100, null=True, blank=True)
    name_id = models.CharField(max_length=100, null=True, blank=True)
    value = models.FloatField(null=True, blank=True)
    variation = models.FloatField(null=True, blank=True)
    risk_level = models.IntegerField(null=True, blank=True)
    net_asset = models.FloatField(null=True, blank=True)

    def __unicode__(self):
    	return "{0}".format(self.code, )