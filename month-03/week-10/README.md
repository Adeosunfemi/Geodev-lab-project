# Week 10: GeoPandas, Layers as Tables

## Overview

This week, I explored GeoPandas using both the provided practice datasets and data from my existing Ibadan North GIS project.

I also learned how to inspect datasets, create point layers, clean attributes, join tables and produce maps.

## Tasks Completed

- Explored tabular data using Pandas.
- Filtered and sorted datasets.
- Inspected vector layers and their geometry types.
- Examined geometry properties.
- Converted CSV coordinate data into point features.
- Cleaned health facility types by standardising PHC and Primary Health Centre into one category.
- Joined ward information with population data.
- Cleaned ward names to improve matching during the join.
- Created maps using GeoPandas and Matplotlib.
- Saved processed outputs.

## Challenge Scripts and Data Sources

### 1. my_explore.py

Used my existing Ibadan North GIS project data to inspect the boundary GeoPackage. Checked its layers, records, geometry type, CRS and spatial bounds.

### 2. my_points.py

Used the `health_facilities.csv` dataset provided in the learning materials because the required dataset for this exercise was not available in my existing GIS project. I converted longitude and latitude coordinates into point geometries using EPSG:4326, standardised facility types and saved the result as `facilities.gpkg`.

### 3. my_join.py

Used the ward and population datasets provided in the learning materials because I could not locate the preferred layer needed for the joining exercise in my existing GIS project.

I performed an initial join, checked the matching records, cleaned the ward names and repeated the join. This improved the matching result from 9 out of 12 wards to 12 out of 12 wards.

### 4. my_map.py

Used my existing Ibadan North GIS project data, including the LGA boundary and 50 m waterways buffer, to create a map using GeoPandas and Matplotlib.

## Outputs

- `facilities_map.png`
- `wards_table.csv`
- `my_map.png`

## Learning Outcomes

I improved my understanding of GeoPandas, data exploration, geometry inspection, coordinate conversion, attribute cleaning, table joining and map visualisation.

I also gained practical experience working with both supplied practice datasets and data from my existing GIS project.
