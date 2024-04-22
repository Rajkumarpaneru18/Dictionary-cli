#! /usr/bin/python3

import argparse
from spinner import Spinner
from api import get_definition, handle_response
from utils import save_image, open_image
from termcolor import colored

# Function to format the definition output


def format_definitions(word, definitions):
    """Format the output for word definitions with source information."""
    formatted_output = colored(f"Word: {word}", "blue") + "\n"

    for definition in definitions:
        meaning = definition["meaning"]
        source = definition["source"]

        # Add the meaning with a bullet point
        formatted_output += "  - " + meaning + "\n"
        # Add the source
        formatted_output += f"    Source: [{source}](http://{source})\n"

    return formatted_output

# Function for interactive mode


def interactive_mode():
    """Prompt the user for input to determine CLI options."""
    source_choices = {
        "1": "/google",
        "2": "/merriam",
        "3": "/dictionary",
        "4": "/oed"
    }

    while True:
        print("Select sources (separated by commas):")
        print("1: Google")
        print("2: Merriam-Webster")
        print("3: Dictionary.com")
        print("4: Oxford Dictionary")

        choices = input("Enter your choices (or 'exit' to quit): ")
        if choices.lower() == "exit":
            print("Exiting interactive mode. Goodbye!")
            break

        source_routes = [
            source_choices[c.strip()] for c in choices.split(",") if c.strip() in source_choices
        ]

        if not source_routes:
            print(colored("No valid source selected_ Please try again.", "red"))
            continue

        json_output = input(
            "Display output in JSON format? (y/n): ").strip().lower() == "y"

        search_word = input(
            "Enter the word to search for (or 'exit' to quit): ")
        if search_word.lower() == "exit":
            print("Exiting interactive mode. Goodbye!")
            break

        # Start the spinner
        spinner = Spinner("Fetching information")
        spinner.start()

        # Fetch data from the selected source routes
        results = []
        for route in source_routes:
            response = get_definition(route, search_word)
            if response.status_code == 200:
                data = response.json()
                results.append({
                    "meaning": data["meaning"],
                    "source": data["source"]
                })
            else:
                results.append({
                    "meaning": "Failed to retrieve data",
                    "source": f"{route}"
                })

        spinner.stop()

        # Display formatted output
        formatted_output = format_definitions(search_word, results)
        print(formatted_output)

# Main function for CLI


def main():
    parser = argparse.ArgumentParser(
        description="Retrieve word meanings from different sources.")

    # Add interactive mode flag
    parser.add_argument("-i", "--interactive",
                        action="store_true", help="Enter interactive mode.")

    # Add source selection flags
    parser.add_argument("-g", "--google", action="store_true",
                        help="Retrieve image results from Google.")
    parser.add_argument("-m", "--merriam", action="store_true",
                        help="Retrieve definitions from Merriam-Webster.")
    parser.add_argument("-d", "--dictionary", action="store_true",
                        help="Retrieve definitions from Dictionary.com.")
    parser.add_argument("-o", "--oed", action="store_true",
                        help="Retrieve definitions from Oxford Dictionary.")

    # Add output format flag
    parser.add_argument("-j", "--json", action="store_true",
                        help="Display output in JSON format.")

    # Add word to search for (normal mode)
    parser.add_argument("word", nargs="?", help="The word to search for.")

    args = parser.parse_args()

    if args.interactive:
        interactive_mode()  # Start interactive mode
    else:
        # Normal mode: Ensure source_routes is initialized
        source_routes = []
        if args.google:
            source_routes.append("/google")
        if args.merriam:
            source_routes.append("/merriam")
        if args.dictionary:
            source_routes.append("/dictionary")
        if args.oed:
            source_routes.append("/oed")

        if not source_routes:
            print("Please specify at least one source.")
            return

        if not args.word:
            print("Please provide a word to search or use '-i' for interactive mode.")
            return

        spinner = Spinner("Fetching information")
        spinner.start()

        results = []
        for route in source_routes:
            response = get_definition(route, args.word)
            if response.status_code == 200:
                data = response.json()
                results.append({
                    "meaning": data["meaning"],
                    "source": data["source"]
                })
            else:
                results.append({
                    "meaning": "Failed to retrieve data",
                    "source": f"{route}"
                })

        spinner.stop()

        # Display formatted output
        formatted_output = format_definitions(args.word, results)
        print(formatted_output)


# Run the CLI application
if __name__ == "__main__":
    main()
