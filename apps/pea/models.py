from django.db import models

# Create your models here.
class PEA(models.Model):

    buying_date = models.DateTimeField(null=True, blank=True)
    selling_date = models.DateTimeField(null=True, blank=True)
    date = models.DateTimeField(null=True, blank=True)
    id_investment = models.FloatField(null=True, blank=True) 
    name_asset = models.CharField(max_length=70, null=True, blank=True)
    description = models.CharField(max_length=200, null=True, blank=True)
    initial_amount = models.FloatField(null=True, blank=True) 
    current_value =  models.FloatField(null=True, blank=True)
    currency = models.CharField(max_length=200, null=True, blank=True)
    user_username = models.CharField(max_length=150, null=True, blank=True)


    def __unicode__(self):
        return "{0}".format(self.code, )