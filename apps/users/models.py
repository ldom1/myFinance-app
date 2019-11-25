from django.db import models
from datetime import datetime


class userInfosSaved(models.Model):

    date = models.DateTimeField(default= datetime.now, null=True, blank=True)
    codePostal = models.IntegerField(null=True, blank=True)
    surface = models.IntegerField(null=True, blank=True)
    prix_m2_max = models.FloatField(null=True, blank=True)
    vente = models.FloatField(null=True, blank=True)
    user_username = models.CharField(max_length=150, null=True, blank=True)

    def __unicode__(self):
        return "{0}".format(self.code, )