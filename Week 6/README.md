## Prepatation:
Please read [Raster processing using Python Tools](https://geohackweek.github.io/raster/).
- [Introduction](https://geohackweek.github.io/raster/01-introduction/)
- [Geospatial Concepts: Raster Data](https://geohackweek.github.io/raster/02-rasterconcepts/)
- [Encodings, Formats and Libraries](https://geohackweek.github.io/raster/03-encodingsandformats/)
- [Working with Raster Datasets](https://geohackweek.github.io/raster/04-workingwithrasters/)
- [Rainier DEM Example](https://geohackweek.github.io/raster/06-pygeotools_rainier/)
We will not follow this, verbatin, but we will go though the techniques that are shown here.

Also, please take a look at this tutorial for [using imagery layers that are hosted online](https://developers.arcgis.com/python/guide/using-imagery-layers/). If we have time, we wil cover this too.

## Lecture:
Following from the **Raster processing** tutorial, demonstrate;
1. Read Landsat images into a numpy array
2. Show images using *matplotlib*
3. Make sure to read in projection info for export back to TIFF
4. Calculate NDVI from numpy array
5. Show NVDI imapge using *matplotlib*
6. *Apply QA band Mask* -> Talk about advanced Numpy concepts
7. Show Raster in *matplotllib*
8. Save image back to disk
9. Load iamge into ArcMap

## In Class Problems:
Following from what was shown in the lecture, do the following:
1. read in the DEM into a numpy array and it's georeference information from the DEM included in the folder.
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
    

## Homework:
