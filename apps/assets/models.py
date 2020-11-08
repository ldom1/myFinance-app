from django.db import models


class Assets(models.Model):
    date = models.DateTimeField(null=True, blank=True)

    id_asset = models.CharField(max_length=100, null=True, blank=True)
    url = models.URLField(max_length=300, null=True, blank=True)
    name = models.CharField(max_length=100, null=True, blank=True)
    value = models.FloatField(null=True, blank=True)
    variation = models.FloatField(null=True, blank=True)
    risk_level = 8
    ouverture = models.FloatField(null=True, blank=True)
    cloture_veille = models.FloatField(null=True, blank=True)
    haut = models.FloatField(null=True, blank=True)
    bas = models.FloatField(null=True, blank=True)
    volume = models.FloatField(null=True, blank=True)
    dividende = models.FloatField(null=True, blank=True)
    date_dividende = models.CharField(max_length=10, null=True, blank=True)

    def __unicode__(self):
        return "{0}".format(self.code, )

    class Meta:
        managed = True


class AssetsInfo(models.Model):
    date_update = models.DateTimeField(null=True, blank=True)
    id_asset = models.CharField(max_length=100, null=True, blank=True)
    name = models.CharField(max_length=100, null=True, blank=True)
    value = models.FloatField(null=True, blank=True)
    variation = models.FloatField(null=True, blank=True)
    dividende = models.FloatField(null=True, blank=True)
    value_3_month = models.FloatField(null=True, blank=True)
    value_1_month = models.FloatField(null=True, blank=True)
    value_1_week = models.FloatField(null=True, blank=True)
    var_3_month = models.FloatField(null=True, blank=True)
    var_1_month = models.FloatField(null=True, blank=True)
    var_1_week = models.FloatField(null=True, blank=True)

    def __unicode__(self):
        return "{0}".format(self.code, )

    class Meta:
        managed = True


class OptimAssetsInfo(models.Model):
    date = models.DateTimeField(null=True, blank=True)
    date_update = models.DateTimeField(null=True, blank=True)
    id_asset = models.CharField(max_length=100, null=True, blank=True)
    name = models.CharField(max_length=100, null=True, blank=True)
    exchange = models.CharField(max_length=5, null=True, blank=True)
    shortname = models.CharField(max_length=100, null=True, blank=True)
    quoteType = models.CharField(max_length=10, null=True, blank=True)
    symbol = models.CharField(max_length=10, null=True, blank=True)
    index = models.CharField(max_length=10, null=True, blank=True)
    score = models.IntegerField(null=True, blank=True)
    typeDisp = models.CharField(max_length=10, null=True, blank=True)
    longname = models.CharField(max_length=100, null=True, blank=True)
    weight = models.FloatField(null=True, blank=True)
    betas = models.FloatField(null=True, blank=True)
    weight_low_var = models.FloatField(null=True, blank=True)
    value = models.FloatField(null=True, blank=True)
    variation = models.FloatField(null=True, blank=True)
    dividende = models.FloatField(null=True, blank=True)
    value_3_month = models.FloatField(null=True, blank=True)
    value_1_month = models.FloatField(null=True, blank=True)
    value_1_week = models.FloatField(null=True, blank=True)
    var_3_month = models.FloatField(null=True, blank=True)
    var_1_month = models.FloatField(null=True, blank=True)
    var_1_week = models.FloatField(null=True, blank=True)
    previously_selected = models.BooleanField(null=True, blank=True)

    def __unicode__(self):
        return "{0}".format(self.code, )

    class Meta:
        managed = True
