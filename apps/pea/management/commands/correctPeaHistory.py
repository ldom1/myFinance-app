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
        fundsca = pd.DataFrame(fundsCA.objects.all().values())
        order_all = pd.DataFrame(Order.objects.all().values())

        pea_history_to_delete = PEAHistory.objects.all()
        for elt in pea_history_to_delete:
            elt.delete()

        # pea test
        pea_list = pea_history.name_pea.unique()

        for name in pea_list:
            id_pea = pea_history[pea_history.name_pea == name].id_pea.iloc[0]
            user = pea_history[pea_history.name_pea == name].user_username.iloc[0]

            try:
                order = order_all[order_all.name_pea == name]
                asset = order.id_asset.iloc[0]
            
                # date
                initial_amount = order.initial_amount.iloc[0]
            except Exception:
                initial_amount = 0
                asset = 'FR0011649029'

            history_asset = fundsca[fundsca.id_fund == asset].sort_values(by='date')
            
            for i in range(history_asset.shape[0]):
            
                if i == 0:
                    value = initial_amount
                else:
                    funds_amnt = history_asset.iloc[i].value
                    funds_amnt_bef = history_asset.iloc[i-1].value
            
                    var = (funds_amnt - funds_amnt_bef)/funds_amnt_bef
                    amount = value*var + value
            
                    value = amount

                pea_history_new, created = PEAHistory.objects.get_or_create(
                                        date=history_asset.iloc[i].date,
                                        id_pea=id_pea,
                                        name_pea=name,
                                        value=value,
                                        currency='EUR',
                                        risk=history_asset.iloc[i].risk_level,
                                        user_username=user,)
