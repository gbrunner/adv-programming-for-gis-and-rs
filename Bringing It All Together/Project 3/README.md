# Project 3 - Bringing it all together

**Choose one of the following options.**

## Option 1

Suppose you work for a consulting agency, and they just 
tasked you with a new assignment to build scripts 
to analyze and inform the NYC council about the 
Uber ride sharing companies. The city wants 1.) 
reproducible workflows in a jupyter notebook and 2.) 
A web page (web application with a map) showing the results.

The data can be obtained from 
here: https://www1.nyc.gov/site/tlc/about/tlc-trip-record-data.page

You will likely need the 
following resources, which can be found on the webpage:
1. Taxi Ride CSV (I suggest Yellow Taxi records CSV from January 2021).
2. [Taxi Zone Lookup Table (CSV)](https://s3.amazonaws.com/nyc-tlc/misc/taxi+_zone_lookup.csv)
3. [Taxi Zone Shapefile (CSV)](https://s3.amazonaws.com/nyc-tlc/misc/taxi_zones.zip)

The information will be given to non-technical 
individuals so they want pretty maps, graph, 
and charts. They have set limits on what 
Python package you can use because their 
IT staff restricts what analysts can use.
Whitelist Software Limitations from the Client

    scipy
    sklearn
    ArcGIS API for Python
    ArcPy
    Standard Python Libraries (which includes Numpy and Pandas)
    Requests

I want to see Python Analysis that derives 2 of the following:
- aggregation of taxi statistics by "Borough" and "Zone"
- Interactive maps (minimum of 2)
- Nice descriptive reporting and plots that show statistics
- Other interesting facts

What to turn in: **Jupyter notebook or ArcGIS Notebook**

###Grading

The project will be graded on the following:
- Successful analysis: (70%)
- Description of goal and meaning of result explained: (10%)
- Proper Markdown usage in Jupyter Notebook (20%)
- 25 Bonus points for making a Leaflet or ArcGIS Javascript API application that showcases your results.

Some Hint(s)
- Use pandas to read the Taxi Ride CSV and Taxi Zone Lookup Table CSV into dataframes
- Join the Taxi "Borough" and "Zone" from the Taxi Zone Lookup Table to the Taxi Ride CSV using join (https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.join.html).
- Use groupby to get ride counts by "Zone" and by "Borough"
- Use the ArcGIS Python API to read the Taxi Zones shapefile into a spatially enabled dataframe.
- Join the counts to the spatially enabled dataframe.

## Option 2
City of Madison GIS Data Analysis Lab

The City of Madison is one of many cities 
that provide a wealth of geo-spatial 
information for anyone to analyze. 
Image you are a GIS analyst who works for 
the city. Being a large city there are many problems 
that need to be addressed.
- Crime
- Homelessness
- Environmental
- Housing .. any many more

Pick an issue you that interests you and explore the 
dataset. Use the ArcGIS API for Python analysis tools 
and perform some kind of analysis, such as 
aggregating the features by zip code, 
finding hot spots, or some other kind of analysis. 
Document your analysis.

Publish your results as a service and create a 
web application that is hosted on GitHub that shows your results

Think of this as your first big assignment 
on the job, and you want to impress your manager!

The data can be found here.

https://data-cityofmadison.opendata.arcgis.com/
I want to see Python Analysis that derives 2 of the following:
- aggregation of some features by city block, zip code, or some other region
- Some other interactive maps (minimum of 2)
- Nice descriptive reporting
- Other interesting facts

What to turn in: **Jupyter notebook or ArcGIS Notebook**

### Grading
Grading The project will be graded on the following:
- Successful analysis: (70%)
- Description of goal and meaning of result explained: (10%)
- Proper Markdown usage in Jupyter Notebook (20%)
- 25 Bonus points for making a Leaflet or ArcGIS Javascript API application that showcases your results.

**Note: If you want to work with data from another city, you can. You just need to find that city's data.**