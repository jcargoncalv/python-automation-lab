from bs4 import BeautifulSoup

def parse_table(html):

    extracted_data = []

    # Parse html into navigable objects using lxml
    soup = BeautifulSoup(html,'lxml')
    #Finds <table> tags
    tables = soup.find("table")
    #Find all <tr> table rows
    rows = tables.find("tr")
    
    for row in rows:

        #Find table columns, headers <th> and cells <td>
        columns = rows.find(["th", "td"])

        clean_columns = [ 
            column.text.strip() 
            for column in columns ]

        extracted_data.append(clean_columns)

    return extracted_data


