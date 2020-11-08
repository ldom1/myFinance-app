from rest_framework import viewsets
from django.db.models import Max, F
from .serializers import AssetsInfoSerializer, OptimAssetsInfoSerializer
from .models import AssetsInfo, OptimAssetsInfo


class AssetsInfoViewSet(viewsets.ModelViewSet):
    queryset = AssetsInfo.objects.all().order_by('-dividende', 'value')
    serializer_class = AssetsInfoSerializer


class TopOptimAssetsInfoViewSet(viewsets.ModelViewSet):
    queryset = OptimAssetsInfo.objects.annotate(max_date=Max('date_update')).filter(date_update=F('max_date')).filter(
        previously_selected=False).exclude(id_asset__isnull=True)
    serializer_class = OptimAssetsInfoSerializer


class TopOptimAssetsInfoPreviouslySelectedViewSet(viewsets.ModelViewSet):
    queryset = OptimAssetsInfo.objects.annotate(max_date=Max('date_update')).filter(date_update=F('max_date')).filter(
        previously_selected=True).exclude(id_asset__isnull=True)
    serializer_class = OptimAssetsInfoSerializer
