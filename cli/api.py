import requests
from constants import BASE_URL
from termcolor import colored

def get_definition(source_route, word):
    """Retrieve definition from the specified source and word."""
    # Construct the URL using the base URL and the provided source route
    url = f"{BASE_URL}{source_route}"
    # Make a GET request to the constructed URL, passing the search word as JSON
    response = requests.get(url, json={"search-word": word})
    return response

def handle_response(response, json_output=False):
    """Process the response from the backend server."""
    # Check if the response status code is 200 (OK)
    if response.status_code == 200:
        # If the response is successful, parse the JSON data
        data = response.json()
        if json_output:
            # If JSON output is requested, return the data as a formatted JSON string
            import json
            return json.dumps(data, indent=2)
        else:
            # If JSON output is not requested, construct and format the response message
            return (
                colored(f"Word: {data['word']}", "blue")
                + "\n"
                + colored(f"Meaning: {data['meaning']}", "green")
                + "\n"
                + colored(f"Source: {data['source']}", "cyan"))
    else:
        # If the response status code is not 200, return a failure message
        return colored("Failed to retrieve data.", "red")
