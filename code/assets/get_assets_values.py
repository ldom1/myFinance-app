#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 24 22:18:45 2019

@author: louisgiron
"""
from tqdm import tqdm
import datetime
import logging

from code.config.global_variables import ALL_PAGES
from code.config.utils import get_code

logging.basicConfig(level=logging.INFO)


def get_urls_for_each_asset():
    urls = []

    for page in tqdm(ALL_PAGES):
        all_code = get_code(page)

        all_infos = all_code.findAll('tbody')[1].findAll('tr')
        for elt in all_infos:
            info = elt.findAll('div')[-1]
            logging.info(f'Assets - Get {info.get_text()} url')
            urls.append('https://www.boursorama.com' + info.a['href'])
    print(urls)
    return list(set(urls))


def extract_html_code_from_one_page(html_code):
    logging.info('Assets - Scrap one page: extract all html code from page')
    html_code_extracted = html_code('div', 'c-faceplate__body')
    return html_code_extracted


def extract_name_of_asset_from_one_page(html_code_extracted):
    logging.info('Assets - Scrap one page: extract name from code')
    return html_code_extracted[0].a.get_text().strip()


def extract_value_of_asset_from_one_page(html_code_extracted):
    logging.info('Assets - Scrap one page: extract value from code')
    value = html_code_extracted[0]('span', 'c-instrument c-instrument--last')[0].get_text().strip().replace(' ', '')
    try:
        value = float(value)
    except Exception as e:
        logging.info(f'Assets - Scrap one page: extract name from code - Error: {e}')
        value = value
    return value


def extract_variation_of_asset_from_one_page(html_code_extracted):
    logging.info('Assets - Scrap one page: extract variation from code')
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
        logging.info(f'Assets - Scrap one page: extract variation from code - Error: {e}')
        variation = variation
    return variation


def extract_name_id_of_asset_from_one_page(html_code_extracted):
    logging.info('Assets - Scrap one page: extract name id from code')
    return html_code_extracted[0]('h2', 'c-faceplate__isin')[0].get_text().strip()


def extract_id_of_asset_from_one_page(name_id):
    logging.info('Assets - Scrap one page: extract id of asset from code')
    return name_id.split('-')[0].split()[0].strip()


def extract_ouverture_of_asset_from_one_page(html_code_extracted):
    logging.info('Assets - Scrap one page: extract ouverture from code')
    ouverture = html_code_extracted[0]('span', 'c-instrument c-instrument--open')[0].get_text().strip()
    try:
        ouverture = float(ouverture)
    except Exception:
        ouverture = None
    return ouverture


def extract_cloture_of_asset_from_one_page(html_code_extracted):
    logging.info('Assets - Scrap one page: extract cloture from code')
    cloture_veille = html_code_extracted[0]('span', 'c-instrument c-instrument--previousclose')[0].get_text().strip()
    try:
        cloture_veille = float(cloture_veille)
    except Exception:
        cloture_veille = None
    return cloture_veille


def extract_haut_of_asset_from_one_page(html_code_extracted):
    logging.info('Assets - Scrap one page: extract haut from code')
    haut = html_code_extracted[0]('span', 'c-instrument c-instrument--high')[0].get_text().strip()
    try:
        haut = float(haut)
    except Exception:
        haut = None
    return haut


def extract_bas_of_asset_from_one_page(html_code_extracted):
    logging.info('Assets - Scrap one page: extract bas from code')
    bas = html_code_extracted[0]('span', 'c-instrument c-instrument--low')[0].get_text().strip()
    try:
        bas = float(bas)
    except Exception:
        bas = None
    return bas


def extract_volume_of_asset_from_one_page(html_code_extracted):
    logging.info('Assets - Scrap one page: extract volume from code')
    volume = html_code_extracted[0]('span', 'c-instrument c-instrument--totalvolume')[0].get_text().replace(' ',
                                                                                                            '').strip()
    try:
        volume = float(volume.replace(' ', ''))
    except Exception:
        volume = None
    return volume


def extract_dividende_of_asset_from_one_page(html_code_extracted):
    logging.info('Assets - Scrap one page: extract dividende from code')
    try:
        dividende = html_code_extracted[0]('p', 'c-list-info__value u-color-big-stone')[14].get_text().strip()
        dividende = float(dividende.split()[0])
        date_dividende = html_code_extracted[0]('p', 'c-list-info__value u-color-big-stone')[15].get_text().strip()
    except Exception as e:
        logging.info(f'Assets - Scrap one page: extract dividende from code - Error: {e}')
        try:
            dividende = 0
            date_dividende = html_code_extracted[0]('p', 'c-list-info__value u-color-big-stone')[14].get_text().strip()
        except Exception as e:
            logging.info(f'Assets - Scrap one page: extract dividende from code - Error: {e}')
            dividende = 0
            date_dividende = None
    return dividende, date_dividende


def extract_all_values_of_asset_from_one_page(html_code):
    html_code_extracted = extract_html_code_from_one_page(html_code)
    name = extract_name_of_asset_from_one_page(html_code_extracted)
    value = extract_value_of_asset_from_one_page(html_code_extracted)
    variation = extract_variation_of_asset_from_one_page(html_code_extracted)
    name_id = extract_name_id_of_asset_from_one_page(html_code_extracted)
    id_asset = extract_id_of_asset_from_one_page(name_id)
    ouverture = extract_ouverture_of_asset_from_one_page(html_code_extracted)
    cloture = extract_cloture_of_asset_from_one_page(html_code_extracted)
    haut = extract_haut_of_asset_from_one_page(html_code_extracted)
    bas = extract_bas_of_asset_from_one_page(html_code_extracted)
    volume = extract_volume_of_asset_from_one_page(html_code_extracted)
    dividende, date_dividende = extract_dividende_of_asset_from_one_page(html_code_extracted)

    dict_values = {'name': name, 'value': value, 'variation': variation, 'name_id': name_id, 'id_asset': id_asset,
                   'ouverture': ouverture, 'cloture': cloture, 'haut': haut, 'bas': bas, 'volume': volume,
                   'dividende': dividende, 'date_dividende': date_dividende}
    return dict_values


def ingest_data_in_db(model_db, dict_values, url=None):
    logging.info('Assets - Scrap one page: ingest values in db')
    today = datetime.datetime.today()
    model_db.objects.get_or_create(
        date=datetime.date(today.year, today.month, today.day),
        id_asset=dict_values['id_asset'],
        url=url,
        name=dict_values['name'],
        value=dict_values['value'],
        variation=dict_values['variation'],
        ouverture=dict_values['ouverture'],
        cloture_veille=dict_values['cloture'],
        haut=dict_values['haut'],
        bas=dict_values['bas'],
        volume=dict_values['volume'],
        dividende=dict_values['dividende'],
        date_dividende=dict_values['date_dividende'], )


def get_all_assets_ca_data_and_ingest_in_db(model_db):
    logging.info('Assets - Scrap all pages and get data')
    urls_for_each_asset = get_urls_for_each_asset()

    for url in tqdm(urls_for_each_asset):
        logging.info(f'Assets - Scrap one page: {url}')
        html_code = get_code(url)
        dict_values = extract_all_values_of_asset_from_one_page(html_code)
        ingest_data_in_db(model_db=model_db, dict_values=dict_values, url=url)


def get_all_assets_data_for_testing():
    logging.info('Assets - Scrap all pages and get data')
    url = get_urls_for_each_asset()[0]
    html_code = get_code(url)
    dict_values = extract_all_values_of_asset_from_one_page(html_code)
    return dict_values
