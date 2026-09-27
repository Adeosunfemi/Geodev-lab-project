#### **Research Question:**



###### Which areas in Ibadan North LGA have steep slopes, and where are they located?





#### **Operation Carried Out:**



###### These operations were carried out in a logical sequence to prepare and analyze the study area. First, the datasets were validated by visually inspecting the layers on the map, reviewing the attribute tables, manually checking individual features, and checking for empty or invalid geometries. No missing or invalid features were identified. Then the relevant layers were then Reprojected to EPSG:32631 to ensure consistency and accurate measurements in meters. The processed datasets were saved in GeoPackage format for organized data management. The DEM was subsequently clipped to the Ibadan North LGA boundary to focus the analysis on the study area and classified to visualize elevation differences. A 50 m buffer was also created around waterways to identify areas close to watercourses. These processed layers were then combined and visualized in QGIS to produce a map showing the spatial distribution of elevation, waterways, and their surrounding buffer. The map was designed with appropriate symbology, labels, grid coordinates, and a scale bar to improve interpretation and presentation.





#### **Expected vs Actual Outcome:**



###### At the beginning, I expected to simply display the Ibadan North LGA boundary together with the mapped waterways. However, as the project progressed, I introduced a DEM dataset, which added elevation information to the map. This made the map more visual, meaningful, and useful for further terrain analysis, especially for identifying areas with different elevation and slope characteristics.



#### **Unexpected Map Outcome** 



###### What surprised me was the outcome of the map. I initially expected a simple map showing the Ibadan North boundary and waterways, but adding the DEM made the final map much more detailed and visually appealing. It also revealed elevation patterns that I had not expected to see, giving the project more meaning and a clearer direction for further analysis.





<img width="17716" height="11811" alt="Waterway Buffer (50 m)" src="https://github.com/user-attachments/assets/b64ceacf-bb9a-446c-8c61-2feb3a1d9817" />



#### **Additional Data Required For Further Analysis** 



###### The main data I still need is additional terrain and environmental data that can support the analysis of steep-slope areas. The datasets already obtained from OpenStreetMap, including roads, buildings, waterways, land use, and settlements, can be used for the next stage of the analysis.





