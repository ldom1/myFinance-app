from django import forms
from django.apps import apps
import numpy as np

class RegisterOrderForm(forms.Form):

	'''PEA = apps.get_model('pea', 'PEA')
	fundsCA = apps.get_model('funds_CA', 'fundsCA')

	pea = PEA.objects.all()
	funds = fundsCA.objects.all()

	unique_pea = np.unique([y.name_pea for y in pea])
	unique_funds = np.unique([y.id_fund for y in funds])

	choices_curr = [[1, 'Choose...']] + [['EUR', 'EUR']] + [['USD', 'USD']]
	choices_pea = [[1, 'Choose...']] + [[y, y] for y in unique_pea]
	choices_asset = [[1, 'Choose...']] + [[y, y] for y in unique_funds]

	id_asset = forms.ChoiceField(choices=choices_asset, required=True)
	initial_amount = forms.IntegerField(required=True)
	name_pea = forms.ChoiceField(choices=choices_pea, required=True)
	currency = forms.ChoiceField(choices=choices_curr, required=True)'''

class RegisterPeaForm(forms.Form):

	'''choices_curr = [[1, 'Choose...']] + [['EUR', 'EUR']] + [['USD', 'USD']]

	currency = forms.ChoiceField(choices=choices_curr, required=True)
	name_pea = forms.CharField(required=True)
	description = forms.CharField(required=True)'''
