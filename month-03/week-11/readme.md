You don't have to include a separate **Project** line, but I recommend it. The Week 11 heading tells readers what you studied, while the project title tells them what you worked on.

Here is the full README with both included.

# Week 11: Coordinate Reference Systems and Spatial Operations in Code

## Project: Ibadan North LGA Waterways 50 m Buffer Analysis

### Overview

This week, I worked with my own GIS project data using GeoPandas. The tasks focused on coordinate reference systems, spatial joins, point counting, nearest-distance analysis, and geometry validation.

### 1. Coordinate Reference Systems (`my_crs.py`)

I checked the CRS of my boundary and buffer layers and used `estimate_utm_crs()` to identify a suitable projected coordinate system.

- **Selected CRS:** EPSG:32631 – WGS 84 / UTM Zone 31N.
- **Reason:** This is the estimated UTM CRS for my study area. It uses metres, making it suitable for calculating areas and measuring distances.

The calculated area of Ibadan North LGA is approximately **38.91 km²**.

### 2. Point Counting (`my_count.py`)

I used `sjoin()` and `groupby()` to count place points within the 50 m waterway buffer polygons. I then merged the counts back to the buffer layer so that polygons without points were also included with a count of zero.

**Results:**

- Total place points within Ibadan North: 9
- Total buffer polygons: 112
- Unique points inside buffers: 2
- Total point-to-buffer matches: 3
- Buffers with zero points: 109
- Total point counts: 3

One point matched more than one buffer polygon, which explains why there were 3 matches but only 2 unique points.

### 3. Nearest Distance Analysis (`my_reach.py`)

I used `sjoin_nearest()` to find the nearest waterway buffer for each place point that was outside all the buffer polygons.

**Results:**

- Points outside the buffers: 7
- Points inside the buffers: 2
- Minimum distance: 12.59 m
- Maximum distance: 464.87 m
- Mean distance: 208.39 m
- Median distance: 120.52 m

I chose the nearest-distance method because it helps show how far uncovered place points are from the nearest 50 m waterway buffer.

### 4. Geometry Validation (`my_validity.py`)

I checked the validity of the Ibadan North boundary and waterway buffer geometries using `is_valid`. I also applied `make_valid()` and checked them again.

**Results:**

| Geometry | Invalid Before | Invalid After |
| -------- | -------------- | ------------- |
| Boundary | 0              | 0             |
| Buffer   | 0              | 0             |

**No invalid geometries were found.** All geometries were valid before and after the validation process.

### 5. Outputs

The analysis produced the following files.

**Processed data:**

- `buffer_point_counts.gpkg`
- `nearest_buffer_distances.gpkg`
- `validated_boundary.gpkg`
- `validated_buffers.gpkg`

**Maps:**

- `my_count_map.png`
- `my_reach_map.png`

### 6. Method Limitation

One limitation of this analysis is that the place dataset contains only 9 mapped points within Ibadan North, so the results may not represent every place in the LGA. Also, `sjoin_nearest()` measures straight-line distance to the nearest buffer, not actual travel distance along roads. Since the buffer polygons were kept separate, overlapping buffers can cause one point to be counted more than once.

### Conclusion

This week's exercise helped me practise CRS selection, spatial joins, point counting, nearest-distance analysis, and geometry validation using GeoPandas. It also improved my understanding of how spatial analysis can be used to examine the relationship between mapped places and nearby waterways.
