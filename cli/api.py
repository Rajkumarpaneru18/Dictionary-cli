import requests
from constants import BASE_URL
from termcolor import colored


def get_definition(source_route, word):
    """Retrieve defination from the specified source and word."""

    url = f"{BASE_URL}{source_route}"
    response = requests.get(url, json={"search-word": word})
    return response


def handle_response(response, json_output=False):
    """Process the response from the backend server."""
    if response.status_code == 200:
        data = response.json()
        if json_output:
            import json
            return json.dumps(data, indent=2)
        else:
            return (
                colored(f"Word: {data['word']}", "blue")
                + "\n"
                + colored(f"Meaning: {data['meaning']}")
                + "\n"
                + colored(f"Source: {data['source']}", "cyan"))
    else:
        return colored("Failed to retrieve data.", "red")
