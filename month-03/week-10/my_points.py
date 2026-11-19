import pandas as pd
import geopandas as gpd
table = pd.read_csv("data/raw/health_facilities.csv")
print(table.head(3))

facilities = gpd.GeoDataFrame(
    table,
    geometry=gpd.points_from_xy(table["longitude"], table["latitude"]),
    crs="EPSG:4326",
)
print(facilities.head(3))
print(facilities.crs)
table["type"] = table["type"].replace({
    "PHC": "Primary Health Centre"
})
print(table["type"].value_counts())

facilities["type"] = table["type"]

print(facilities["type"].value_counts())

facilities.to_file("data/processed/facilities.gpkg", layer="facilities")
print("saved", len(facilities), "facilities")
