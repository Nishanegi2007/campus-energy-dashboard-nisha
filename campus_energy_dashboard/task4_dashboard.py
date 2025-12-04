import matplotlib.pyplot as plt
import pandas as pd
from task1_ingestion import load_csv
from task2_aggregation import calculate_daily_totals

def create_dashboard(df, output_path="output/dashboard.png"):
    fig, axes = plt.subplots(3, 1, figsize=(12, 18))

    # 1. Daily trend line
    for b, subdf in df.groupby("building"):
        daily = subdf.resample("D", on="timestamp")["kwh"].sum()
        axes[0].plot(daily, label=b)

    axes[0].set_title("Daily Electricity Consumption")
    axes[0].legend()

    # 2. Weekly bar chart
    weekly = df.groupby("building").resample("W", on="timestamp")["kwh"].mean()
    weekly_avg = weekly.groupby("building").mean()

    axes[1].bar(weekly_avg.index, weekly_avg.values)
    axes[1].set_title("Average Weekly Electricity Usage")

    # 3. Scatter plot (hour vs kWh)
    df["hour"] = df["timestamp"].dt.hour
    axes[2].scatter(df["hour"], df["kwh"], alpha=0.6)
    axes[2].set_title("Peak-Hour Consumption")

    plt.tight_layout()
    plt.savefig(output_path)
    plt.close()
    print("📊 Dashboard saved to", output_path)


if __name__ == "__main__":
    df = load_csv()
    create_dashboard(df)
