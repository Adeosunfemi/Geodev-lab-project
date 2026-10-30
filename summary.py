import csv

def read_rows(filename):
    with open(filename, encoding="utf-8-sig") as f:
        return list(csv.DictReader(f))

def clean_values(rows, column):
    values = []
    for row in rows:
        raw = row[column].strip()
        if raw == "":
            continue
        values.append(float(raw))
    return values

def summaries(values):
    if len(values) == 0:
        return {"Count": 0, "smallest": None, "largest": None, "average": None}
    return{
        "Count": len(values),
        "smallest": min(values),
        "largest": max(values),
        "average": sum(values) / len(values),
    }

rows = read_rows("waterways_buffer_50m.csv")
values = clean_values(rows, "area_km2")
result = summaries(values)
print(result)

def summaries_all(filename, columns):
    rows = read_rows(filename)
    report = {}

    for column in columns:
        values = clean_values(rows, column)
        report[column] = summaries(values)
    return report

report = summaries_all("waterways_buffer_50m.csv", ["area_km2", "Count"])

for column, stats in report.items():
    print(column, "->", stats)