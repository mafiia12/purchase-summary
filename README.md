# Purchase Summary

A command-line tool that reads a purchase records CSV file and produces a spending summary: grand total, spending by supplier, and a report of any invalid rows.

Built as a learning project while developing Python and Git skills, using the structure of real procurement data from the construction and finishing industry.

## Features

- Reads any CSV file with the expected columns
- Calculates total spending and breaks it down by supplier with percentage share
- Validates every row and skips invalid ones instead of crashing
- Reports skipped rows with their exact line number and reason
- Clear error messages for missing or empty files

## Requirements

- Python 3.8 or newer
- No external packages (uses the standard library only)

## Usage

Run with the included sample data:

```
python summary.py
```

Run with your own file:

```
python summary.py path/to/your_file.csv
```

## Input format

The CSV file must include a header row with these columns:

| Column | Description | Example |
|---|---|---|
| date | Purchase date (YYYY-MM-DD) | 2026-01-05 |
| supplier | Supplier name | Delta Supplies |
| item | Item description | Steel Rebar 12mm |
| unit | Unit of measure | ton |
| quantity | Quantity purchased | 3 |
| unit_price | Price per unit (EGP) | 38500 |

Line totals are calculated as `quantity × unit_price` and are never stored in the file.

## Sample output

```
Processed 10 of 10 rows

Grand total: 527,390.00 EGP

Spending by supplier:
  Delta Supplies         386,400.00 EGP  ( 73.3%)
  Al Nasr Trading         93,550.00 EGP  ( 17.7%)
  Horus Materials         42,340.00 EGP  (  8.0%)
  Nile Hardware            5,100.00 EGP  (  1.0%)
```

## Project structure

```
purchase-summary/
├── data/
│   ├── sample_purchases.csv   # clean sample data
│   └── broken.csv             # invalid rows for testing error handling
├── summary.py
└── README.md
```

## Data notice

All supplier names and prices in the `data/` folder are fictional and for demonstration only.