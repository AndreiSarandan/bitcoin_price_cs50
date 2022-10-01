import sys
import requests

try:
    # extract bitcoin price value
    r = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
    json = r.json()
    z = (json['bpi']['USD']['rate']).replace(',', '')
    x = (float(z)*float(sys.argv[1]))
    print(format(x, ".4f"))
except IndexError:
    sys.exit('Missing command-line argument ')
except ValueError:
    sys.exit('Command-line argument is not a number')
except requests.RequestException:
    print("error")
