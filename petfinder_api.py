# Handles Petfinder API requests and filters pet data based on search inputs
import json
import requests

# Load API keys from a separate config file
with open("api_keys.json") as x:
    config = json.load(x)


# Gets pet data based on user input (like type, location, filters, etc.)
def get_pet_data(animal_type, location, breed=None, age=None, gender=None, with_photos=False):
    # First, get an access token from Petfinder
    token_response = requests.post(
        "https://api.petfinder.com/v2/oauth2/token",
        data={
            "grant_type": "client_credentials",
            "client_id": config["api_key"],
            "client_secret": config["secret_key"]
        }
    )

    # Grab the token from the response
    api_key = token_response.json().get("access_token")

    # Set up the headers for authorization
    headers = {"Authorization": f"Bearer {api_key}"}

    # Set up the required and optional parameters
    params = {
        "type": animal_type,
        "location": location,
        "limit": 20
    }

    if breed:
        params["breed"] = breed
    if age:
        params["age"] = age
    if gender:
        params["gender"] = gender
    if with_photos:
        params["include_photos"] = 1

    # Make the GET request to get matching pets
    response = requests.get("https://api.petfinder.com/v2/animals", headers=headers, params=params)

    # If something went wrong, return an empty list
    if response.status_code != 200:
        print(f"Error fetching data: {response.status_code}")
        return []

    # Return the list of pets
    return response.json().get("animals", [])
