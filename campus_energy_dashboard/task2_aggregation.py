import pandas as pd

def calculate_daily_totals(df):
    return df.resample("D", on="timestamp")["kwh"].sum()

def calculate_weekly_totals(df):
    return df.resample("W", on="timestamp")["kwh"].sum()

def building_summary(df):
    return df.groupby("building")["kwh"].agg(["mean", "min", "max", "sum"])


# For testing
if __name__ == "__main__":
    from task1_ingestion import load_csv
    df = load_csv()


    daily = calculate_daily_totals(df)
    weekly = calculate_weekly_totals(df)
    summary = building_summary(df)

    print("\nDaily Totals:\n", daily)
    print("\nWeekly Totals:\n", weekly)
    print("\nBuilding Summary:\n", summary)
