# Setup and Installation

10EQS Evaluation

## Requirements

1. Read and process the CSV Data
2. Choose and integrate ONE external data source
    - Could be pricing data, market trends, economic indicators, etc.
    - Document why you chose this source
3. Create ONE useful insight
    - Examples: price comparison, trend alert, recommended system
    - The specific insight is up to you - be creative!

## Installation

Assuming `python` is installed and set up on your machine, simply navigate to the directory and run the below command to execute.

Navigate to the project directory before proceeding to the next step.

`cd /path/to/python-challenge`

### RapidAPI Setup

Go to `https://rapidapi.com/remote-skills-remote-skills-default/api/grocery-pricing-api/` and sign up for an account (free).

After that create a `.env` file and add thhe following keys:

- API_URL
- API_KEY
- API_HOST

The `API_URL` will be `https://grocery-pricing-api.p.rapidapi.com/searchGrocery`
The `API_KEY` is provided after signing up for an account
The `API_HOST` will be `grocery-pricing-api.p.rapidapi.com`

After that is setup, we need to install `dotenv` via `pip install dotenv`. Once that is successful, you should be able to run

```code
python src/analysis.py data/products.csv
```

and see the output in `report.md`

## Executing

Running the command:

```code
python src/analysis.py data/products.csv
```

Include the argument `data/products.csv` in order to specify which `csv` file to include as an input file.

### Approach

The overall approach was to create a helper class called CSVHelper, which handled the parsing and cleaning up of the csv file. In `analysis.py`, the class is imported and passed along the corresponding variables.

The approach utilized classes to group related data & functions together for a more organized and concise approach. This also allows the reusability of the class in another application if warranted.

Potential limitations may include if CSV data format (such as dates, pricing, default values such as out of stock) change beyond what the class is currenlty able to handle.

The CSVHelper class was overall straightforward, around 10 minutes of setting up and tweaking.

The report generator took a bit more time, roughly 20 minutes.

Integrating RapidAPI and generating a price difference to reflect profit or loss took roughly 5 minutes.

Refactoring and cleanup took around 25 minutes.
