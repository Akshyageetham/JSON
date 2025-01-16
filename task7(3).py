#count the number of types of breweries present in individual cities of the state mentioned above


import requests
def count_brewery_types_by_city(states):
    # OpenBreweryDB API endpoint
    api_url = "https://api.openbrewerydb.org/v1/breweries"

    try:
        # Fetch data from the API
        response = requests.get(api_url)
        response.raise_for_status()  # Raise exception for HTTP errors

        # Parse the JSON response
        breweries_data = response.json()

        # Initialize a dictionary to count brewery types by city
        city_brewery_types = {}

        # Count brewery types by city within the specified states
        for brewery in breweries_data:
            state = brewery.get("state")
            city = brewery.get("city")
            brewery_type = brewery.get("brewery_type")

            if state in states and city and brewery_type:
                if city not in city_brewery_types:
                    city_brewery_types[city] = {}
                if brewery_type not in city_brewery_types[city]:
                    city_brewery_types[city][brewery_type] = 0
                city_brewery_types[city][brewery_type] += 1

        # Display the results
        print("Brewery types in individual cities of specified states:")
        for city, types in city_brewery_types.items():
            print(f"City: {city}")
            for brewery_type, count in types.items():
                print(f"  {brewery_type}: {count}")

    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")
