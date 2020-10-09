from rest_framework import serializers

from .models import AssetsInfo


class AssetsInfoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = AssetsInfo
        fields = ('date_update', 'id_asset', 'name', 'value', 'variation', 'dividende',
                  'value_3_month', 'value_1_month', 'value_1_week', 'var_3_month', 'var_1_month',
                  'var_1_week')
