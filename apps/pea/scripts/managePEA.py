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

		pea.current_value = np.sum([y.current_value for y in pea_orders])
		pea.save()


def risk_pea():

	all_pea = PEA.objects.all()
	all_orders = Order.objects.all()
	all_funds = Order.objects.all()

	for pea in all_pea:

		id_pea = pea.id_pea
		pea_orders = all_orders.filter(id_pea=id_pea)

		risk_ = []

		for order in pea_orders:
			id_asset = order.id_asset
			risk_.append(fundsCA.objects.filter(id_fund=id_asset, date=date.today())[0].risk_level)

		try:
			pea.risk = np.mean(risk_)
			pea.save()
		except Exception:
			pea.risk = 0
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

