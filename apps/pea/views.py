from django.shortcuts import render, redirect
from django.contrib import messages
from django.views.generic import View, TemplateView
from django.contrib.auth.decorators import login_required
from django.test.client import RequestFactory
from django.apps import apps
import numpy as np
import datetime

from .forms import *
from .models import *


@login_required
def view_display_pea(request):

    pea = PEA.objects.filter(user_username=request.user.get_username())

    context = {}

    return render(request, 'pea/display_pea.html', context)

class view_register_new_order(TemplateView):
	# Form to get data
    template_name = 'pea/register_new_order.html'

    def get(self, request):
    	context = {}

    	form = fournisseurForm()
    	# context
    	context['form'] = form
    	return render(request, self.template_name, context)

    def post(self, request):
    	context = {}
    	test = False
    	form = fournisseurForm(request.POST)

    	if form.is_valid():

    		name = form.cleaned_data['name']
    		description = form.cleaned_data['description']
    		adress = form.cleaned_data['adress']
    		zip_code = form.cleaned_data['zip_code']
    		siren = form.cleaned_data['siren']

    		# Get the id
    		fournisseurs = Fournisseur.objects.filter(user_username=request.user.get_username())

    		try:
    			id_fournisseur = np.int(np.max([y.id_fournisseur for y in fournisseurs]) + 1)
    		except Exception:
    			id_fournisseur = 1
    		asset, created = Fournisseur.objects.get_or_create(
				            	name = name,
				            	date = datetime.datetime.today(),
				            	id_fournisseur = id_fournisseur,
    							description = description,
    							adress = adress,
    							zip_code = zip_code,
    							siren = siren,
    							user_username = request.user.get_username())
    	# context
    	context['form'] = form
    	context['test'] = test
    	return render(request, self.template_name, context)
