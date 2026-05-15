from bs4 import BeautifulSoup

# Tables parsing method from raw HTML
def parse_tables(html):

    extracted_tables = []

    # BS object using lxml
    soup = BeautifulSoup(html,'lxml')
    # Find all tables present in the html
    tables = soup.find_all("table")

    # For each table found, parse its contents
    for table in tables:
        extracted_tables.append(
            parse_table(table)
        )

    return extracted_tables


def parse_table(table):

    extracted_data = []

    # Parse each row for the <tr> tag
    rows = table.find_all("tr")
    
    # For each row
    for row in rows:

        #Find table columns, headers <th> and cells <td>
        columns = row.find_all(["th", "td"])

        # Clean the result of whitespaces
        clean_columns = [ 
            column.text.strip() 
            for column in columns ]

        extracted_data.append(clean_columns)

    return extracted_data