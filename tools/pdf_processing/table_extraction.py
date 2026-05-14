import pandas as pd
import pdfplumber

# Defines file path for the target pdf
filepath = 'assets/foo.pdf'

# Result list to store all DataFrames extracted from the PDF
result = []

# Function to sanitize column names, avoiding errors. List of column names as input
def clean_columns(columns):
    # List of sanitized column names
    cleaned = []
    # Dict to track how many times the same column name occurs, allowing duplicate detection
    seen = {}

    for col in columns:
        # Converts to string and removes whitespace 
        # If empty or NoneType, replaces with 'unnamed'
        col = str(col).strip() if col else 'unnamed'

        # if column name was already matched
        if col in seen:
            seen[col] += 1 # increment the seen counter
            # Replace column name with format: Ex.: 'data_2' or 'client_name_3'
            col = f"{col}_{seen[col]}"
        else:
            seen[col] = 0
        
        cleaned.append(col)
    
    return cleaned

# Open target pdf with pdf plumber
with pdfplumber.open(filepath) as pdf:

    # For each page in pdf
    for page in pdf.pages:
        # Extract all tables
        tables = page.extract_tables()

        for table in tables:
            # Ignore empty table or invalid tables (header without data or data without header)
            if not table or len(table) < 2:
                continue
            
            # Convert to DataFrame, first row is header, the rest is data
            df = pd.DataFrame(table[1:], columns=table[0])

            # Clean column names, avoid duplicates
            df.columns = clean_columns(df.columns)

            # Reset index, preserving the basic integer index and no columns becoming indexes
            df = df.reset_index(drop=True)

            # Adds final dataframe to result list
            result.append(df)
# Concatenate all resulting DFs in result list, ignoring their index and setting a single integer index
final_df = pd.concat(result, ignore_index=True)

# Writes data in CSV format to disk, removing Pandas indexes
final_df.to_csv('foo.csv', index=False)

# Preview results
print(final_df.head())