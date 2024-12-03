Describe DAIRA’s new focus on Solana and behavioral intelligence.
Include usage instructions for running Solana-specific modules.

**Implement Solana Wallet Data Fetching (solana_data.py):**
from solana.rpc.api import Client

# Initialize Solana Client
client = Client("https://api.mainnet-beta.solana.com")

def get_wallet_history(wallet_address):
    response = client.get_confirmed_signature_for_address2(wallet_address, limit=100)
    return response['result']

**Build Wallet Behavior Analysis (wallet_analysis.py):**

  def classify_wallet(wallet_history):
    # Analyze transactions to determine wallet type
    if len(wallet_history) > 100:
        return "Frequent Trader"
    elif all(tx['amount'] > 1000 for tx in wallet_history):
        return "Whale"
    else:
        return "HODLer"

        

