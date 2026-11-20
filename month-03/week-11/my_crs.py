import geopandas as gpd

boundary = gpd.read_file(
    "My-Project/Data-/Processed_Data/Ibadan_North_bound.gpkg"
)

buffer = gpd.read_file(
    "My-Project/Data-/Processed_Data/Ibadan_North_Waterways_Buffer_50m.gpkg"
)

print("Boundary CRS:", boundary.crs)
print("Buffer CRS:", buffer.crs)

print("Estimated UTM CRS:", boundary.estimate_utm_crs())

# Reproject both layers to the estimated UTM CRS
target_crs = boundary.estimate_utm_crs()

boundary_utm = boundary.to_crs(target_crs)
buffer_utm = buffer.to_crs(target_crs)

# Calculate area in square kilometres
boundary_utm["area_km2"] = boundary_utm.geometry.area / 1_000_000
buffer_utm["area_km2"] = buffer_utm.geometry.area / 1_000_000

# Print total areas
print("Boundary area (km²):", boundary_utm["area_km2"].sum())
print("Buffer area (km²):", buffer_utm["area_km2"].sum())