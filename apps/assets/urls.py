from django.urls import include, path
from rest_framework import routers
from .views import *

router = routers.DefaultRouter()

router.register(r'assets_info', AssetsInfoViewSet)

"""
router.register(r'optimal_assets_info', TopOptimAssetsInfoViewSet)
router.register(r'optimal_assets_info_previously_selected', TopOptimAssetsInfoPreviouslySelectedViewSet)
router.register(r'assets_check_limit', AssetsCheckLimitsViewSet)
router.register(r'assets_check_limit_names', AssetsCheckLimitsAssetsNamesViewSet)
router.register(r'recommended_assets', RecommendedAssetsViewSet)"""

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
