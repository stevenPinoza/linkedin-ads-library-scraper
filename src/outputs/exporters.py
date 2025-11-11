thonimport json
import csv

def export_to_json(data, filename):
    """
    Export data to JSON file.

    :param data: Data to export
    :param filename: Output file name
    """
    with open(filename, 'w') as f:
        json.dump(data, f, indent=4)

def export_to_csv(data, filename):
    """
    Export data to CSV file.

    :param data: Data to export
    :param filename: Output file name
    """
    with open(filename, mode='w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=data[0].keys())
        writer.writeheader()
        writer.writerows(data)