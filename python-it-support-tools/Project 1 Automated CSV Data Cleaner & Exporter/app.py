import csv
import os

# Sample raw data containing typos and inconsistent formatting
raw_data = [
    {"id": "1", "name": " Kevin kanyama ", "status": "Active", "tickets": "3"},
    {"id": "2", "name": "SARAH SMITH", "status": "Pending", "tickets": ""},
    {"id": "3", "name": "john doe", "status": "Inactive", "tickets": "0"},
]

def clean_data(data):
    cleaned = []
    for row in data:
        # Clean whitespace and standardize casing
        clean_row = {
            "ID": row["id"].strip(),
            "Name": row["name"].strip().title(),  # Capitalizes first letters
            "Status": row["status"].strip().upper(),
            # Handle missing ticket numbers by assigning a default 0
            "Tickets_Resolved": int(row["tickets"]) if row["tickets"].strip().isdigit() else 0
        }
        cleaned.append(clean_row)
    return cleaned

def export_to_csv(cleaned_data, filename="cleaned_support_data.csv"):
    keys = cleaned_data[0].keys()
    with open(filename, "w", newline="") as output_file:
        dict_writer = csv.DictWriter(output_file, fieldnames=keys)
        dict_writer.writeheader()
        dict_writer.writerows(cleaned_data)
    print(f"[SUCCESS] Cleaned dataset saved to {os.path.abspath(filename)}")

if __name__ == "__main__":
    processed_records = clean_data(raw_data)
    export_to_csv(processed_records)