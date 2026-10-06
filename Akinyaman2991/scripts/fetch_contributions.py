import json
import os

# Basit bir örnek veri oluşturucu (GitHub API entegrasyonu yerine yerel veri akışı)
def fetch_data():
    os.makedirs("data", exist_ok=True)
    mock_data = {"status": "active", "contributions": 1250}
    with open("data/contributions.json", "w") as f:
        json.dump(mock_data, f)
    print("Katkı verileri çekildi.")

if __name__ == "__main__":
    fetch_data()