import requests

try:
    # extract bitcoin price value
    r = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
    json = r.json()
    z = (json['bpi']['USD']['rate'])
    print(z)
except requests.RequestException:
    print("error")
