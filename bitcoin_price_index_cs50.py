import sys
import requests

try:
    # extract bitcoin price value
    r = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
    json = r.json()
    z = (json['bpi']['USD']['rate']).replace(',', '')#price
    mynum = float(sys.argv[1])#formatting
    x = (float(z)*mynum)
    print("$", end="")
    y = f"{x:,.4f}"
    print(y, end="")
    
#error handling    
except IndexError:
    sys.exit('Missing command-line argument ')
except ValueError:
    sys.exit('Command-line argument is not a number')
except requests.RequestException:
    print("error")
