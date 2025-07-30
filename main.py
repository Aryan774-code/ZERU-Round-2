import csv
from aave_utils import fetch_aave_data, calculate_risk_score

input_file = "input_wallets.csv"
output_file = "output_scores.csv"

with open(input_file, "r") as infile, open(output_file, "w", newline="") as outfile:
    reader = csv.DictReader(infile)
    writer = csv.writer(outfile)
    writer.writerow(["wallet_id", "score"])

    for row in reader:
        wallet = row["wallet_id"]
        try:
            data = fetch_aave_data(wallet)
            if data:
                score = calculate_risk_score(data["healthFactor"])
            else:
                score = 1000  # Unknown / Not active on Aave
        except Exception as e:
            print(f"Error for {wallet}: {e}")
            score = 1000

        writer.writerow([wallet, score])
        print(f"Processed {wallet} → Score: {score}")
