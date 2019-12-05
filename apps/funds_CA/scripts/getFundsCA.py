#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 24 22:18:45 2019

@author: louisgiron
"""
from bs4 import BeautifulSoup as soup
import requests
import re
from user_agent import generate_user_agent
import pandas as pd
import numpy as np
from tqdm import tqdm
from funds_CA.models import fundsCA
import datetime
import time


def get_code(url):
        """Return the code html"""
        # Define the user agent
        headers = {'User-Agent': generate_user_agent(device_type="desktop",
                                                     os=('mac', 'linux'))}
        # Open the url file and get the html code of the page
        req = requests.Session()
        req = requests.get(url, headers=headers)
        return soup(req.text, "lxml")


def getFundsData():
    # First fonds
    urls = ['https://www.boursorama.com/bourse/opcvm/cours/0P00016DRV/',
            'https://www.boursorama.com/bourse/opcvm/cours/0P0001AMLS/',
            'https://www.boursorama.com/bourse/opcvm/cours/0P00016LLM/',
            'https://www.boursorama.com/bourse/opcvm/cours/0P00016P31/',
            'https://www.boursorama.com/bourse/opcvm/cours/MP-828959/',
            'https://www.boursorama.com/bourse/opcvm/cours/MP-828841/',
            'https://www.boursorama.com/bourse/opcvm/cours/0P00011IWP/',
            'https://www.boursorama.com/bourse/opcvm/cours/MP-356460/',
            'https://www.boursorama.com/bourse/opcvm/cours/0P0000TIK4/',
            'https://www.boursorama.com/bourse/opcvm/cours/0P0001HV65/',
            'https://www.boursorama.com/bourse/opcvm/cours/0P0000XWUI/',
            'https://www.boursorama.com/bourse/opcvm/cours/MP-442076/',
            'https://www.boursorama.com/bourse/opcvm/cours/0P0001CC08/',
            'https://www.boursorama.com/bourse/opcvm/cours/MP-984095/',
            'https://www.boursorama.com/bourse/opcvm/cours/0P0000YNF8/',
            'https://www.boursorama.com/bourse/opcvm/cours/MP-809773/',
            'https://www.boursorama.com/bourse/opcvm/cours/MP-806992/',
            'https://www.boursorama.com/bourse/opcvm/cours/MP-546993/',
            'https://www.boursorama.com/bourse/opcvm/cours/0P0001DH3M/',
            'https://www.boursorama.com/bourse/opcvm/cours/0P0001DWME/',
            'https://www.boursorama.com/bourse/opcvm/cours/0P0001EOO3/',
            'https://www.boursorama.com/bourse/opcvm/cours/0P0001H3VS/',
            'https://www.boursorama.com/bourse/opcvm/cours/0P0001HET2/',
            'https://www.boursorama.com/bourse/opcvm/cours/MP-828192/',
            'https://www.boursorama.com/bourse/opcvm/cours/0P0000W8CR/',
            'https://www.boursorama.com/bourse/opcvm/cours/0P00016DVT/',
            'https://www.boursorama.com/bourse/opcvm/cours/0P0001DH3L/',
            'https://www.boursorama.com/bourse/opcvm/cours/0P0001DWMF/',
            'https://www.boursorama.com/bourse/opcvm/cours/0P0001EONQ/',
            'https://www.boursorama.com/bourse/opcvm/cours/0P0001FFVK/',
            'https://www.boursorama.com/bourse/opcvm/cours/0P0001HETC/',
            'https://www.boursorama.com/bourse/opcvm/cours/0P00011RIT/' ]

    urls = set(urls)

    i = 1

    res = []

    for url in tqdm(urls):
        # Infos
        all_code = get_code(url)

        funds_info = all_code('div', 'c-faceplate__company')

        # Name
        name = funds_info[0].a.get_text().strip()

        # Value
        value = funds_info[0]('span', 'c-instrument c-instrument--last')[0].get_text().strip().replace(' ', '')
        try:
            value = float(value)
        except Exception as e:
            print(e)
            value = value

        # Currency
        currency = funds_info[0]('span', 'c-faceplate__price-currency')[0].get_text().strip()

        # Variation
        variation = funds_info[0]('span', 'c-instrument c-instrument--variation')[0].get_text().strip().replace(' ', '')
        variation = variation.replace('%', '')

        try:
            if '+' in variation:
                variation = float(variation.replace('+', ''))/100
            elif '-' in variation:
                variation = float(variation.replace('-', ''))/100*-1
            else:
                variation = 0.
        except Exception as e:
            print(e)
            variation = variation

        # Name id
        name_id = funds_info[0]('h2', 'c-faceplate__isin')[0].get_text().strip()

        # ID fund
        try:
            id_fund = name_id.split('-')[0].strip()
        except Exception as e:
            print(e)
            id_fund = name_id

        # Date
        date_ = funds_info[0]('div', 'c-faceplate__real-time')[0].get_text().strip()
        
        try:
            date = date_.split()[-1].split('/')
            date = datetime(int(date[2]), int(date[1]), int(date[0]))
        except Exception as e:
            print(e)
            date = None

        # Risk
        risk_ = all_code('div', 'c-faceplate__quotation c-faceplate__quotation--new-line c-faceplate__quotation--margin-top')[0]
        
        try:
            risk = int(risk_('div', 'c-gauge')[0]['data-gauge-current-step'])
        except Exception as e:
            print(e)
            risk = risk

        # Net asset    
        net_asset_ = all_code('div', 'c-faceplate__quotation')[0]('ul')[0]('li')[-1].get_text().strip()
        net_asset_ = net_asset_.split('\n')[-1].strip().split('/')[-1].strip().replace(' ', '')

        try:
            net_asset = float(net_asset_)
        except Exception as e:
            print(e)
            net_asset = None

        # Feed the database
        created = None
        today = datetime.datetime.today()
        fund, created = fundsCA.objects.get_or_create(
                                date=datetime.date(today.year, today.month, today.day),
                                date_dernier_cours=date,
                                id_fund=str(id_fund),
                                url=url,
                                name=name,
                                name_id=name_id,
                                value=value,
                                variation=variation,
                                risk_level=risk,
                                net_asset=net_asset,)
