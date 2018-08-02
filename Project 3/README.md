# Project 3 - Creating Some Data Science Notebooks

## Goal: Apply your knowledge of the ArcGIS Python API and web services
## Asssigned: Week 8
## Due: Week 11

Create two Python Notebooks that answer the following questions. Please use the notebook to explain your steps.
## 1. Missouri Demographic Study
Using Esri's [USA Tapestry Service for Counties](http://services.arcgis.com/P3ePLMYs2RVChkJx/arcgis/rest/services/Tapestry_Households/FeatureServer/1), create a Python Notebook that answers the following questions
1. For the counties in Missouri only, what is the dominant Tapestry LifeMode Group Name(*TLIFENAME*)?
2. Create a histrogram that shows the number of Missouri counties per Tapestry LifeMode Group Name(*TLIFENAME*)
3. Create a pie chart that shows the number of Missouri counties per Tapestry LifeMode Group Name(*TLIFENAME*)
4. For the counties in Missouri, what is the dominant Dominant Tapestry Segment Name (*TSEGNAME*)
5. Create a histogram  that shows the number of Missouri counties per Tapestry Segment Name (*TSEGNAME*).
6. Create a pie chart that shows the number of Missouri counties per Tapestry Segment Name (*TSEGNAME*).
7. Is there Any correlation between LifeMode Group and Segment name? *Hint: plot TSEGNAME' vs. TLIFENAME.*
8 **Bonus** Explore the data and show me somethig cool that I haven't thought of.


**Helpful Hint**
You can return only Missouri data from the feature service query by usring a geometry filter. See the example here:
```
from arcgis.geometry import filters
import arcpy

fc = r'C:\PROJECTS\STATE_OF_THE_DATA\DATA\usa_states\usa.gdb\nj'

grid_desc = arcpy.Describe(fc)
grid_sr = grid_desc.spatialReference
grid_extent = grid_desc.extent

geometry = grid_extent
sr = grid_sr
sp_rel = "esriSpatialRelIntersects"
sp_filter = filters.intersects(geometry=geometry)

fl.query(geometry_filter=sp_filter, return_all_records=True).df
```

## 2. 