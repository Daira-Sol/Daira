# tests/test_wallet_analysis.py

from modules.wallet_analysis import analyze_wallet

def test_analyze_wallet():
    wallet_data = analyze_wallet("TestWallet123")
    assert wallet_data["address"] == "TestWallet123"
    assert "transactions" in wallet_data
