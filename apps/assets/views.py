from rest_framework import viewsets

from .serializers import AssetsInfoSerializer, OptimalAssetsInfoSerializer
from .models import AssetsInfo, OptimalAssetsInfo


class AssetsInfoViewSet(viewsets.ModelViewSet):
    queryset = AssetsInfo.objects.all().order_by('-dividende', 'value')
    serializer_class = AssetsInfoSerializer


class TopOptimalAssetsInfoViewSet(viewsets.ModelViewSet):
    queryset = OptimalAssetsInfo.objects.filter(previously_selected=False).exclude(id_asset__isnull=True)
    serializer_class = OptimalAssetsInfoSerializer


class TopOptimalAssetsInfoPreviouslySelectedViewSet(viewsets.ModelViewSet):
    queryset = OptimalAssetsInfo.objects.filter(previously_selected=True).exclude(id_asset__isnull=True)
    serializer_class = OptimalAssetsInfoSerializer
