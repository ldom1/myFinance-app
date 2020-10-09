from rest_framework import viewsets

from .serializers import AssetsInfoSerializer
from .models import AssetsInfo


class AssetsInfoViewSet(viewsets.ModelViewSet):
    queryset = AssetsInfo.objects.all().order_by('-dividende', 'value')
    serializer_class = AssetsInfoSerializer
