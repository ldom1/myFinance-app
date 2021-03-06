from django.core.management.base import BaseCommand
import os
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class Command(BaseCommand):
    help = 'Run all commands'
    commands = [
        'python3 manage.py cleanAssetsInfoDB',
        'python3 manage.py cleanAssetsLimitsDB',
        'python3 manage.py cleanOptimAssetsInfoDB',
    ]

    def handle(self, *args, **options):
        for command in self.commands:
            logger.info(f'Run all: run command: {command}')
            os.system(command)
