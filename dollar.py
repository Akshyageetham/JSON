import requests

class CountryData:
    def __init__(self, url):
        self.url = url
        self.data = self.fetch_data()

    def fetch_data(self):
        response = requests.get(self.url)
        return response.json()

    def display_dollar_countries(self):
        dollar_countries = []
        for country in self.data:
            try:
                if 'USD' in country['currencies'].keys():
                    dollar_countries.append(country['name']['common'])
            except KeyError as e:
                print(f"Error: {e} in country {country.get('name', {}).get('common', 'Unknown')}")

        print("Countries that use USD as their currency:")
        for country in dollar_countries:
            print(country)

# Usage
url = "https://restcountries.com/v3.1/all"
country_data = CountryData(url)
country_data.display_dollar_countries()

