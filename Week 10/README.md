## Preparation:
Please read [Raster processing using Python Tools](https://geohackweek.github.io/raster/).
- [Introduction](https://geohackweek.github.io/raster/01-introduction/)
- [Geospatial Concepts: Raster Data](https://geohackweek.github.io/raster/02-rasterconcepts/)
- [Encodings, Formats and Libraries](https://geohackweek.github.io/raster/03-encodingsandformats/)
- [Working with Raster Datasets](https://geohackweek.github.io/raster/04-workingwithrasters/)
- [Rainier DEM Example](https://geohackweek.github.io/raster/06-pygeotools_rainier/)
We will not follow this, verbatin, but we will go though the techniques that are shown here.

Also, please take a look at this tutorial for [using imagery layers that are hosted online](https://developers.arcgis.com/python/guide/using-imagery-layers/). If we have time, we wil cover this too.

## Lecture 1:
Following from the **Raster processing** tutorial, demonstrate;
1. Read Landsat images into a numpy array
2. Show images using *matplotlib*
3. Make sure to read in projection info for export back to TIFF
4. Calculate NDVI from numpy array
5. Show NVDI imapge using *matplotlib*
6. *Apply QA band Mask* -> Talk about advanced Numpy concepts
7. Show Raster in *matplotllib*
8. Save image back to disk
9. Load image into ArcMap

## In Class Problem 1:
Following from what was shown in the lecture, do the following:
1. Read in the DEM into a numpy array and it's georeference information from the DEM included in the folder. What are the dimmensions of the image? ```dem.shape```
2. Display it using *matplotlib*
3. Create a slope raster from the dem using the following slope function:
```
def slope_function(dem, cellsize):
    #Modified from calculation found here:
    #http://geoexamples.blogspot.com/2014/03/shaded-relief-images-using-gdal-python.html

    x, y = np.gradient(dem, cellsize, cellsize)
    #slope = np.pi/2.0 - np.arctan(np.sqrt(x*x + y*y))
    slope = np.arctan(np.sqrt(x*x + y*y))
    return slope
 ```
 4. Display the slope using imshow in *matplotlib*
 5. Export the raster to a TIFF
 6. View in Arcmap
 7. **Challange!** Building on the workflow here, go back to Jupyter and create a Hillshade raster from the DEM. Follow the code found [here](https://github.com/rveciana/geoexamples/blob/master/python/shaded_relief/hillshade.py)
 ```
 def hillshade(array, azimuth, angle_altitude): 
    
    x, y = gradient(array)
    slope = pi/2. - arctan(sqrt(x*x + y*y))
    aspect = arctan2(-x, y)
    azimuthrad = azimuth*pi / 180.
    altituderad = angle_altitude*pi / 180.
     
 
    shaded = sin(altituderad) * sin(slope)\
     + cos(altituderad) * cos(slope)\
     * cos(azimuthrad - aspect)
    return 255*(shaded + 1)/2
 ```
 8. View the hillshade in matplotlib
 9. Export the hillshade to a TIFF
 
## Lecture 2:
Go through the [Using Imagey Layers](https://developers.arcgis.com/python/guide/using-imagery-layers/) Notebook.
1. Log into the GIS
2. Serarch for "Landsat 8 Views"
3. Display the "Landsat 8 Views" items
4. Bring the Landsat 8 service into a ImageryLayer
5. Add the Landsa 8 service to a map
6. Show the Landsat 8 table as a dataframe
7. List the raster Functions
8. Play through the raster functions
9. Show how to create a layer by appling the SAVI function function.
 
## In Class Problem 2:
**Challange!** Following from **In [13]** in the [Using Imagery Layers Tutorial](https://developers.arcgis.com/python/guide/using-imagery-layers/), create an NDVI layer over St. Louis. Submit your Jupyter notebook.

## In Class Problem 3:
The Climate Hazards Group at UC Santa Barbera produces a 30+ year quasi global dataset called [CHIRPS](http://chg.geog.ucsb.edu/data/chirps/). You can download the precipitation data as rasters here: ftp://ftp.chg.ucsb.edu/pub/org/chg/products/CHIRP/. 

For this exercise:
1. Download the first 36 rasters here: ftp://ftp.chg.ucsb.edu/pub/org/chg/products/CHIRP/dekads/. 
    - This data has 3 precipitation rasters per month, 1 every ten days, totaling 36 rasters in a year. 
2. Read each raster into a numpy array and concatenate those numpy arrays into a matrix of dimmension (3,x,y)
3. Using *matplotlib*, plot a few slices of the array so that we can see the rainfall over time.
4. **Are the rainfall trends periodic?**
5. **Challenge** Extract the time frame the filenames and plot some rainfall values (on the y-axis) vs. time (on the x-axis).

## Homework:
1. Watch the following video on [ArcGIS Python Raster Functions](https://www.youtube.com/watch?v=OgwnKRrVHN0)
2. Assign Project 2. You have 3 weeks to complete Project 2
