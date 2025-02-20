# NYT Best Sellers Fetcher

## Objective
Fetch the current New York Times Best Sellers list.

## Requirements
- Python 3.8+
- Poetry
- An API key from The New York Times (https://developer.nytimes.com/)

## Setup
1. Install Poetry:
   ```bash
   curl -sSL https://install.python-poetry.org | python3 -

2. Navigate to the folder:
    cd ex-1-14

3. Install dependencies:
    poetry install

4. Get an API key from The New York Times and set it as an environment variable:
    export NYT_API_KEY="your-api-key-here"


## Usage
    Run the script:

    poetry run python nyt_best_sellers.py


## Expected Output

1. "The Heaven & Earth Grocery Store" by James McBride
2. "Lessons in Chemistry" by Bonnie Garmus
3. "Demon Copperhead" by Barbara Kingsolver
