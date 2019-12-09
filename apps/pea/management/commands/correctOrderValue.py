#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec  8 20:26:21 2019

@author: louisgiron
"""
from django.core.management.base import BaseCommand, CommandError

# import
from pea.models import *
from funds_CA.models import *

import pandas as pd
from datetime import datetime, date, timedelta

class Command(BaseCommand):
    help = 'Closes the specified poll for voting'

    def handle(self, *args, **options):

        # correct
        pea_history = pd.DataFrame(PEAHistory.objects.all().values())
        pea = pd.DataFrame(PEA.objects.all().values())
        order_all = Order.objects.all()

        # Correct order
        for order in order_all:
            id_pea = order.id_pea
            pea_history = PEAHistory.objects.filter(id_pea=id_pea)
            order.current_value = pea_history[len(pea_history)-1].value
            order.save()
