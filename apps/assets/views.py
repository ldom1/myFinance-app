from rest_framework import viewsets
from django.db.models import Q
from .serializers import AssetsInfoSerializer, OptimAssetsInfoSerializer, AssetsLimitCheckerSerializer, \
    RecommendedAssetsSerializer
from .models import AssetsInfo, OptimAssetsInfo, AssetsCheckLimits, RecommendedAssetsToBuy


class AssetsInfoViewSet(viewsets.ModelViewSet):
    """
    queryset = AssetsInfo.objects.all().order_by('-dividende', 'value')
    serializer_class = AssetsInfoSerializer
    """


class TopOptimAssetsInfoViewSet(viewsets.ModelViewSet):
    """
    previously_selected = False
    last_date = OptimAssetsInfo.objects.filter(previously_selected=previously_selected).latest(
        'date_update').date_update
    queryset = OptimAssetsInfo.objects.filter(date_update=last_date).filter(
        previously_selected=previously_selected).exclude(id_asset__isnull=True).order_by('-weight')
    serializer_class = OptimAssetsInfoSerializer"""


class TopOptimAssetsInfoPreviouslySelectedViewSet(viewsets.ModelViewSet):
    """
    previously_selected = True
    last_date = OptimAssetsInfo.objects.filter(previously_selected=previously_selected).latest(
        'date_update').date_update
    queryset = OptimAssetsInfo.objects.filter(date_update=last_date).filter(
        previously_selected=previously_selected).exclude(id_asset__isnull=True).order_by('-weight')
    serializer_class = OptimAssetsInfoSerializer"""


class AssetsCheckLimitsViewSet(viewsets.ModelViewSet):
    """
    queryset = AssetsCheckLimits.objects.exclude(
        Q(up_limit__isnull=True) & Q(down_limit__isnull=True)).order_by('name')
    serializer_class = AssetsLimitCheckerSerializer"""


class AssetsCheckLimitsAssetsNamesViewSet(viewsets.ModelViewSet):
    """
    queryset = AssetsCheckLimits.objects.exclude(name__isnull=True).order_by('name')
    serializer_class = AssetsLimitCheckerSerializer"""


class RecommendedAssetsViewSet(viewsets.ModelViewSet):
    """
    last_date = RecommendedAssetsToBuy.objects.latest('date_date').date_date
    queryset = RecommendedAssetsToBuy.objects.filter(date_date=last_date).order_by('-potential_percent')
    serializer_class = RecommendedAssetsSerializer"""
