## Preparation:
### Read the following chapters of the *Python Data Science Handbook*
  - Chapter 3: [Introduction to Pandas](https://github.com/jakevdp/PythonDataScienceHandbook/blob/master/notebooks/03.00-Introduction-to-Pandas.ipynb) 
  - Chapter 3: [Introducing Pandas Objects](https://github.com/jakevdp/PythonDataScienceHandbook/blob/master/notebooks/03.01-Introducing-Pandas-Objects.ipynb)
  - Chapter 3: [Data Indexing and Selection](https://github.com/jakevdp/PythonDataScienceHandbook/blob/master/notebooks/03.02-Data-Indexing-and-Selection.ipynb)
  - Chapter 3: [Operations in Pandas](https://github.com/jakevdp/PythonDataScienceHandbook/blob/master/notebooks/03.03-Operations-in-Pandas.ipynb)
  - If you like learning this, don't limit yourself to just these chapters becuase this is the only class where we will focus on Pandas.

## Lecture:
### Pandas
1. Show read in spreadsheet (CSV)
2. Slice data
3. List columns
4. Add Column
5. Populate column with some sort of analysis
6. Juxtapose against reading CSV files
7. Load dataframe from Python dictionary
8. Load dataframe from JSON
9. Load dataframe from ArcGIS Feature Service JSON
*Sequeys into Spatial Dataframes*

### ArcGIS Spatial Dataframe
1. Load this services directly into a spatial dataframe
2. Load a feature class in a geodatabse directly to a Spatial dataframe
3. Slice the dataframe
4. Publish the dataframe
5. **Go to ArcGIS Online and show the feature class**
6. **Make sure editing is enabled**
7. Show that we can update\edit an existing service using the spatial dataframe

## In Class Exercises:
1. [Loading a Spatial Dataframe](https://developers.arcgis.com/labs/python/load-spatial-data-frame/)
2. [Updating Features](https://developers.arcgis.com/python/sample-notebooks/updating-features-in-a-feature-layer/)

## In Class Problems:
1. Go to the [USGS Earthquakes Hazard Program and download *All Earthquakes* from the *Past Day*](https://earthquake.usgs.gov/earthquakes/feed/v1.0/csv.php). Using **pandas**:
- Read the CSV into a dataframe
- Drop the **nst, gap, dmin, rms,** and **net** fields from the dataframes. Look at ```df.drop```
- Slice the dataframe into 4 new dataframes corresponding to:
  - Earthquakes between 0 and 2.5 magnitude
  - Earthquakes between 2.5 and 4 magnitude
  - Earthquakes between 4 and 5 magnitudes
  - Earthquakes greater than 5 in magnitude
- Publish each dataframe to ArcGIS Online as a Feature Service
- Create a Webmap that shows all 4 feature classes

2. Go to the [USGS Earthquakes Hazard Program and download *All Earthquakes* from the *Past Week*](https://earthquake.usgs.gov/earthquakes/feed/v1.0/csv.php). Using **pandas**:
- Read in that CSV.
- Read in the CSV in this repo named: all_week_aug_13_20.csv.
- Append the two CSVs into a single dataframe.
- Publish the dataframe as a Feature Service **or** save it to a feature class. Either way, check that the output is valid afterwards in ArcGIS online or ArcMap.

*Hint: You can use [append](https://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.append.html)*
```df.append(df2, ignore_index=True)```

3. Let's revisit the [UNHCR Immigration Statistics API](http://popdata.unhcr.org/). Using this url:
```url = 'http://popdata.unhcr.org/api/stats/asylum_seekers_monthly.json?year=2015&month=1&coa=FRA'```
You can retrieve the UNHCR immigration assylum seeker statistics for France from January or 2015. Using pandas, you can convert the JSON returned by this URL directly into a dataframe as follows:
```
import requests
import pandas as pd

url = 'http://popdata.unhcr.org/api/stats/asylum_seekers_monthly.json?year=2015&month=1&coa=FRA'
data = requests.get(url)
as_json = data.json()
df = pd.DataFrame(as_json)
```

After importing the data into a pandas dataframe, please answer the follwoing questions:
- From what country did France recieve the most immigrants in January 2015?
- What were the 5 countries that contributed the most immigrants in January of 2015?
- From what countries did only 1 immigrant arrive from France in January of 2015?

Then, modify the URL to answer the same questions for January of 2018
- From what country did France recieve the most immigrants in January 2018?
- What were the 5 countries that contributed the most immigrants in January of 2018?
- From what countries did only 1 immigrant arrive from France in January of 2018?

Please use pandas dataframe manipulations to answer all of these questions.

**Hints:**
- ```df.sort_values(by=)``` can be used to [sort data](https://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.sort_values.html)
- ```.idxmax()``` and ```.idxmin()``` can be used in pandas to get [min](https://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.idxmin.html) and [max](https://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.idxmax.html) values in a dataframe

4. **Challenge** Going back to problem 3, setup your Python Notebook to easily take in an arbtrary *year*, *month*, and *country* and answer the series of three questions by only modifying the *year*, *month*, and *country* parameters. For example, your code should have the following variables defined and just be able to pass them through the query URL:
```
year = 2015
month = 'January'
country = 'USA'
```
5. **Challenge** Fot this challenge, let's revisit the Fragile States Index. Using the [fsi-2018.xlsx]()...
- Read the file into a pandas dataframe
- List the columns in the dataframe ```df.columns.values```
- For each column, I want a list of the worst 10 countries per metric.
I would like your output to be in the form of a dictionary such as:
```
{'C1: Security Apparatus': ['Central African Republic',
  'Libya',
  'Mali',
  'Chad',
  'Somalia',
  'Philippines',
  'Syria',
  'Yemen',
  'Afghanistan',
  'South Sudan'],
 'C2: Factionalized Elites': ['Lebanon',
  'Kenya',
  'Sudan',
  'Central African Republic',
  'South Sudan',
  .
  .
  .
  ```

## Homework:
1. Complete this weeks **In Class Problems**
2. Please read:
- [Intro to Numpy](https://github.com/jakevdp/PythonDataScienceHandbook/blob/master/notebooks/02.00-Introduction-to-NumPy.ipynb)
- [Understanding Data Types](https://github.com/jakevdp/PythonDataScienceHandbook/blob/master/notebooks/02.01-Understanding-Data-Types.ipynb)
- [Basics of Numpy Arrays](https://github.com/jakevdp/PythonDataScienceHandbook/blob/master/notebooks/02.02-The-Basics-Of-NumPy-Arrays.ipynb)
3. Please read [Raster processing using Python Tools](https://geohackweek.github.io/raster/).
- [Introduction](https://geohackweek.github.io/raster/01-introduction/)
- [Geospatial Concepts: Raster Data](https://geohackweek.github.io/raster/02-rasterconcepts/)
- [Encodings, Formats and Libraries](https://geohackweek.github.io/raster/03-encodingsandformats/)
- [Working with Raster Datasets](https://geohackweek.github.io/raster/04-workingwithrasters/)
- [Rainier DEM Example](https://geohackweek.github.io/raster/06-pygeotools_rainier/)
We will not follow this verbatim, but we will go though the techniques that are shown here.

## Help
- [Python Dictionaries](https://www.w3schools.com/python/python_dictionaries.asp)
