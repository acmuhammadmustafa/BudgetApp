import pandas as pd
from io import StringIO, BytesIO


def parse_bofa_csv(file_content):
    """
    Parse Bank of America CSV export
    Expected columns: Date, Description, Amount (or similar variations)
    """
    try:
        # Handle both bytes and string content
        if isinstance(file_content, bytes):
            file_content = file_content.decode('utf-8')

        # Read CSV, skipping header rows if needed
        df = pd.read_csv(StringIO(file_content))

        # Normalize column names (BofA exports vary)
        df.columns = df.columns.str.strip().str.lower()

        # Expected columns: date, description, amount
        required_cols = ['date', 'description', 'amount']

        # Handle variations in column names
        col_mapping = {
            'posted date': 'date',
            'transaction date': 'date',
            'merchant': 'description',
            'description': 'description',
            'debit': 'amount',
            'credit': 'amount',
            'amount': 'amount'
        }

        df = df.rename(columns=col_mapping)

        # Convert date to datetime
        df['date'] = pd.to_datetime(df['date'])

        # Clean amount (remove $, convert to float, make negative for debits)
        df['amount'] = df['amount'].astype(
            str).str.replace('$', '').str.replace(',', '')
        df['amount'] = pd.to_numeric(df['amount'], errors='coerce')

        # Filter out null amounts
        df = df.dropna(subset=['amount'])

        # Sort by date (newest first)
        df = df.sort_values('date', ascending=False)

        return df[['date', 'description', 'amount']]

    except Exception as e:
        print(f"Error parsing CSV: {e}")
        raise
