## Preparation: [Watch this video on mapping and data science](https://www.youtube.com/watch?v=DdUBrV2zpvI&t=11s)

## Lecture:
Let's pick up where we left off last week and Look at **Week 7, Problem 4**
### 1. St. Louis Crime Aggregation

### 2. St. Louis Data Analysis

### 3. St. Louis Imagery Analysis Using Landsat NDVI


## In Class Exercises:
- Fighting forest fires notebook: https://developers.arcgis.com/python/sample-notebooks/fighting-california-forest-fires-using-spatial-analysis/

- [Geoenrichment](https://developers.arcgis.com/python/guide/performing-geoenrichment/)

## In Class Problems:
1. **What is the Total population of St. Louis City?** Following from the [Geoenrichment example](https://developers.arcgis.com/python/guide/performing-geoenrichment/), create a notebooks that:
- Gets the USA geoenrichment data
- lists the datasets within the geoenrichment dataset for the USA
- Lists the USA subgeographies ```usa.subgeographies.states```
- Uses *Missouri* as the state and to find the places within *Missouri* ```usa.subgeographies.states['Missouri'].places```
- Creates a Map object over St. Louis that plots the boundary of St. Louis over the topographic basemap
  - Hint: Make sure that you have the right place_name in ```usa.subgeographies.states['Missouri'].places['place_name'].geometry```
- Uses the enrichment capability ```stl_df = enrich(``` to find the *Total Population* ```'TOTPOP'``` of St. Louis.
- What is the Total Population of the City of St. Louis?


2. Using the [world population](http://slustl.maps.arcgis.com/home/item.html?id=92d3005feb84428a8f85160f2451ec63) [image service](https://landscape7.arcgis.com/arcgis/rest/services/World_Population_Estimate_2016/ImageServer), estimate the population of St. Louis using the same polygon.
- Define the image service layer ```il = ImageryLayer(url = img_url, gis=gis)```
- Use ```get_samples``` to get the counts of the population cells ```samples = il.get_samples(geometry =, geometry_type='esriGeometryPolygon', sample_count=)```
- Look at the ```samples``` variable.
- Extract the Population from the samples and sum those values.



## Homework:
1. read the following chapters of the *Python Data Science Handbook*
  - Chapter 3: [Introduction to Pandas](https://github.com/jakevdp/PythonDataScienceHandbook/blob/master/notebooks/03.00-Introduction-to-Pandas.ipynb) 
  - Chapter 3: [Introducing Pandas Objects](https://github.com/jakevdp/PythonDataScienceHandbook/blob/master/notebooks/03.01-Introducing-Pandas-Objects.ipynb)
  - Chapter 3: [Data Indexing and Selection](https://github.com/jakevdp/PythonDataScienceHandbook/blob/master/notebooks/03.02-Data-Indexing-and-Selection.ipynb)
  - Chapter 3: [Operations in Pandas](https://github.com/jakevdp/PythonDataScienceHandbook/blob/master/notebooks/03.03-Operations-in-Pandas.ipynb)
  - If you like learning this, don't limit yourself to just these chapters becuase this is the only class where we will focus on Pandas.
2. Project 3 Assigned.

## Helpful Links
- Data Science Example: https://developers.arcgis.com/python/sample-notebooks/historical-wildfire-analysis/
- Raster\Image Service exmaple: https://developers.arcgis.com/python/sample-notebooks/tour-the-world-with-landsat-imagery-and-raster-functions/
