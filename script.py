import csv
import requests

def check_url_status(url):
    """
    Checks the HTTP status code of a given URL.

    Args:
        url (str): The URL to check.

    Returns:
        int or str: The HTTP status code if the request is successful. 
                   If an error occurs, returns a string with the error message.
    """
    try:
        response = requests.get(url, timeout=10)
        return response.status_code
    except requests.RequestException as e:
        return f"Error: {e}"

# Read the CSV file and process each URL
with open('Task 2 - Intern.csv', mode='r', encoding='utf-8') as file:
    """
    Reads a CSV file containing URLs and checks the status code of each URL.

    The CSV file is expected to have URLs in the first column. The header row is skipped.

    Prints the status code and URL in the format: (STATUS CODE) URL
    """
    csv_reader = csv.reader(file)
    next(csv_reader)  # Skip the header row
    for row in csv_reader:
        url = row[0].strip()  # Get the URL from the first column
        status_code = check_url_status(url)
        print(f"({status_code}) {url}")
