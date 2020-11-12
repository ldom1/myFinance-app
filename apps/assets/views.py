from rest_framework import viewsets
from django.db.models import Max, F
from .serializers import AssetsInfoSerializer, OptimAssetsInfoSerializer
from .models import AssetsInfo, OptimAssetsInfo


class AssetsInfoViewSet(viewsets.ModelViewSet):
    queryset = AssetsInfo.objects.all().order_by('-dividende', 'value')
    serializer_class = AssetsInfoSerializer


class TopOptimAssetsInfoViewSet(viewsets.ModelViewSet):
    previously_selected = False
    last_date = OptimAssetsInfo.objects.filter(previously_selected=previously_selected).latest(
        'date_update').date_update
    queryset = OptimAssetsInfo.objects.filter(date_update=last_date).filter(
        previously_selected=previously_selected).exclude(id_asset__isnull=True)
    serializer_class = OptimAssetsInfoSerializer


class TopOptimAssetsInfoPreviouslySelectedViewSet(viewsets.ModelViewSet):
    previously_selected = True
    last_date = OptimAssetsInfo.objects.filter(previously_selected=previously_selected).latest(
        'date_update').date_update
    queryset = OptimAssetsInfo.objects.filter(date_update=last_date).filter(
        previously_selected=previously_selected).exclude(id_asset__isnull=True)
    serializer_class = OptimAssetsInfoSerializer
