from rest_framework import serializers

from .models import AssetsInfo, OptimAssetsInfo, AssetsCheckLimits


class AssetsInfoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = AssetsInfo
        fields = ('date_update', 'id_asset', 'name', 'value', 'variation', 'dividende',
                  'value_3_month', 'value_1_month', 'value_1_week', 'var_3_month', 'var_1_month',
                  'var_1_week')


class OptimAssetsInfoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = OptimAssetsInfo
        fields = ('date_update', 'id_asset', 'name', 'url', 'shortname', 'value',
                  'variation', 'dividende',  'longname', 'date')


class AssetsLimitCheckerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = AssetsCheckLimits
        fields = ('name', 'down_limit', 'up_limit')

    def create(self, validated_data):
        asset_limit, created = AssetsCheckLimits.objects.update_or_create(
            name=validated_data.get('name', None),
            defaults={'down_limit': validated_data.get('down_limit', None),
                      'up_limit': validated_data.get('up_limit', None)})
        return asset_limit
