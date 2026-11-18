import geopandas as gpd

print(gpd.list_layers("My-Project/data-/Processed_Data/Ibadan_North_bound.gpkg"))

bound = gpd.read_file("My-Project/data-/Processed_Data/Ibadan_North_bound.gpkg",  layer="ibadan_north_boundary_")

print(bound.head())
print("Rows and columns:", bound.shape)
print(bound.geom_type.value_counts())
print("CRS:", bound.crs)
print("Bounds:", bound.total_bounds)