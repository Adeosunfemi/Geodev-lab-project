
import geopandas as gpd
import matplotlib.pyplot as plt

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

# 2. Make sure all layers use the same CRS
place = place.to_crs(boundary.crs)
buffer = buffer.to_crs(boundary.crs)

print("Boundary CRS:", boundary.crs)
print("Place CRS:", place.crs)
print("Buffer CRS:", buffer.crs)

# 3. Restrict the analysis to Ibadan North LGA
place = gpd.clip(place, boundary)
buffer = gpd.clip(buffer, boundary)

# Reset indexes for reliable counting
place = place.reset_index(drop=True)
buffer = buffer.reset_index(drop=True)

print("\nPoints inside Ibadan North:", len(place))
print("Buffer features:", len(buffer))

# 4. Spatial join: find points inside each buffer
joined = gpd.sjoin(
    place,
    buffer,
    how="inner",
    predicate="within"
)

print("\nPoint-to-buffer matches:", len(joined))
print("Unique points inside buffers:", joined.index.nunique())

# 5. Count points in each buffer
counts = (
    joined.groupby("index_right")
    .size()
    .rename("point_count")
)

# 6. Add counts to all buffer polygons
buffer = buffer.merge(
    counts,
    left_index=True,
    right_index=True,
    how="left"
)

buffer["point_count"] = (
    buffer["point_count"].fillna(0).astype(int)
)

# 7. Print counting results
print("\n--- POINT COUNT RESULTS ---")
print("Total points inside LGA:", len(place))
print("Unique points inside buffers:", joined.index.nunique())
print("Point-to-buffer matches:", len(joined))
print("Buffers with zero points:", (buffer["point_count"] == 0).sum())
print("Total point counts:", buffer["point_count"].sum())

# 8. Save the buffer point-count results
buffer.to_file(
    "My-Project/Data-/Processed_Data/buffer_point_counts.gpkg",
    driver="GPKG"
)

# 9. Create the map
fig, ax = plt.subplots(figsize=(10, 10))

boundary.plot(
    ax=ax,
    facecolor="none",
    edgecolor="black",
    linewidth=1
)

buffer.plot(
    ax=ax,
    column="point_count",
    cmap="Blues",
    edgecolor="steelblue",
    linewidth=0.3,
    legend=True,
    legend_kwds={"label": "Number of place points"}
)

place.plot(
    ax=ax,
    color="darkorange",
    markersize=40,
    label="Place points"
)

ax.set_title(
    "Place Point Count Within 50 m Waterway Buffers\nIbadan North LGA"
)

ax.legend()
ax.set_axis_off()

plt.savefig(
    "month-03/week-11/my_count_map.png",
    dpi=200,
    bbox_inches="tight"
)

plt.close()

print("\nPoint counting completed successfully!")
