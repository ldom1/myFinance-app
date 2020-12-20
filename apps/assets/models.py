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
    date = models.DateTimeField(null=True, blank=True)
    date_update = models.DateTimeField(null=True, blank=True)
    id_asset = models.CharField(max_length=100, null=True, blank=True)
    name = models.CharField(max_length=100, null=True, blank=True)
    longname = models.CharField(max_length=100, null=True, blank=True)
    symbol = models.CharField(max_length=100, null=True, blank=True)
    url = models.URLField(max_length=300, null=True, blank=True)
    value = models.FloatField(null=True, blank=True)
    asset_return = models.FloatField(null=True, blank=True)
    variation = models.FloatField(null=True, blank=True)
    dividende = models.FloatField(null=True, blank=True)
    date_dividende = models.CharField(max_length=10, null=True, blank=True)
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
    url = models.URLField(max_length=300, null=True, blank=True)
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


class AssetsCheckLimits(models.Model):
    date = models.DateTimeField(null=True, blank=True)
    date_update = models.DateTimeField(null=True, blank=True)
    id_asset = models.CharField(max_length=100, null=True, blank=True)
    name = models.CharField(max_length=100, null=True, blank=True)
    symbol = models.CharField(max_length=10, null=True, blank=True)
    longname = models.CharField(max_length=100, null=True, blank=True)
    down_limit = models.FloatField(null=True, blank=True)
    down_limit_knocked = models.BooleanField(null=True, blank=True)
    up_limit = models.FloatField(null=True, blank=True)
    up_limit_knocked = models.BooleanField(null=True, blank=True)
    url = models.URLField(max_length=300, null=True, blank=True)
    value = models.FloatField(null=True, blank=True)
    value_objective = models.FloatField(null=True, blank=True)
    potential_percent = models.FloatField(null=True, blank=True)

    def __unicode__(self):
        return "{0}".format(self.code, )

    class Meta:
        managed = True


class RecommendedAssetsToBuy(models.Model):
    date = models.DateTimeField(null=True, blank=True)
    date_date = models.DateTimeField(null=True, blank=True)
    id_asset = models.CharField(max_length=100, null=True, blank=True)
    name = models.CharField(max_length=100, null=True, blank=True)
    url = models.URLField(max_length=300, null=True, blank=True)
    action = models.CharField(max_length=100, null=True, blank=True)
    value = models.FloatField(null=True, blank=True)
    value_objective = models.FloatField(null=True, blank=True)
    potential_percent = models.FloatField(null=True, blank=True)
    nb_analysts = models.IntegerField(null=True, blank=True)
    net_benefit_in_eur = models.FloatField(null=True, blank=True)
    rentability_n_percent = models.FloatField(null=True, blank=True)
    price_earning_ratio_n = models.FloatField(null=True, blank=True)
    price_earning_ratio_n_plus_1 = models.FloatField(null=True, blank=True)

    def __unicode__(self):
        return "{0}".format(self.code, )

    class Meta:
        managed = True
