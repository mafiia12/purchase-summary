import csv
import sys

DEFAULT_FILE = "data/sample_purchases.csv"


def get_file_path():
    """Return the file path from the command line, or the default."""
    if len(sys.argv) > 1:
        return sys.argv[1]
    print(f"No file given, using default: {DEFAULT_FILE}")
    return DEFAULT_FILE


def load_rows(file_path):
    """Read the CSV file and return its rows as a list of dictionaries."""
    try:
        with open(file_path, mode="r", encoding="utf-8") as file:
            return list(csv.DictReader(file))
    except FileNotFoundError:
        print(f"Error: file not found: {file_path}")
        sys.exit(1)


def print_preview(rows, file_path):
    """Show row count, column names, and the first few rows."""
    print(f"Loaded {len(rows)} rows from {file_path}")

    print("\nColumns:")
    for column in rows[0].keys():
        print(f"  - {column}")

    print("\nFirst 3 rows:")
    for row in rows[:3]:
        print(f"  {row['date']} | {row['supplier']} | {row['item']} | {row['quantity']} {row['unit']} @ {row['unit_price']}")


def summarize(rows):
    """Validate rows and calculate totals. Returns (grand_total, totals_by_supplier, skipped)."""
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

    return grand_total, totals_by_supplier, skipped


def print_report(row_count, grand_total, totals_by_supplier, skipped):
    """Print the processing summary, grand total, and spending by supplier."""
    print(f"\nProcessed {row_count - len(skipped)} of {row_count} rows")

    if skipped:
        print(f"Skipped {len(skipped)} rows:")
        for line_number, reason in skipped:
            print(f"  line {line_number}: {reason}")

    print(f"\nGrand total: {grand_total:,.2f} EGP")

    print("\nSpending by supplier:")
    for supplier, total in sorted(totals_by_supplier.items(), key=lambda item: item[1], reverse=True):
        share = total / grand_total * 100
        print(f"  {supplier:<20} {total:>12,.2f} EGP  ({share:5.1f}%)")


def main():
    file_path = get_file_path()
    rows = load_rows(file_path)

    if not rows:
        print("Error: file is empty or has no data rows")
        sys.exit(1)

    print_preview(rows, file_path)
    grand_total, totals_by_supplier, skipped = summarize(rows)
    print_report(len(rows), grand_total, totals_by_supplier, skipped)


if __name__ == "__main__":
    main()