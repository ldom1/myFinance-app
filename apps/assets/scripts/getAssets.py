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
from datetime import datetime, date

from assets.models import Assets


def get_code(url):
        """Return the code html"""
        # Define the user agent
        headers = {'User-Agent': generate_user_agent(device_type="desktop",
                                                     os=('mac', 'linux'))}
        # Open the url file and get the html code of the page
        req = requests.Session()
        req = requests.get(url, headers=headers)
        return soup(req.text, "lxml")


def getAssetData():
    # get all urls
    nb_page = 15
    urls_page = ['https://www.boursorama.com/bourse/actions/cotations/page-{0}?quotation_az_filter%5Bmarket%5D=SRD&quotation_az_filter%5Bletter%5D=&quotation_az_filter%5BpeaEligibility%5D=1&quotation_az_filter%5Bfilter%5D=&pagination_1447025609='.format(i) for i in range(1, nb_page+1)]

    urls = []

    for page in tqdm(urls_page):

        # Infos
        all_code = get_code(page)

        all_infos = all_code('tbody', 'c-table__body')[0]('div', 'o-pack__item u-ellipsis u-color-cerulean')

        for elt in all_infos:

            urls.append('https://www.boursorama.com' + elt.a['href'])


    # actions
    urls = set(urls)

    res = []

    for url in tqdm(urls):
        # Infos
        all_code = get_code(url)

        funds_info = all_code('div', 'c-faceplate__body')

        # Name
        name = funds_info[0].a.get_text().strip().lower()

        # Value
        value = funds_info[0]('span', 'c-instrument c-instrument--last')[0].get_text().strip()
        try:
            value = float(value.replace(' ', ''))
        except Exception:
            value = None

        # Currenc
        currency = funds_info[0]('span', 'c-faceplate__price-currency')[0].get_text().strip()

        variation = funds_info[0]('span', 'c-instrument c-instrument--variation')[0].get_text().strip()

        variation = variation.replace('%', '')

        if '+' in variation:
            variation = float(variation.replace('+', ''))/100
        elif '-' in variation:
            variation = float(variation.replace('-', ''))/100*-1
        else:
            variation = 0.
        
        name_id = funds_info[0]('h2', 'c-faceplate__isin')[0].get_text().strip()

        id_asset = name_id.split('-')[0].split()[0].strip()

        ouverture = funds_info[0]('span', 'c-instrument c-instrument--open')[0].get_text().strip()
        try:
            ouverture = float(ouverture)
        except Exception:
            ouverture = None

        cloture_veille = funds_info[0]('span', 'c-instrument c-instrument--previousclose')[0].get_text().strip()
        try:
            cloture_veille = float(cloture_veille)
        except Exception:
            cloture_veille = None

        haut = funds_info[0]('span', 'c-instrument c-instrument--high')[0].get_text().strip()
        try:
            haut = float(haut)
        except Exception:
            haut = None

        bas = funds_info[0]('span', 'c-instrument c-instrument--low')[0].get_text().strip()
        try:
            bas = float(bas)
        except Exception:
            bas = None

        volume = funds_info[0]('span', 'c-instrument c-instrument--totalvolume')[0].get_text().replace(' ', '').strip()
        try:
            volume = float(volume.replace(' ', ''))
        except Exception:
            volume = None

        try:
            dividende = funds_info[0]('p', 'c-list-info__value u-color-big-stone')[14].get_text().strip()
            dividende = float(dividende.split()[0])
            date_dividende = funds_info[0]('p', 'c-list-info__value u-color-big-stone')[15].get_text().strip()
        except Exception:
            try:
                dividende = 0
                date_dividende = funds_info[0]('p', 'c-list-info__value u-color-big-stone')[14].get_text().strip()
            except Exception:
                dividende = 0
                date_dividende = None

        

        # Feed the database
        created = None
        today = datetime.today()
        asset, created = Assets.objects.get_or_create(
                                date=date(today.year, today.month, today.day),
                                id_asset=id_asset,
                                url=url,
                                name=name,
                                value=value,
                                variation=variation,
                                ouverture=ouverture,
                                cloture_veille=cloture_veille,
                                haut=haut,
                                bas=bas,
                                volume=volume,
                                dividende=dividende,
                                date_dividende=date_dividende,)
