# from assets.scripts.quantpy.portfolio import Portfolio
import requests
import json
import pandas as pd
import numpy as np
from tqdm import tqdm
import time
from assets.models import Assets

assets_list = np.unique([y.id_asset for y in Assets.objects.all()])

dict_res = {'id_asset': [], 'exchange': [], 'shortname': [], 'quoteType': [], 'symbol': [], 'index': [], 'score': [],
            'typeDisp': [], 'longname': []}

for asset in tqdm(assets_list):

    dict_res['id_asset'].append(asset)

    url = "https://apidojo-yahoo-finance-v1.p.rapidapi.com/auto-complete"

    querystring = {"region": "FR", "q": f"{asset}"}

    headers = {
        'x-rapidapi-host': "apidojo-yahoo-finance-v1.p.rapidapi.com",
        'x-rapidapi-key': "55bf12d4b0msh279ea37b0091a3ap14f315jsn5cb034cf2b7f"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)

    try:
        result = json.loads(response.text)["quotes"][0]
        dict_res['exchange'].append(result['exchange'])
        dict_res['shortname'].append(result['shortname'])
        dict_res['quoteType'].append(result['quoteType'])
        dict_res['symbol'].append(result['symbol'])
        dict_res['index'].append(result['index'])
        dict_res['score'].append(result['score'])
        dict_res['typeDisp'].append(result['typeDisp'])
        dict_res['longname'].append(result['longname'])
    except Exception as e:
        print(f'Error with asset: {asset} - error: {e}')
        print(f'Response: {response.text}')
        dict_res['exchange'].append(None)
        dict_res['shortname'].append(None)
        dict_res['quoteType'].append(None)
        dict_res['symbol'].append(None)
        dict_res['index'].append(None)
        dict_res['score'].append(None)
        dict_res['typeDisp'].append(None)
        dict_res['longname'].append(None)

    time.sleep(0.5)

pd.DataFrame(dict_res).to_csv('id_asset_full_list.csv', index=False, header=True)
