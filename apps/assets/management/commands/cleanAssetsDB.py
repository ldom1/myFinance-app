from django.core.management.base import BaseCommand, CommandError

# import
from assets.models import AssetsInfo, OptimAssetsInfo, AssetsCheckLimits
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class Command(BaseCommand):
    help = 'Closes the specified poll for voting'

    def handle(self, *args, **options):

        logger.info(f'Clean asset DB: Clean assets infos ...')
        for asset in AssetsInfo.objects.all():
            asset.delete()

        logger.info(f'Clean asset DB: Clean optimal assets ...')
        for asset in OptimAssetsInfo.objects.all():
            asset.delete()

        logger.info(f'Clean asset DB: Clean assets check list ...')
        for asset in AssetsCheckLimits.objects.all():
            asset.delete()
