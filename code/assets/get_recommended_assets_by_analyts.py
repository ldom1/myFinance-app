#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 24 22:18:45 2020

@author: louisgiron
"""
from tqdm import tqdm
import datetime
import logging

from assets.models import RecommendedAssetsToBuy
from code.config.utils import get_code
from code.config.global_variables import URLS_RECOMMENDED_ASSETS

logging.basicConfig(level=logging.INFO)


def extract_html_code_from_one_page(html_code):
    logging.info('Assets - Scrap one page: extract all html code from page')
    html_code_extracted = html_code('tbody')[0]
    return html_code_extracted


def clean_text(text):
    new_text = text.replace(u'\n', '')
    new_text = new_text.replace('EUR', '')
    new_text = new_text.replace('+', '')
    new_text = new_text.replace('-', '')
    new_text = new_text.split('(')[0]
    new_text = new_text.strip()
    return new_text


def convert_text_to_float(text):
    text_cleaned = clean_text(text)
    try:
        if text_cleaned != '':
            return float(text_cleaned)
        else:
            return None
    except Exception as e:
        logging.info(f'Recommended assets - Scrap one page: convert text to float: {e}')
        if '%' in text_cleaned:
            text_cleaned = text_cleaned.replace('%', '')
            return float(text_cleaned) / 100
        elif text_cleaned == 'Atteint':
            return float(100)
        else:
            return clean_text(text)


def convert_text_to_int(text):
    try:
        return int(clean_text(text))
    except Exception as e:
        logging.info(f'Recommended assets - Scrap one page: convert text to int: {e}')
        return clean_text(text)


def get_info_from_table_row(extracted_table_row):
    name = extracted_table_row.a.get_text()
    url = 'https://www.boursorama.com' + extracted_table_row.a['href']
    values_row = extracted_table_row('td')
    action = values_row[1].get_text()
    value = convert_text_to_float(values_row[2].get_text())
    value_objective = convert_text_to_float(values_row[3].get_text())
    potential_percent = convert_text_to_float(values_row[4].get_text())
    nb_analysts = convert_text_to_int(values_row[5].get_text())
    net_benefit_in_eur = convert_text_to_float(values_row[6].get_text())
    rentability_n_percent = convert_text_to_float(values_row[7].get_text())
    price_earning_ratio_n = convert_text_to_float(values_row[8].get_text())
    price_earning_ratio_n_plus_1 = convert_text_to_float(values_row[9].get_text())

    id_asset = get_id_asset_info(url=url)

    return (id_asset, name, url, action, value, value_objective, potential_percent, nb_analysts, net_benefit_in_eur,
            rentability_n_percent, price_earning_ratio_n, price_earning_ratio_n_plus_1)


def get_id_asset_info(url):
    html_code = get_code(url)
    id_asset_div = html_code('div', 'c-faceplate__body')
    try:
        return id_asset_div[0]('h2', 'c-faceplate__isin')[0].get_text().strip().split()[0]
    except Exception as e:
        logging.info(f'Recommended assets - Scrap one page: convert text to int: {e}')


def insert_table_row_in_db(extracted_table_row):
    (id_asset, name, url, action, value, value_objective, potential_percent, nb_analysts, net_benefit_in_eur,
     rentability_n_percent, price_earning_ratio_n, price_earning_ratio_n_plus_1) = get_info_from_table_row(
        extracted_table_row)

    response = RecommendedAssetsToBuy.objects.update_or_create(
        id_asset=id_asset,
        date_date=datetime.date.today(),
        defaults={'date': datetime.datetime.today(),
                  'name': name,
                  'url': url,
                  'action': action,
                  'value': value,
                  'value_objective': value_objective,
                  'potential_percent': potential_percent,
                  'nb_analysts': nb_analysts,
                  'net_benefit_in_eur': net_benefit_in_eur,
                  'rentability_n_percent': rentability_n_percent,
                  'price_earning_ratio_n': price_earning_ratio_n,
                  'price_earning_ratio_n_plus_1': price_earning_ratio_n_plus_1
                  }
    )
    logging.info(f'Recommended assets - ingested {name} in db: {response}')


def insert_table_in_db(table):
    for row in table:
        insert_table_row_in_db(extracted_table_row=row)


def get_code_and_insert_in_db():
    for url in tqdm(URLS_RECOMMENDED_ASSETS):
        html_code = get_code(url=url)
        table = html_code('tbody')[0]
        insert_table_in_db(table=table)
