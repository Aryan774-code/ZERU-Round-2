# wallet_utils.py

import pandas as pd

def fetch_wallet_data(wallet_address, csv_file='wallets.csv'):
    """
    Fetch data for a given wallet address from a CSV file.

    Parameters:
    wallet_address (str): The wallet address to search for.
    csv_file (str): Path to the CSV file.

    Returns:
    dict or None: Data for the wallet if found.
    """
    try:
        df = pd.read_csv(csv_file)
        wallet_data = df[df['wallet_id'] == wallet_id]

        if wallet_data.empty:
            return None

        return wallet_data.to_dict(orient='records')[0]

    except FileNotFoundError:
        print(f"Error: {csv_file} not found.")
        return None
    except Exception as e:
        print(f"Unexpected error: {e}")
        return None
