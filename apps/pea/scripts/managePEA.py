#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 24 22:18:45 2019

@author: louisgiron
"""
import numpy as np
from datetime import datetime, date
import time

from funds_CA.models import fundsCA
from pea.models import PEA, Order, PEAHistory


def valorise_order():

	all_orders = Order.objects.filter(live=1)


	for order in all_orders:

		ord_id_asset = order.id_asset
		ord_buying_date = date(order.buying_date.year, order.buying_date.month, order.buying_date.day)
		ord_initial_amount = order.initial_amount

		funds = fundsCA.objects.filter(id_fund=ord_id_asset)

		initial_fund_value = funds.filter(date=ord_buying_date)[0].value
		current_fund_value = funds.filter(date=date.today())[0].value
		
		variation = (current_fund_value - initial_fund_value)/initial_fund_value

		order.current_value = variation*ord_initial_amount + ord_initial_amount
		order.save()

def valorise_pea():

	all_pea = PEA.objects.all()
	all_orders = Order.objects.all()

	for pea in all_pea:

		id_pea = pea.id_pea
		pea_orders = all_orders.filter(id_pea=id_pea)

		current_value = np.sum([y.current_value for y in pea_orders])
		initial_amount = np.sum([y.initial_amount for y in pea_orders])

		pea.current_value = current_value
		pea.initial_amount = initial_amount
		pea.global_variation = (current_value - initial_amount)/initial_amount*100

		# Update date
		pea.update_date = datetime.today()
		pea.save()


def risk_pea():

	all_pea = PEA.objects.all()
	all_orders = Order.objects.all()

	for pea in all_pea:

		id_pea = pea.id_pea
		pea_orders = all_orders.filter(id_pea=id_pea)

		try:
			pea.current_value = np.mean([y.risk for y in pea_orders])
		except Exception:
			pea.current_value = 0

		# Update date
		pea.update_date = datetime.today()
		pea.save()

def generateHistory():

	all_pea = PEA.objects.all()

	for pea in all_pea:

		created = None
		fund, created = PEAHistory.objects.get_or_create(
                                date=date.today(),
                                id_pea=pea.id_pea,
                                name_pea=pea.name_pea,
                                value=pea.current_value,
                                currency=pea.currency,
                                risk=pea.risk,
                                user_username=pea.user_username)


def variationInterdayPeaValue():

	all_hist_pea = PEAHistory.objects.all().order_by('date')
	all_pea = PEA.objects.all()

	for pea in all_pea:

		pea_hist = all_hist_pea.filter(name_pea=pea.name_pea)

		try:
			value_list = [y.value for y in pea_hist]
			yesterday_value = value_list[-2]
			today_value = value_list[-1]

			variation = (today_value-yesterday_value)/yesterday_value*100

			# Feed pea database
			pea.interday_variation = variation
			pea.save()

		except Exception as e:
			print(e)
			pea.variation = None
			pea.save()
		




