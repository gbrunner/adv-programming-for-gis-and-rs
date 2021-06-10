# Imagery and Jupyter RISE

## Preparation:
- Watch this video on [Jupyter RISE](https://www.youtube.com/watch?v=Gx2TnIdt0hw)
- Watch this video on [Jupyter Dashboards](https://www.youtube.com/watch?v=8Jktm-Imt-I)
- Check out the Following Dashboards on [Notebooks.esri.com](http://notebooks.esri.com). They will be in the samples/02_power_users folder.
  - jupyter_dashboard_for_raster_analytics.ipynb
  - [building_a_change_detection_app_using_jupyter_dashboard.ipynb](https://developers.arcgis.com/python/sample-notebooks/building-a-change-detection-app-using-jupyter-dashboard/)

## Lecture 1:
Go through the [Using Imagey Layers](https://developers.arcgis.com/python/guide/using-imagery-layers/) Notebook.
1. Log into the GIS
2. Search for "Landsat 8 Views"
3. Display the "Landsat 8 Views" items
4. Bring the Landsat 8 service into a ImageryLayer
5. Add the Landsa 8 service to a map
6. Show the Landsat 8 table as a dataframe
7. List the raster Functions
8. Play through the raster functions
9. Show how to create a layer by appling the SAVI function function.

## Lecture 2
Pixel analysis from Image Services

## Lecture 3
### Jupyter RISE
- Install RISE
```conda install -c conda-forge rise --force```
- Turn my Ocean Depth explorer into a RISE presentation
 
## In Class Problem 1:
**Challange!** Following from **In [13]** in the [Using Imagery Layers Tutorial](https://developers.arcgis.com/python/guide/using-imagery-layers/), create an NDVI layer over St. Louis. Do this 2 ways:
1. Applying the NDVI Raster function like ```map.add_layer(apply(landsat_lyr, fn['name']))```
2. Using the ```ndvi``` function similar to how I showed the ```savi``` function ```savi_map.add_layer(savi(landsat_lyr, band_indexes="5 4 0.3"))```

## In Class Problem 2
Turn what you submitted for **Project 2** into a presentation using Jupyter RISE

## Homework:
1. Complete the **In Class Assignments**
2. Work on **Project 3** (your **Final Project**).

