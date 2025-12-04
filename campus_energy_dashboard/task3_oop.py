class MeterReading:
    def __init__(self, timestamp, kwh):
        self.timestamp = timestamp
        self.kwh = kwh


class Building:
    def __init__(self, name):
        self.name = name
        self.meter_readings = []

    def add_reading(self, timestamp, kwh):
        self.meter_readings.append(MeterReading(timestamp, kwh))

    def total_consumption(self):
        return sum(r.kwh for r in self.meter_readings)

    def generate_report(self):
        return {
            "building": self.name,
            "readings": len(self.meter_readings),
            "total_kwh": self.total_consumption(),
        }


class BuildingManager:
    def __init__(self):
        self.buildings = {}

    def load_from_dataframe(self, df):
        for _, row in df.iterrows():
            name = row["building"]
            if name not in self.buildings:
                self.buildings[name] = Building(name)
            self.buildings[name].add_reading(row["timestamp"], row["kwh"])

    def generate_all_reports(self):
        return {name: b.generate_report() for name, b in self.buildings.items()}


# Testing module
if __name__ == "__main__":
    import pandas as pd
    from task1_ingestion import load_csv
    df = load_csv()

    from task3_oop import BuildingManager

    manager = BuildingManager()
    manager.load_from_dataframe(df)
    print(manager.generate_all_reports())
