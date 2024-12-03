# src/main.py

from modules.wallet_analysis import analyze_wallet
from modules.sentiment import analyze_sentiment
from modules.solana_data import fetch_solana_data

def main():
    print("Welcome to DAIRA-CBI: Crypto Behavior Intelligence!")
    
    # Example: Analyze a wallet
    wallet_address = "YourSolanaWalletAddressHere"
    wallet_data = analyze_wallet(wallet_address)
    print("Wallet Analysis:", wallet_data)

    # Example: Fetch Solana data
    solana_stats = fetch_solana_data()
    print("Solana Data:", solana_stats)

    # Example: Analyze sentiment
    topic = "Solana"
    sentiment = analyze_sentiment(topic)
    print("Social Sentiment:", sentiment)

if __name__ == "__main__":
    main()
