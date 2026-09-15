import csv

FILE_PATH = "data/sample_purchases.csv"

with open(FILE_PATH, mode="r", encoding="utf-8") as file:
    reader = csv.DictReader(file)
    rows = list(reader)

print(f"Loaded {len(rows)} rows from {FILE_PATH}")
