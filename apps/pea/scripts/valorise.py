#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 24 22:18:45 2019

@author: louisgiron
"""
import pandas as pd
import numpy as np
from datetime import datetime, date
import time

from funds_CA.models import fundsCA
from pea.models import Order


def valorise_order():

	all_orders = Order.objects.filter(live=1)


	for order in all_orders:

		ord_id_asset = order.id_asset
		ord_buying_date = date(order.buying_date.year, order.buying_date.month, order.buying_date.day)
		ord_initial_amount = order.initial_amount

		funds = fundsCA.objects.filter(id_fund=ord_id_asset)



		print(ord_id_asset)

def valorise_pea():

	pass
