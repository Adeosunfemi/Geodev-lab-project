
import geopandas as gpd

# 1. Load the datasets
boundary = gpd.read_file(
    "My-Project/Data-/Processed_Data/Ibadan_North_bound.gpkg",
    layer="ibadan_north_boundary_"
)

buffer = gpd.read_file(
    "My-Project/Data-/Processed_Data/Ibadan_North_Waterways_Buffer_50m.gpkg"
)

# 2. Check geometry validity before fixing
print("Invalid boundary geometries before:")
print((~boundary.geometry.is_valid).sum())

print("\nInvalid buffer geometries before:")
print((~buffer.geometry.is_valid).sum())

# 3. Repair invalid geometries
boundary["geometry"] = boundary.geometry.make_valid()
buffer["geometry"] = buffer.geometry.make_valid()

# 4. Check validity after fixing
print("\nInvalid boundary geometries after:")
print((~boundary.geometry.is_valid).sum())

print("\nInvalid buffer geometries after:")
print((~buffer.geometry.is_valid).sum())

# 5. Save validated datasets
boundary.to_file(
    "My-Project/Data-/Processed_Data/validated_boundary.gpkg",
    driver="GPKG"
)

buffer.to_file(
    "My-Project/Data-/Processed_Data/validated_buffers.gpkg",
    driver="GPKG"
)

print("\nValidated datasets saved successfully!")
