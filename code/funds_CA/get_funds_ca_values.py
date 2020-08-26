#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 24 22:18:45 2019

@author: louisgiron
"""
from tqdm import tqdm
import datetime
import logging

from code.config.global_variables import URLS_FUNDS_CA
from code.config.utils import get_code

logging.basicConfig(level=logging.INFO)


def extract_html_code_from_one_page(html_code):
    logging.info('Funds CA - Scrap one page: extract all html code from page')
    return html_code('div', 'c-faceplate__company')


def extract_name_of_fund_from_one_page(html_code_extracted):
    logging.info('Funds CA - Scrap one page: extract name from code')
    return html_code_extracted[0].a.get_text().strip()


def extract_value_of_fund_from_one_page(html_code_extracted):
    logging.info('Funds CA - Scrap one page: extract value from code')
    value = html_code_extracted[0]('span', 'c-instrument c-instrument--last')[0].get_text().strip().replace(' ', '')
    try:
        value = float(value)
    except Exception as e:
        logging.info(f'Funds CA - Scrap one page: extract name from code - Error: {e}')
        value = value
    return value


def extract_currency_of_fund_from_one_page(html_code_extracted):
    logging.info('Funds CA - Scrap one page: extract currency from code')
    return html_code_extracted[0]('span', 'c-faceplate__price-currency')[0].get_text().strip()


def extract_variation_of_fund_from_one_page(html_code_extracted):
    logging.info('Funds CA - Scrap one page: extract variation from code')
    variation = html_code_extracted[0]('span', 'c-instrument c-instrument--variation')[0].get_text().strip().replace(
        ' ', '')
    variation = variation.replace('%', '')
    try:
        if '+' in variation:
            variation = float(variation.replace('+', '')) / 100
        elif '-' in variation:
            variation = float(variation.replace('-', '')) / 100 * -1
        else:
            variation = 0.
    except Exception as e:
        logging.info(f'Funds CA - Scrap one page: extract variation from code - Error: {e}')
        variation = variation
    return variation


def extract_name_id_of_fund_from_one_page(html_code_extracted):
    logging.info('Funds CA - Scrap one page: extract name id of fund from code')
    return html_code_extracted[0]('h2', 'c-faceplate__isin')[0].get_text().strip()


def extract_id_of_fund_from_one_page(name_id):
    logging.info('Funds CA - Scrap one page: extract id of fund from code')
    try:
        id_fund = name_id.split('-')[0].strip()
    except Exception as e:
        print(e)
        id_fund = name_id
    return id_fund


def extract_date_of_fund_from_one_page(html_code_extracted):
    logging.info('Funds CA - Scrap one page: extract date from code')
    date_ = html_code_extracted[0]('div', 'c-faceplate__real-time')[0].get_text().strip()

    try:
        date = date_.split()[-1]
        date = datetime.datetime.strptime(date, '%d/%m/%Y')
    except Exception as e:
        logging.info(f'Funds CA - Scrap one page: extract date from code - Error: {e}')
        date = None
    return date


def extract_risk_of_fund_from_one_page(html_code):
    logging.info('Funds CA - Scrap one page: extract risk from code')

    try:
        risk_ = \
            html_code('div',
                      'c-faceplate__quotation c-faceplate__quotation--new-line c-faceplate__quotation--margin-top')[0]

        risk = int(risk_('div', 'c-gauge')[0]['data-gauge-current-step'])
    except Exception as e:
        logging.info(f'Funds CA - Scrap one page: extract date from code - Error: {e}')
        risk = None
    return risk


def extract_net_asset_of_fund_from_one_page(html_code):
    logging.info('Funds CA - Scrap one page: extract net asset from code')
    net_asset_ = html_code('div', 'c-faceplate__quotation')[0]('ul')[0]('li')[-1].get_text().strip()
    net_asset_ = net_asset_.split('\n')[-1].strip().split('/')[-1].strip().replace(' ', '')

    try:
        net_asset = float(net_asset_)
    except Exception as e:
        logging.info(f'Funds CA - Scrap one page: extract net asset from code - Error: {e}')
        net_asset = None
    return net_asset


def extract_all_values_of_fund_from_one_page(html_code):
    html_code_extracted = extract_html_code_from_one_page(html_code)
    name = extract_name_of_fund_from_one_page(html_code_extracted)
    value = extract_value_of_fund_from_one_page(html_code_extracted)
    currency = extract_currency_of_fund_from_one_page(html_code_extracted)
    variation = extract_variation_of_fund_from_one_page(html_code_extracted)
    name_id = extract_name_id_of_fund_from_one_page(html_code_extracted)
    id_fund = extract_id_of_fund_from_one_page(name_id)
    date = extract_date_of_fund_from_one_page(html_code_extracted)
    risk = extract_risk_of_fund_from_one_page(html_code)
    net_asset = extract_net_asset_of_fund_from_one_page(html_code)

    dict_values = {'name': name, 'value': value, 'currency': currency, 'variation': variation, 'name_id': name_id,
                   'id_fund': id_fund, 'date': date, 'risk': risk, 'net_asset': net_asset}
    return dict_values


def ingest_data_in_db(model_db, dict_values, url=None):
    logging.info('Funds CA - Scrap one page: ingest values in db')
    today = datetime.datetime.today()
    model_db.objects.get_or_create(
        date=datetime.date(today.year, today.month, today.day),
        date_dernier_cours=dict_values['date'],
        id_fund=str(dict_values['id_fund']),
        url=url,
        name=dict_values['name'],
        name_id=dict_values['name_id'],
        value=dict_values['value'],
        variation=dict_values['variation'],
        risk_level=dict_values['risk'],
        net_asset=dict_values['net_asset'], )


def get_all_funds_ca_data_and_ingest_in_db(model_db):
    logging.info('Funds CA - Scrap all pages and get data')
    for url in tqdm(URLS_FUNDS_CA):
        logging.info(f'Funds CA - Scrap one page: {url}')
        html_code = get_code(url)
        dict_values = extract_all_values_of_fund_from_one_page(html_code)
        ingest_data_in_db(model_db=model_db, dict_values=dict_values, url=url)


def get_all_funds_ca_data_for_testing():
    url = URLS_FUNDS_CA[0]
    html_code = get_code(url)
    dict_values = extract_all_values_of_fund_from_one_page(html_code)
    return dict_values
