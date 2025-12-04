import pandas as pd
from pathlib import Path

def load_csv(filename="energy_data_big.csv"):
    csv_path = Path(filename)

    if not csv_path.exists():
        print(f"❌ ERROR: {filename} not found in this folder!")
        return None

    print(f"Reading {filename} ...")
    df = pd.read_csv(csv_path, on_bad_lines="skip")

    # Convert timestamp
    df["timestamp"] = pd.to_datetime(df["timestamp"], errors="coerce")
    df.dropna(subset=["timestamp"], inplace=True)

    # Ensure building + month exist
    if "building" not in df.columns:
        df["building"] = "Unknown_Building"

    if "month" not in df.columns:
        df["month"] = df["timestamp"].dt.month

    df.sort_values("timestamp", inplace=True)
    print("✅ CSV loaded successfully!")
    print(df.head())

    return df


if __name__ == "__main__":
    load_csv()
