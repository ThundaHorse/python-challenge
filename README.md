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

The CSVHelper class was overall straightforward, around 20 minutes of setting up and tweaking.

The report generator took a bit more time, roughly 35 minutes.