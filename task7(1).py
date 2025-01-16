#List the names of all breweries present in the states of Alaska,Maine and New York
import requests

def fetch_breweries_by_states(states):
    api_url = "https://api.openbrewerydb.org/v1/breweries"
    try:
        # Fetch data from the API
        response = requests.get(api_url)
        response.raise_for_status()  # Raise exception for HTTP errors

        # Parse the JSON response
        breweries_data = response.json()

        # Filter breweries by states
        filtered_breweries = [
            brewery["name"] for brewery in breweries_data if brewery.get("state") in states
        ]

        # Display the results
        print("Breweries in Alaska, Maine, and New York:")
        for brewery in filtered_breweries:
            print(f"- {brewery}")

    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")

