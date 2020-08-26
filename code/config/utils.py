import datetime

import requests
from user_agent import generate_user_agent
from bs4 import BeautifulSoup as soup
import logging

logging.basicConfig(level=logging.INFO)


def get_code(url):
    """Return the code html"""
    # Define the user agent
    headers = {'User-Agent': generate_user_agent(device_type="desktop",
                                                 os=('mac', 'linux'))}
    # Open the url file and get the html code of the page
    req = requests.Session()
    req = requests.get(url, headers=headers)
    return soup(req.text, "lxml")


def extract_name_of_fund_from_one_page(html_code_extracted):
    logging.info('Scrap one page: extract name from code')
    return html_code_extracted[0].a.get_text().strip()


def extract_value_of_fund_from_one_page(html_code_extracted):
    logging.info('Scrap one page: extract value from code')
    value = html_code_extracted[0]('span', 'c-instrument c-instrument--last')[0].get_text().strip().replace(' ', '')
    try:
        value = float(value)
    except Exception as e:
        logging.info(f'Scrap one page: extract name from code - Error: {e}')
        value = value
    return value


def extract_currency_of_fund_from_one_page(html_code_extracted):
    logging.info('Scrap one page: extract currency from code')
    return html_code_extracted[0]('span', 'c-faceplate__price-currency')[0].get_text().strip()


def extract_variation_of_fund_from_one_page(html_code_extracted):
    logging.info('Scrap one page: extract variation from code')
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
        logging.info(f'Scrap one page: extract variation from code - Error: {e}')
        variation = variation
    return variation


def extract_name_id_of_fund_from_one_page(html_code_extracted):
    logging.info('Scrap one page: extract name id of fund from code')
    return html_code_extracted[0]('h2', 'c-faceplate__isin')[0].get_text().strip()


def extract_id_of_fund_from_one_page(name_id):
    logging.info('Scrap one page: extract id of fund from code')
    try:
        id_fund = name_id.split('-')[0].strip()
    except Exception as e:
        print(e)
        id_fund = name_id
    return id_fund


def extract_date_of_fund_from_one_page(html_code_extracted):
    logging.info('Scrap one page: extract date from code')
    date_ = html_code_extracted[0]('div', 'c-faceplate__real-time')[0].get_text().strip()

    try:
        date = date_.split()[-1]
        date = datetime.datetime.strptime(date, '%d/%m/%Y')
    except Exception as e:
        logging.info(f'Scrap one page: extract date from code - Error: {e}')
        date = None
    return date


def extract_risk_of_fund_from_one_page(html_code):
    logging.info('Scrap one page: extract risk from code')

    try:
        risk_ = \
            html_code('div',
                      'c-faceplate__quotation c-faceplate__quotation--new-line c-faceplate__quotation--margin-top')[0]

        risk = int(risk_('div', 'c-gauge')[0]['data-gauge-current-step'])
    except Exception as e:
        logging.info(f'Scrap one page: extract date from code - Error: {e}')
        risk = None
    return risk


def extract_net_asset_of_fund_from_one_page(html_code):
    logging.info('Scrap one page: extract net asset from code')
    net_asset_ = html_code('div', 'c-faceplate__quotation')[0]('ul')[0]('li')[-1].get_text().strip()
    net_asset_ = net_asset_.split('\n')[-1].strip().split('/')[-1].strip().replace(' ', '')

    try:
        net_asset = float(net_asset_)
    except Exception as e:
        logging.info(f'Scrap one page: extract net asset from code - Error: {e}')
        net_asset = None
    return net_asset
