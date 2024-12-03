# tests/test_solana_data.py

from modules.solana_data import fetch_solana_data

def test_fetch_solana_data():
    """
    Test to validate fetch_solana_data function returns valid Solana data.
    """
    solana_data = fetch_solana_data()
    
    # Ensure the returned data is a dictionary
    assert isinstance(solana_data, dict), "Data should be a dictionary"

    # Check if required keys are present
    assert "network_status" in solana_data, "Missing 'network_status' key"
    assert "average_transaction_cost" in solana_data, "Missing 'average_transaction_cost' key"
    assert "latest_block" in solana_data, "Missing 'latest_block' key"

    # Validate the values (example checks)
    assert solana_data["network_status"] in ["Healthy", "Degraded", "Offline"], "Invalid network status"
    assert isinstance(solana_data["average_transaction_cost"], str), "Transaction cost should be a string"
    assert isinstance(solana_data["latest_block"], int), "Latest block should be an integer"

# If you want to run this script directly for testing:
if __name__ == "__main__":
    test_fetch_solana_data()
    print("All tests passed for fetch_solana_data!")
