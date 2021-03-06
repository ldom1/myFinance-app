from django.core.management.base import BaseCommand
import os
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class Command(BaseCommand):
    help = 'Run all commands'
    commands = [
        'python3 manage.py generateAssetsBDD',
        'python3 manage.py getAssetsInfos',
        'python3 manage.py getOptimalAssets',
        'python3 manage.py getAndCheckAssetsLimits',
        'python3 manage.py getRecommendedAssets'
    ]

    def handle(self, *args, **options):
        for command in self.commands:
            logger.info(f'Run all: run command: {command}')
            os.system(command)
