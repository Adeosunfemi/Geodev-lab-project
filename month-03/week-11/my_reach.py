
import geopandas as gpd

# 1. Load the datasets
boundary = gpd.read_file(
    "My-Project/Data-/Processed_Data/Ibadan_North_bound.gpkg",
    layer="ibadan_north_boundary_"
)

place = gpd.read_file(
    "My-Project/Data-/Processed_Data/place.gpkg"
)

buffer = gpd.read_file(
    "My-Project/Data-/Processed_Data/Ibadan_North_Waterways_Buffer_50m.gpkg"
)

# 2. Ensure all layers use the same CRS
place = place.to_crs(boundary.crs)
buffer = buffer.to_crs(boundary.crs)

# 3. Clip data to Ibadan North
place = gpd.clip(place, boundary)
buffer = gpd.clip(buffer, boundary)

# 4. Reset indexes
place = place.reset_index(drop=True)
buffer = buffer.reset_index(drop=True)

print("Place points:", len(place))
print("Buffer polygons:", len(buffer))

# 5. Find points covered by the buffer polygons
joined = gpd.sjoin(
    place,
    buffer,
    how="left",
    predicate="within"
)

# 6. Identify points outside all buffers
matched_indexes = joined.index[
    joined["index_right"].notna()
].unique()

outside = place.loc[
    ~place.index.isin(matched_indexes)
].copy()

print("\nPoints outside buffers:", len(outside))
print("Points inside buffers:", len(place) - len(outside))

# 7. Find the nearest buffer for each uncovered point
nearest = gpd.sjoin_nearest(
    outside,
    buffer,
    how="left",
    distance_col="distance_m"
)

# 8. Display nearest buffer distances
print("\nNearest buffer distances:")
print(nearest[["distance_m"]])

print("\nDistance summary:")
print(nearest["distance_m"].describe())

# 9. Save nearest-distance results
nearest.to_file(
    "My-Project/Data-/Processed_Data/nearest_buffer_distances.gpkg",
    driver="GPKG"
)

print("\nNearest-distance analysis saved successfully!")

import matplotlib.pyplot as plt

# 10. Identify covered points
inside = place.loc[
    place.index.isin(matched_indexes)
].copy()

# 11. Create coverage-gap map
fig, ax = plt.subplots(figsize=(10, 10))

boundary.plot(
    ax=ax,
    facecolor="none",
    edgecolor="black",
    linewidth=1
)

buffer.plot(
    ax=ax,
    facecolor="lightblue",
    edgecolor="steelblue",
    alpha=0.5
)

inside.plot(
    ax=ax,
    color="green",
    markersize=40,
    label="Covered points"
)

outside.plot(
    ax=ax,
    color="red",
    markersize=40,
    label="Uncovered points"
)

ax.set_title(
    "Waterway Buffer Coverage Gap Analysis\nIbadan North LGA"
)

ax.legend()
ax.set_axis_off()

plt.savefig(
    "month-03/week-11/my_reach_map.png",
    dpi=200,
    bbox_inches="tight"
)

plt.close()

print("\nCoverage-gap map saved successfully!")
