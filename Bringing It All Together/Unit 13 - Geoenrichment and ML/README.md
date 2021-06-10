# [What is GeoEnrichment](https://developers.arcgis.com/python/guide/part1-introduction-to-geoenrichment/)
GeoEnrichment adds location intelligence to the data by 
providing facts about a location or an area. Using 
GeoEnrichment, you can get information about the people 
and places in a specific area or within a certain distance 
or drive time from a location. It enables you to query and 
use information from a large collection of data sets including 
population, income, housing, consumer behavior, and the natural 
environment. GeoEnrichment enables you to answer questions about 
locations that you can't answer with maps alone. For example: 
What kind of people live here? What do people like to do in 
this area? What are their habits and lifestyles?

# [Where to enrich? (what are study areas?)](https://developers.arcgis.com/python/guide/part2-where-to-enrich-study-areas/)
GeoEnrichment uses the concept of a study area to define the location 
of the point or area that you want to enrich with additional 
information or create reports about. The accepted forms of 
study areas are:

    Street address locationsPoint, line and polygon geometries
        Single line input
        Multiple field input
    Buffered study areas
    Named statistical areas

# [Where to enrich? (what are Named Statistical Areas?)](https://developers.arcgis.com/python/guide/part3-where-to-enrich-named-stat-areas/)
Each country has several named statistical areas in 
a hierarchy of geography levels (such as states, counties, 
zip codes, etc). The Country class can be used to discover 
the data collections, sub-geographies and available 
reports for a country. When working with a particular country, 
you will find it convenient to get a reference to it using the 
Country.get() method. This method accepts the country name or 
its [2 letter abbreviation](http://www.nationsonline.org/oneworld/country_code_list.htm) 
or [ISO3 code](https://unstats.un.org/unsd/tradekb/knowledgebase/country-code) and returns an instance 
of that country.

Let's look into some countries 
and explore their subgeographies.

# [What to enrich with? (What are Data Collections and Analysis Variables?)](https://developers.arcgis.com/python/guide/part4-what-to-enrich-datacollections-analysisvariables/)
As described earlier, a data collection is a preassembled list 
of attributes that will be used to enrich the input features. 
Collection attributes can describe various types of 
information, such as demographic characteristics and geographic 
context of the locations or areas submitted as input features.

Some data collections (such as default) can be used in 
all supported countries. Other data collections may 
only be available in one or a collection of countries. 
[Data Browser](https://doc.arcgis.com/en/esri-demographics/data/data-browser.htm) can be used to examine the entire global 
listing of variables, and associated datasets for each 
country.


# [Intro to Statistical Learning - Python](https://github.com/JWarmenhoven/ISLR-python)

# [Linear Regression from ISLR](https://nbviewer.jupyter.org/github/JWarmenhoven/ISL-python/blob/master/Notebooks/Chapter%203.ipynb#3.2-Multiple-Linear-Regression)

# [Gadient Boosting from ISLR](https://nbviewer.jupyter.org/github/JWarmenhoven/ISL-python/blob/master/Notebooks/Chapter%208.ipynb#8.3.4-Boosting)

# [Unit 13 Notebooks](https://arcg.is/1eXD4y0)
Notebooks for Unit 13

# Unit 13 Geoenrichment Notebooks
These are notebooks I have used in previous semesters.
- Unit 12 - Geoenrichment Example.ipynb
- Unit 12 - GeoEnrichment.ipynb 

# Unit 13 Assignment (Optional)
What is the Total population of St. Louis City? 
Following from the Geoenrichment example, 
create a notebooks that:

- Gets the USA geoenrichment data
- lists the datasets within the geoenrichment dataset for the USA
L- ists the USA subgeographies ```usa.subgeographies.states```
- Uses Missouri as the state and to find the places within Missouri ```usa.subgeographies.states['Missouri'].places```
- Creates a Map object over St. Louis that plots the boundary of St. Louis over the topographic basemap
    - Hint: Make sure that you have the right 
    - ```place_name in usa.subgeographies.states['Missouri'].places['place_name'].geometry```
- Uses the enrichment capability ```stl_df = enrich()``` to find the Total Population 'TOTPOP' of St. Louis.
- What is the Total Population of the City of St. Louis?
