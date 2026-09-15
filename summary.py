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

grand_total = 0
for row in rows:
    quantity = float(row["quantity"])
    unit_price = float(row["unit_price"])
    grand_total += quantity * unit_price

print(f"\nGrand total: {grand_total:,.2f} EGP")