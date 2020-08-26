from django import forms
from django.apps import apps
import numpy as np

class RegisterOrderFundsForm(forms.Form):

	PEA = apps.get_model('pea', 'PEA')
	fundsCA = apps.get_model('funds_ca', 'fundsCA')

	pea = PEA.objects.all()
	funds = fundsCA.objects.all()

	unique_pea = np.unique([y.name_pea for y in pea])
	unique_funds = np.unique([y.name for y in funds])

	choices_curr = [[1, 'Choose...']] + [['EUR', 'EUR']] + [['USD', 'USD']]
	choices_pea = [[1, 'Choose...']] + [[y, y] for y in unique_pea]
	choices_asset = [[1, 'Choose...']] + [[y, y] for y in unique_funds]
	choices_type_asset = [[1, 'Choose...']] + [['fond', 'fond']] + [['action', 'action']]

	name = forms.ChoiceField(choices=choices_asset, required=True)
	type_asset = forms.ChoiceField(choices=choices_type_asset, required=True)
	initial_amount = forms.IntegerField(required=True)
	name_pea = forms.ChoiceField(choices=choices_pea, required=True)
	currency = forms.ChoiceField(choices=choices_curr, required=True)


class RegisterOrderAssetForm(forms.Form):

	PEA = apps.get_model('pea', 'PEA')
	assets = apps.get_model('assets', 'Assets')

	pea = PEA.objects.all()
	asset = assets.objects.all()

	unique_pea = np.unique([y.name_pea for y in pea])
	unique_asset = np.unique([y.name for y in asset])

	choices_curr = [[1, 'Choose...']] + [['EUR', 'EUR']] + [['USD', 'USD']]
	choices_pea = [[1, 'Choose...']] + [[y, y] for y in unique_pea]
	choices_asset = [[1, 'Choose...']] + [[y, y] for y in unique_asset]
	choices_type_asset = [[1, 'Choose...']] + [['fond', 'fond']] + [['action', 'action']]

	name = forms.ChoiceField(choices=choices_asset, required=True)
	type_asset = forms.ChoiceField(choices=choices_type_asset, required=True)
	initial_amount = forms.IntegerField(required=True)
	name_pea = forms.ChoiceField(choices=choices_pea, required=True)
	currency = forms.ChoiceField(choices=choices_curr, required=True)


class RegisterPeaForm(forms.Form):

	choices_curr = [[1, 'Choose...']] + [['EUR', 'EUR']] + [['USD', 'USD']]

	currency = forms.ChoiceField(choices=choices_curr, required=True)
	name_pea = forms.CharField(required=True)
	description = forms.CharField(required=True)
