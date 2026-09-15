import csv
import sys

DEFAULT_FILE = "data/sample_purchases.csv"

if len(sys.argv) > 1:
    FILE_PATH = sys.argv[1]
else:
    FILE_PATH = DEFAULT_FILE
    print(f"No file given, using default: {DEFAULT_FILE}")
try:
    with open(FILE_PATH, mode="r", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        rows = list(reader)
except FileNotFoundError:
    print(f"Error: file not found: {FILE_PATH}")
    sys.exit(1)

print(f"Loaded {len(rows)} rows from {FILE_PATH}")

print("\nColumns:")
for column in rows[0].keys():
    print(f"  - {column}")

print("\nFirst 3 rows:")
for row in rows[:3]:
    print(f"  {row['date']} | {row['supplier']} | {row['item']} | {row['quantity']} {row['unit']} @ {row['unit_price']}")

grand_total = 0
totals_by_supplier = {}
skipped = []

for index, row in enumerate(rows, start=2):
    supplier = (row.get("supplier") or "").strip()
    if not supplier:
        skipped.append((index, "missing supplier"))
        continue

    try:
        quantity = float(row["quantity"])
        unit_price = float(row["unit_price"])
    except (ValueError, TypeError):
        skipped.append((index, "invalid quantity or price"))
        continue

    if quantity <= 0 or unit_price <= 0:
        skipped.append((index, "zero or negative value"))
        continue

    line_total = quantity * unit_price
    grand_total += line_total
    totals_by_supplier[supplier] = totals_by_supplier.get(supplier, 0) + line_total

print(f"\nProcessed {len(rows) - len(skipped)} of {len(rows)} rows")

if skipped:
    print(f"Skipped {len(skipped)} rows:")
    for line_number, reason in skipped:
        print(f"  line {line_number}: {reason}")

print(f"\nGrand total: {grand_total:,.2f} EGP")

print("\nSpending by supplier:")
for supplier, total in sorted(totals_by_supplier.items(), key=lambda item: item[1], reverse=True):
    share = total / grand_total * 100
    print(f"  {supplier:<20} {total:>12,.2f} EGP  ({share:5.1f}%)")