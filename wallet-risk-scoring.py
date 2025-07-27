import csv
import random

def generate_score(wallet_address):
    # Replace this with your actual logic if needed
    return random.randint(100, 1000)

input_file = 'wallets.csv'
output_file = 'wallet_risk_scores.csv'

wallet_scores = []

# Step 1: Read wallet addresses from CSV
with open(input_file, mode='r', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        wallet_id = row.get('wallet_id')
        if wallet_id:
            score = generate_score(wallet_id)
            wallet_scores.append({'wallet_id': wallet_id, 'score': score})

# Step 2: Write scores to new CSV
with open(output_file, mode='w', newline='') as csvfile:
    fieldnames = ['wallet_id', 'score']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(wallet_scores)

print(f"Scoring completed. Results saved to '{output_file}'")
