import requests
class CountryData:
    def __init__(self,url):
        self.url=url
        self.data=self.fetch_data()
    def fetch_data(self):
        response=requests.get(self.url)
        return response.json()
    def display_euro_currencies(self):
        euro_countries=[]
        for country in self.data:
            try:
                if hasattr(country, 'currencies') and 'EUR' in country['currencies'].keys():
                    if hasattr(country, 'name') and 'common' in country['name']:
                      euro_countries.append(country['name']['common'])
            except KeyError as e:
                print(f"Error: {e} in country {country.get('name', {}).get('common', 'Unknown')}")
            except AttributeError as e:
                print(f"Error: {e} in country {country.get('name', {}).get('common', 'Unknown')}")

            print("Countries that use EUR as their currency:")
            for country in euro_countries:
                print(country)
url = "https://restcountries.com/v3.1/all"
country_data = CountryData(url)
country_data.display_euro_currencies()
