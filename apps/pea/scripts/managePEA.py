#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 24 22:18:45 2019

@author: louisgiron
"""
import numpy as np
from datetime import datetime, date, timedelta
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

		yesterday_fund_value = funds.filter(date=date.today() + timedelta(days=-1))[0].value
		current_fund_value = funds.filter(date=date.today())[0].value
		
		variation = (current_fund_value - yesterday_fund_value)/yesterday_fund_value

		order.current_value = variation*ord_initial_amount + ord_initial_amount
		order.save()

def valorise_pea():

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


def generateHistory():

	all_pea = PEA.objects.all()

	for pea in all_pea:

		created = None
		pea_history, created = PEAHistory.objects.get_or_create(
                                date=date.today(),
                                id_pea=pea.id_pea,
                                name_pea=pea.name_pea,
                                value=pea.current_value,
                                currency=pea.currency,
                                risk=pea.risk,
                                global_variation=pea.global_variation,
                                interday_variation=pea.interday_variation,
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
			pea.interday_variation = None
			pea.save()




