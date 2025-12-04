import pandas as pd
from task1_ingestion import load_csv
from task2_aggregation import calculate_daily_totals, calculate_weekly_totals, building_summary
from pathlib import Path

def export_results(df, output_dir="output"):
    out = Path(output_dir)
    out.mkdir(exist_ok=True)

    # Export CSVs
    df.to_csv(out / "cleaned_energy_data.csv", index=False)
    summary = building_summary(df)
    summary.to_csv(out / "building_summary.csv")

    # Summary text
    daily = calculate_daily_totals(df)
    weekly = calculate_weekly_totals(df)

    summary_text = f"""
=== EXECUTIVE SUMMARY ===

Total Campus Consumption: {df['kwh'].sum():.2f} kWh

Highest Consuming Building: {summary['sum'].idxmax()} 
Total: {summary['sum'].max():.2f} kWh

Peak Load Timestamp: {df.loc[df['kwh'].idxmax(), 'timestamp']}

Daily Trend: Min={daily.min():.2f} kWh | Max={daily.max():.2f} kWh
Weekly Trend: Min={weekly.min():.2f} kWh | Max={weekly.max():.2f} kWh
"""

    with open(out / "summary.txt", "w") as f:
        f.write(summary_text)

    print("📁 Data exported successfully.")


if __name__ == "__main__":
    df = load_csv()
    export_results(df)
