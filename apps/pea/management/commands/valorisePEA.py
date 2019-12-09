#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec  8 20:26:21 2019

@author: louisgiron
"""
from django.core.management.base import BaseCommand, CommandError

import numpy as np

# import
from pea.models import *
from funds_CA.models import *

import pandas as pd
from datetime import datetime, date, timedelta

class Command(BaseCommand):
    help = 'Closes the specified poll for voting'

    def handle(self, *args, **options):

        # correct
        all_pea = PEA.objects.all()
        all_orders = Order.objects.all()

        for pea in all_pea:
        	try:
        		print(pea.name_pea)
        		id_pea = pea.id_pea
        		pea_orders = all_orders.filter(id_pea=id_pea)

        		# all infos
        		try:
        			current_value = np.sum([y.current_value for y in pea_orders])
        			pea.current_value = current_value
        		except Exception as e:
        			print(e)
        			pea.current_value = 0.

        		try:
        			initial_amount = np.sum([y.initial_amount for y in pea_orders])
        			pea.initial_amount = initial_amount
        		except Exception as e:
        			print(e)
        			pea.initial_amount = 0.
        		try:
        			current_value = np.sum([y.current_value for y in pea_orders])
        			initial_amount = np.sum([y.initial_amount for y in pea_orders])
        			pea.global_variation = (current_value - initial_amount)/initial_amount*100
        		except Exception as e:
        			print(e)
        			pea.global_variation = 0.
        		try:
        			pea.risk = np.mean([y.risk for y in pea_orders])
        		except Exception as e:
        			print(e)
        			pea.risk = 0
        		# Update date
        		pea.update_date = datetime.today()
        		pea.save()
        	except Exception as e:
        		print(e)
        		pass

	