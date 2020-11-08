from rest_framework import serializers

from .models import AssetsInfo, OptimAssetsInfo


class AssetsInfoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = AssetsInfo
        fields = ('date_update', 'id_asset', 'name', 'value', 'variation', 'dividende',
                  'value_3_month', 'value_1_month', 'value_1_week', 'var_3_month', 'var_1_month',
                  'var_1_week')


class OptimAssetsInfoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = OptimAssetsInfo
        fields = ('date_update', 'id_asset', 'name', 'exchange', 'shortname', 'quoteType', 'symbol', 'index', 'value',
                  'variation', 'dividende', 'score', 'typeDisp', 'longname', 'weight', 'betas', 'weight_low_var',
                  'value_3_month', 'value_1_month', 'value_1_week', 'var_3_month', 'var_1_month',
                  'var_1_week', 'previously_selected')
