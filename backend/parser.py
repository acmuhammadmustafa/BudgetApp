import pandas as pd
from io import StringIO, BytesIO


def parse_bofa_csv(file_content):
    """
    Parse Bank of America CSV export
    Handles both simple format and format with summary header section.
    Expected columns: Date, Description, Amount (or similar variations)
    """
    try:
        # Handle both bytes and string content
        if isinstance(file_content, bytes):
            file_content = file_content.decode('utf-8')

        # BofA often includes a summary section at the top, so we need to find
        # where the actual transaction data starts
        lines = file_content.split('\n')

        # Find the line with "Date" header for actual transactions
        data_start_idx = 0
        for i, line in enumerate(lines):
            if line.strip().startswith('Date') and 'Description' in line:
                data_start_idx = i
                break

        # Reconstruct CSV starting from transaction data
        csv_data = '\n'.join(lines[data_start_idx:])

        # Read CSV
        df = pd.read_csv(StringIO(csv_data))

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
            'amount': 'amount',
            'running bal.': 'running_bal'  # Ignore running balance column
        }

        df = df.rename(columns=col_mapping)

        # Drop unnecessary columns
        df = df[['date', 'description', 'amount']]

        # Convert date to datetime
        df['date'] = pd.to_datetime(df['date'], errors='coerce')

        # Remove rows where date conversion failed
        df = df.dropna(subset=['date'])

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
