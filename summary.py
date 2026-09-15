import csv

FILE_PATH = "data/sample_purchases.csv"

with open(FILE_PATH, mode="r", encoding="utf-8") as file:
    reader = csv.DictReader(file)
    rows = list(reader)

print(f"Loaded {len(rows)} rows from {FILE_PATH}")

print("\nColumns:")
for column in rows[0].keys():
    print(f"  - {column}")

print("\nFirst 3 rows:")
for row in rows[:3]:
    print(f"  {row['date']} | {row['supplier']} | {row['item']} | {row['quantity']} {row['unit']} @ {row['unit_price']}")
    print("\nType check:", type(rows[0]['quantity']))
