# campus-energy-dashboard-nisha

A structured Python-based data analytics project to ingest, clean, model, visualize, and summarize electricity usage across multiple campus buildings.

 Objective

The objective of this project is to develop a complete data-processing pipeline for analyzing electricity consumption across campus buildings.
This system:

Automatically loads and validates energy meter data

Cleans and aggregates hourly/daily/weekly usage

Uses OOP classes to model buildings and readings

Generates visual dashboards with Matplotlib

Exports processed results and a written executive summary

The goal is to provide actionable insights into campus-wide energy usage patterns.

This project follows a 5-stage analytical pipeline:

1️. Data Ingestion & Validation

Read the CSV file using pandas.read_csv().

Validate timestamps, check column consistency.

Convert timestamp column to datetime format.

Handle corrupt/missing data using:

on_bad_lines='skip'

NaN removal or interpolation

2. Core Aggregation Logic

Using Pandas features:

Daily totals via .resample('D')

Weekly averages via .resample('W')

Building-wise summaries using .groupby('Building')

Additional metrics generated:

3. Total consumption

Mean/min/max usage

Peak-hour usage

Object-Oriented Modeling

Three classes were created:

Building

Holds building metadata and a list of meter readings.

MeterReading

Represents a single timestamped kWh value.

BuildingManager

Loads data, creates Building objects, and generates reports.

This modular design improves scalability and reusability.

4️. Visual Dashboard (Matplotlib)

A combined Matplotlib dashboard contains:

Trend Line – Daily consumption over time

Bar Chart – Weekly average comparison

Scatter Plot – Peak-hour consumption pattern

5. The summary includes:

Total campus consumption

Highest-consuming building

Peak load hour

Notes from daily & weekly trends



📈 Insights & Key Findings

Based on the processed dataset:

Hostel buildings typically show higher evening-hour consumption.

Lab Block shows irregular spikes due to equipment usage.

Admin building maintains stable weekday-only electricity patterns.

Peak load hours are commonly between 7 PM – 10 PM.

Weekly trends show reduced usage on weekends across all buildings.

These insights help identify:

Opportunities for demand-side management

Buildings with abnormal or excessive consumption

Time slots where load shifting could reduce energy bills



🏁 Conclusion

This project demonstrates a full end-to-end analytical workflow—from raw ingestion to dashboard visualization and executive reporting.
It provides a robust foundation for real-world utility monitoring, sustainability planning, and smart-campus energy management.
