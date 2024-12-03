import pandas as pd

def add_prefix_to_addresses(input_csv, output_csv, prefix_url, address_column):
    """
    Add a prefix URL to addresses in a CSV file.
    
    Args:
        input_csv (str): Path to the input CSV file
        output_csv (str): Path to save the output CSV file
        prefix_url (str): URL prefix to add to each address
        address_column (str): Name of the column containing addresses
    
    Raises:
        FileNotFoundError: If input CSV file doesn't exist
        KeyError: If address_column is not found in the CSV
        Exception: For other errors during processing
    """
    try:
        # Validate inputs
        if not prefix_url:
            raise ValueError("prefix_url cannot be empty")
        
        if not address_column:
            raise ValueError("address_column cannot be empty")
            
        # Read the CSV file
        df = pd.read_csv(input_csv)
        
        # Verify the address column exists
        if address_column not in df.columns:
            raise KeyError(f"Column '{address_column}' not found in the CSV file")
        
        # Add the prefix to each address in the specified column
        # Handle potential NaN values by converting to string first
        df[address_column] = df[address_column].fillna('')
        df[address_column] = prefix_url + df[address_column].astype(str)
        
        # Remove double slashes that might occur if prefix ends with / and address starts with /
        df[address_column] = df[address_column].str.replace('//', '/')
        
        # Add back the protocol double slash
        df[address_column] = df[address_column].str.replace('http:/', 'http://')
        df[address_column] = df[address_column].str.replace('https:/', 'https://')
        
        # Save the modified data to a new CSV file
        df.to_csv(output_csv, index=False)
        print(f"Successfully prefixed addresses and saved to {output_csv}")
        
        # Return the DataFrame in case it's needed for further processing
        return df
        
    except FileNotFoundError:
        print(f"Error: Input file '{input_csv}' not found")
        raise
    except KeyError as e:
        print(f"Error: {str(e)}")
        raise
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        raise

# Example usage
if __name__ == "__main__":
    input_csv = "addresses.csv"  # Input CSV file with addresses
    output_csv = "prefixed_addresses.csv"  # Output CSV file to save the results
    prefix_url = "https://gmgn.ai/base/address/"
    address_column = "Address"  # Column name containing the addresses

    try:
        df = add_prefix_to_addresses(input_csv, output_csv, prefix_url, address_column)
    except Exception as e:
        print(f"Failed to process addresses: {str(e)}")