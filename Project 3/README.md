# Project 3 - Creating Some Data Science Notebooks

## Goal: Apply your knowledge of the ArcGIS Python API and web services
## Asssigned: Week 8
## Due: Week 11
## Score: Out of 100 points. Anything exceeding 100 points is a A+!

Create two Python Notebooks that answer the following questions. Please use the notebook to explain your steps.
## 1. Missouri Demographic Study
Using Esri's [USA Tapestry Service for Counties](http://services.arcgis.com/P3ePLMYs2RVChkJx/arcgis/rest/services/Tapestry_Households/FeatureServer/1), create a Python Notebook that answers the following questions
1. For the counties in Missouri only, what is the dominant Tapestry LifeMode Group Name(*TLIFENAME*)? (**10 points**)
2. Create a histrogram that shows the number of Missouri counties per Tapestry LifeMode Group Name(*TLIFENAME*) (**5 points**)
3. Create a pie chart that shows the number of Missouri counties per Tapestry LifeMode Group Name(*TLIFENAME*) (**5 points**)
4. For the counties in Missouri, what is the dominant Dominant Tapestry Segment Name (*TSEGNAME*) (**10 points**)
5. Create a histogram  that shows the number of Missouri counties per Tapestry Segment Name (*TSEGNAME*). (**5 points**)
6. Create a pie chart that shows the number of Missouri counties per Tapestry Segment Name (*TSEGNAME*). (**5 points**)
7. Is there Any correlation between LifeMode Group and Segment name? *Hint: plot TSEGNAME' vs. TLIFENAME.* (**2 points**)
8. Make sure the notebook is well-documented. (**8 points**)
9. **Bonus** Explore the data and show me somethig cool that I haven't thought of. (**5 Points**)


### Helpful Hint
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

## 2. Earthquake Impact Assessment
The USGS tracks [global earthquake activity](https://earthquake.usgs.gov/earthquakes/map/). For this project, I want you to estimate the potential population affected by a large earthquake that occurred over the past month. The significant earthquakes from the past month can be found [here](https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/significant_month.csv). There will be on the order of 1 to 10 *significant* earthquakes from the last month. 

As a template for this analysis, please see this [GeoEnrichment Tutorial](https://developers.arcgis.com/python/guide/performing-geoenrichment/). For your analysis, you will follow some steps seen here. Your goal is to present an estimate of the **Total Population** affected by those earthquakes. I'm leaving it up to you to figure out buffer sizes, whether there are in fact any people within range of the earthquake, and other questions.

Please submit a detailed and clean notebook.

### Ruberic
- Well-documented Notebook (**10 Points**)
- reasonable *Total Population* estimates (**15 points**)
- Successful implementation of geoenrichment workflow based on the [Geoenrichment Tutorial](https://developers.arcgis.com/python/guide/performing-geoenrichment/). (**25 points**)
- **Bonus** plot the events on a map symbolized by potentail population affected. (**10 points**)

### Helpful Hint(s)
- If you create a Notebook that works, and after running it like 10 times in a row it stops working, you might have exceeded an ArcGIS service credit usage threshold. Becuase geoenrichment taps into the ArcGIS Online credit based service, you can actually exceed the credit useage. Just an FYI...


