from src.extractor import fetch_html
from src.parser import parse_tables
from src.exporter import export_to_csv

# Sample tables from w3schools site
URL = 'https://www.w3schools.com/html/html_tables.asp'
# Output path for the CSV files
output_path = 'tools/web_scraping/table_extractor/output/'

def main():
    # Main Pipeline

    # Fetch HTML from URL
    raw_html = fetch_html(URL)

    # Parse table data
    table_data = parse_tables(raw_html)

    # For each table found, export to a separate csv
    for count, table in enumerate(table_data, start=1):
        export_to_csv(table, f"{output_path}extracted_table_{count}.csv")   

if __name__ == "__main__":
    main()
