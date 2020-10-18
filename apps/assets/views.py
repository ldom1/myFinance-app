from rest_framework import viewsets

from .serializers import AssetsInfoSerializer
from .models import AssetsInfo


class AssetsInfoViewSet(viewsets.ModelViewSet):
    queryset = AssetsInfo.objects.all().order_by('-dividende', 'value')
    serializer_class = AssetsInfoSerializer


class Top5AssetsInfoViewSet(viewsets.ModelViewSet):
    queryset = AssetsInfo.objects.all().exclude(name__isnull=True).order_by('-dividende', 'value')[:5]
    serializer_class = AssetsInfoSerializer
