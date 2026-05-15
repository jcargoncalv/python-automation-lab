import pandas as pd

# Main CSV export method for tables
def export_to_csv(data, filename):

    # Separate table header from data
    header = data[0]
    rows = data[1:]

    # Create Dataframe equivalent for the table
    dataframe = pd.DataFrame(rows, columns=header)

    # Convert new DataFrame to CSV format and save
    dataframe.to_csv(filename, index=False)

    print(f"CSV saved to: {filename}")