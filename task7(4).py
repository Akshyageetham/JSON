#count and list how many breweries have websites in the states of Alaska, Maine,Newyork.

import requests

def count_and_list_breweries_with_websites(states):
    # OpenBreweryDB API endpoint
    api_url = "https://api.openbrewerydb.org/v1/breweries"

    try:
        # Fetch data from the API
        response = requests.get(api_url)
        response.raise_for_status()  # Raise exception for HTTP errors

        # Parse the JSON response
        breweries_data = response.json()

        # Initialize a dictionary to count breweries with websites by state
        state_website_counts = {state: [] for state in states}

        # Filter breweries by states and check for websites
        for brewery in breweries_data:
            state = brewery.get("state")
            website_url = brewery.get("website_url")
            name = brewery.get("name")

            if state in states and website_url:
                state_website_counts[state].append(name)

        # Display the results
        print("Breweries with websites in specified states:")
        for state, breweries in state_website_counts.items():
            print(f"State: {state}")
            print(f"  Number of breweries with websites: {len(breweries)}")
            for brewery in breweries:
                print(f"    - {brewery}")

    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")