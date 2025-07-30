import requests

AAVE_V2_SUBGRAPH_URL = "https://api.thegraph.com/subgraphs/name/aave/protocol-v2"

def fetch_aave_data(wallet_address):
    query = """
    {
      user(id: "%s") {
        id
        healthFactor
        totalCollateralETH
        totalBorrowsETH
      }
    }
    """ % wallet_address.lower()

    response = requests.post(AAVE_V2_SUBGRAPH_URL, json={"query": query})
    data = response.json()

    user_data = data.get("data", {}).get("user")
    if not user_data:
        return None  # Wallet not found

    return {
        "healthFactor": float(user_data["healthFactor"]) / 1e18 if user_data["healthFactor"] else 0.0,
        "collateral": float(user_data["totalCollateralETH"]) / 1e18,
        "borrowed": float(user_data["totalBorrowsETH"]) / 1e18
    }

def calculate_risk_score(health_factor):
    if health_factor == 0.0:
        return 300  # No activity
    elif health_factor < 1.0:
        return 900  # Very high risk (liquidatable)
    elif health_factor < 1.5:
        return 700  # Medium risk
    elif health_factor < 2.0:
        return 500  # Low risk
    else:
        return 300  # Very low risk
