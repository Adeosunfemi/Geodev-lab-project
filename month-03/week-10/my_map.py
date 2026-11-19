import geopandas as gpd
import matplotlib.pyplot as plt

# Load the datasets
boundary = gpd.read_file(
    "My-Project/Data-/Processed_Data/Ibadan_North_bound.gpkg"
)

waterways_buffer = gpd.read_file(
    "My-Project/Data-/Processed_Data/Ibadan_North_Waterways_Buffer_50m.gpkg"
)

# Create the map
fig, ax = plt.subplots(figsize=(8, 8))

# Plot the boundary
boundary.plot(
    ax=ax,
    color="#F2F2F2",
    edgecolor="#333333"
)

# Plot the waterways
waterways_buffer.plot(
    ax=ax,
    color="#4AADD8",
    edgecolor="#1676A3"
)

# Map title
ax.set_title("Ibadan North LGA Waterways 50 m Buffer Analysis")

# Remove axes
ax.set_axis_off()

# Save the map
fig.savefig(
    "month-03/week-10/my_map.png",
    dpi=150,
    bbox_inches="tight"
)

print("Map saved successfully!")