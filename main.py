from email import header
from lib2to3.pytree import convert
from site import USER_SITE
from urllib import response
import requests
import urllib3
urllib3.disable_warnings()

class CurrencyConverter:
    def __init__(self, url):

        self.data= requests.get(url, verify=False).json()
        self.currecies= self.data['rates']
        """
        When a currency converter is created it should first try to load currency data from JSON (using the load_currency_data-method)
        If it doesn't find any json-data, it should try to get the data from the exchangerates API (using the fetch_currency_data-method)
        """

    def fetch_currency_data(self):
        """
        This method should fetch new currency data using the openexchangerate API
        It has some boilerplate code you can use.
        """
        # Use this code to fetch currency data from openexchangerates.org.
        app_id = "eafd01d91db74dde8db1f329d1d1a2f7" # Add your own app_id from openexchangerates.org here
        url = 'https://openexchangerates.org/api/latest.json?app_id={eafd01d91db74dde8db1f329d1d1a2f7'
        headers = {"accept": "application/json"} # This needs to be added, it tells the API that they should return JSON
        response = requests.get(url, headers=headers, verify=False)
        convert_into_json = response.json()
    
    def convert_from_usd(self, from_currency, to_currency, amount):
        initial_amount = amount
        if from_currency == 'USD':
            amount = amount / self.currecies[to_currency]

        amount = round(amount * self.currencies[to_currency], 4)
        """
        This method should convert from USD to a currency of choice
        You should not use an additional endpoint, the latest currencies are enough.
        """
            
    def convert_any_currency(self, from_currency, to_currency, amount):
        initial_amount = amount
        #fisrt convert it to USD if it is not in USD since USD is the base currency for conversion rate
        #this method takes arguments the currency you want to convets from, the currency in which you want to convert, and the amount you wan to convert
        url = "https://api.apilayer.com/exchangerates_data/convert?to={to_currency}&from={from_currency}&amount={amount}"

        payload = {}
        headers= {
        "apikey": "XsCzsB7NXiQN2t64c5t3yD4flb7cruid"
        }
        response = requests.request("GET", url, verify=False, headers=headers, data = payload)

        status_code = response.status_code
        result = response.json()

        if from_currency != 'USD':
            amount = amount / self.currecies[from_currency]

        #limiting the precision to 4 decimal places
        amount = round(amount * self.currecies[to_currency], 4)
        return amount      
        """
        This method is not required for Godkänt (G) grade
                
        # # # # # # FÖR VÄL GODKÄND - VG REQUIREMENT # # #
        This method converts from any currency, to any currency
        This should not require any more requests (e.g you do not need to make another request with a different base currency)
        """
    
    def list_currencies(self, url):

        url = "https://openexchangerates.org/api/currencies.json?prettyprint=false&show_alternative=false&show_inactive=false&app_id=eafd01d91db74dde8db1f329d1d1a2f7"

        headers = {"accept":"application/json"}

        record_response = requests.get(url, Verify=False, header=headers).json()
        
        print(f"\n Available Currencies : {len(record_response)}")

        for key, value in record_response.items():
            print(key, value)
        
        """
        curl --request GET 'https://api.apilayer.com/exchangerates_data/live?base=USD&symbols=EUR,GBP' \
        --header 'apikey: YOUR API KEY'
        This method lists available currencies in alphabetical order
        """
        
    
    def load_currency_data(self):
        """
        # # # # # FÖR GODKÄND - G REQUIREMENT # # # # #:
        This method should attempt to load currency data from a json-file.
        
        # # # # # FÖR ATT FÅ VÄL GODKÄNT - VG REQUIREMENT # # # # # #
        The function should look at the current time using the python datetime module (https://docs.python.org/3/library/datetime.html).
        If the saved data is older than more hour, it should automatically update the data being used and save it.
        This is possible by looking at the timestamp of the fetched data. You need to figure out yourself how this can be done.
        """
        pass

    def export_to_json(self):
        """
        This should export to JSON so that the application can be run again without the need to fetch new data
        """
        pass
    
def main():
    #This function should contain a menu allowing the user to
    print("[0] - (G) List all currencies")
    print("[1] - (G) Convert USD to a currency of choice")
    print("[2] - (G) Refresh the data (fetch new currency data, this is because the API updates new currency rates every hour)")
    print("[3] - (G) Export the data to JSON")
    print("[4] - (VG) Convert from any currency to any currency that is available on the API")

    
if __name__ == "__main__":
    main()

    new_currency_converter = CurrencyConverter()
    #this is the main function
    user_input = int(input())
    if user_input == 0:
        
        pass