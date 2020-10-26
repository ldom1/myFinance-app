from assets.scripts.quantpy.portfolio import Portfolio

import requests

url = "https://apidojo-yahoo-finance-v1.p.rapidapi.com/auto-complete"

querystring = {"region":"FR","q":"FR0000121014"}

headers = {
    'x-rapidapi-host': "apidojo-yahoo-finance-v1.p.rapidapi.com",
    'x-rapidapi-key': "55bf12d4b0msh279ea37b0091a3ap14f315jsn5cb034cf2b7f"
    }

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)
