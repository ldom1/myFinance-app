from django.shortcuts import render, redirect
from django.contrib import messages
from django.views.generic import View, TemplateView
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.apps import apps
import numpy as np
from datetime import datetime

from funds_CA.models import fundsCA
from .forms import *
from .models import *


@login_required
def view_display_pea(request):

    id_pea = request.GET.get('get_id')

    if id_pea:

	    pea_to_delete = PEA.objects.filter(id_pea=id_pea, user_username=request.user.get_username())
	    for pea in pea_to_delete:
	    	pea.delete()

    pea = PEA.objects.filter(user_username=request.user.get_username())

    if len(pea) == 0:
    	context = {}
    else:
    	context = {'pea': pea}

    return render(request, 'pea/display_pea.html', context)


@login_required
def view_display_one_pea(request, name_pea):

	pea = PEA.objects.filter(name_pea=name_pea, user_username=request.user.get_username())[0]
	pea_history = PEAHistory.objects.filter(name_pea=name_pea, user_username=request.user.get_username())
	orders = Order.objects.filter(name_pea=name_pea, user_username=request.user.get_username())

	nb_orders = len(orders)

	# Var for chart
	risk = np.zeros(8)

	for order in orders:
		try:
			risk[order.risk-1] += 1
		except Exception:
			pass

	context = {'pea': pea,
			   'pea_history': pea_history,
			   'orders': orders,
			   'nb_orders': nb_orders,
			   'risk': risk}

	return render(request, 'pea/display_one_pea.html', context)

class view_register_new_pea(TemplateView):
	# Form to get data
    template_name = 'pea/register_new_pea.html'

    def get(self, request):
    	context = {}

    	form = RegisterPeaForm()
    	# context
    	context['form'] = form
    	return render(request, self.template_name, context)

    def post(self, request):
    	context = {}
    	form = RegisterPeaForm(request.POST)

    	if form.is_valid():

    		name_pea = form.cleaned_data['name_pea']
    		description = form.cleaned_data['description']
    		currency = form.cleaned_data['currency']

    		# Get the pea
    		pea = PEA.objects.filter(user_username=request.user.get_username())

    		try:
    			id_pea = np.int(np.max([y.id_pea for y in pea]) + 1)
    		except Exception:
    			id_pea = 1


    		pea, created = PEA.objects.get_or_create(
				            	date = datetime.today(),
				            	id_pea = id_pea,
				            	name_pea = name_pea,
				            	description = description,
				            	current_value = 0,
				            	currency = currency,
				            	risk = 0,
    							user_username = request.user.get_username())
    	# context
    	context['form'] = form
    	return render(request, self.template_name, context)


class view_register_new_order_funds(TemplateView):
	# Form to get data
    template_name = 'pea/register_new_order_funds.html'

    def get(self, request):
    	context = {}

    	form = RegisterOrderFundsForm()

    	# context
    	context['form'] = form

    	return render(request, self.template_name, context)

    def post(self, request):
    	context = {}

    	form = RegisterOrderFundsForm(request.POST)

    	if form.is_valid():
    		type_asset = form.cleaned_data['type_asset']
	    	name = form.cleaned_data['name']
	    	initial_amount = form.cleaned_data['initial_amount']
	    	currency = form.cleaned_data['currency']
	    	name_pea = form.cleaned_data['name_pea']

	    	# Get the pea
	    	pea = PEA.objects.filter(name_pea=name_pea, user_username=request.user.get_username())
	    	order = Order.objects.filter(user_username=request.user.get_username())
	    	id_pea = pea[0].id_pea

	    	try:
	    		id_order = np.int(np.max([y.id_order for y in order]) + 1)
	    	except Exception:
	    		id_order = 1

	    	fundsCA = apps.get_model('funds_CA', 'fundsCA')
    		funds = fundsCA.objects.all()

	    	risk = funds.filter(name=name)[0].risk_level
	    	id_asset = funds.filter(name=name)[0].id_fund

	    	order, created = Order.objects.get_or_create(
				            	buying_date = datetime.today(),
				            	type_asset=type_asset,
				            	name_asset=name,
				            	id_pea = id_pea,
				            	id_order = id_order,
				            	name_pea = name_pea,
				            	id_asset = id_asset,
				            	initial_amount = initial_amount,
				            	current_value = initial_amount,
				            	currency = currency,
				            	live=1,
				            	risk=risk,
				            	user_username = request.user.get_username())

    	# context
    	context['form'] = form

    	return render(request, self.template_name, context)


class view_register_new_order_asset(TemplateView):
	# Form to get data
    template_name = 'pea/register_new_order_asset.html'

    def get(self, request):
    	context = {}

    	form = RegisterOrderAssetForm()

    	# context
    	context['form'] = form
    	return render(request, self.template_name, context)

    def post(self, request):
    	context = {}

    	form = RegisterOrderAssetForm(request.POST)

    	if form.is_valid():
    		type_asset = form.cleaned_data['type_asset']
	    	name = form.cleaned_data['name']
	    	initial_amount = form.cleaned_data['initial_amount']
	    	currency = form.cleaned_data['currency']
	    	name_pea = form.cleaned_data['name_pea']

	    	# Get the pea
	    	pea = PEA.objects.filter(name_pea=name_pea, user_username=request.user.get_username())
	    	order = Order.objects.filter(user_username=request.user.get_username())
	    	id_pea = pea[0].id_pea

	    	try:
	    		id_order = np.int(np.max([y.id_order for y in order]) + 1)
	    	except Exception:
	    		id_order = 1

	    	assets = apps.get_model('assets', 'Assets')
    		asset = assets.objects.all()

	    	id_asset = asset.filter(name=name)[0].id_asset

	    	order, created = Order.objects.get_or_create(
				            	buying_date = datetime.today(),
				            	type_asset=type_asset,
				            	name_asset=name,
				            	id_pea = id_pea,
				            	id_order = id_order,
				            	name_pea = name_pea,
				            	id_asset = id_asset,
				            	initial_amount = initial_amount,
				            	current_value = initial_amount,
				            	currency = currency,
				            	live=1,
				            	risk=8,
				            	user_username = request.user.get_username())

    	# context
    	context['form'] = form

    	return render(request, self.template_name, context)
