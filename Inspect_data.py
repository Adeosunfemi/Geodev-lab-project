
    #Turn it into a function that returns
import csv

def inspect_column(filename, column):
    with open(filename, encoding="utf-8-sig") as f:
        rows = list(csv.DictReader(f))
        values = []
        for row in rows:
            raw = row[column].strip()
            if raw == "":
                continue
            values.append(float(raw))
            return{
                "smallest": min(values),
                "largest": max(values),
                "count": len(values),
            }
        result = inspect_column("waterways_buffer_50m.csv", "area_km2")
        print(result)

       #use your function twice
area_result = inspect_column("waterways_buffer_50m.csv", "area_km2")
count_result = inspect_column("waterways_buffer_50m.csv", "Count")

print("Area:", area_result)
print("Count:",count_result)