
#what is the count of breweries in each of the states mentioned above?


import requests
def count_breweries_by_states(states):
    # OpenBreweryDB API endpoint
    api_url = "https://api.openbrewerydb.org/v1/breweries"

    try:
        # Fetch data from the API
        response = requests.get(api_url)
        response.raise_for_status()  # Raise exception for HTTP errors

        # Parse the JSON response
        breweries_data = response.json()

        # Initialize a dictionary to count breweries by state
        state_counts = {state: 0 for state in states}

        # Count breweries by states
        for brewery in breweries_data:
            state = brewery.get("state")
            if state in states:
                state_counts[state] += 1

        # Display the results
        print("Count of breweries in specified states:")
        for state, count in state_counts.items():
            print(f"- {state}: {count} breweries")

    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")

