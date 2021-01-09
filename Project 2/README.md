# Project 2

## Problem 1

[An image kernel is a small matrix used to apply effects like the ones you might find in Photoshop or Gimp, such as blurring](https://setosa.io/ev/image-kernels/). FOr this problem, I want you to use ```numpy``` to read in this image, and apply a 3x3 mean filter so that it smooths or blurs the image. I recommend doing this by iterating over every pixel, and for every pixel, average that pixel value with the pixels surrounding it.

## Problem 2
[The UN Refugee Agency (UNHCR)](https://www.unhcr.org/en-us/) tracks the movement of immigrants worldwide. They provide an API for you to access their data. You can access the [UNHCR API documentation here](https://api.unhcr.org/docs/).

For this problem, I want you to use the UNHCR data API to find out how many immigrants were resettled to the United States (USA) from the following countries:
- Syria (SYR)
- Sudan (SDN)
- Afghanistan (AFG)
- Iran (IRN)
- Iraq (IRQ)

FOr the following years:
- 2017
- 2018
- 2019
- 2020

I want you to figure out how to for the query URL to retrieve that data. As an example, the following URL will query the number of refugees that were resettled in the USA and Norway from Myanmar and Syria from 2017:
http://api.unhcr.org/rsq/v1/demographics?page=1&year=2017&origin=MMR%2CSYR&resettlement=NOR%2CUSA

Use ```pandas``` to read the data from the API into a dataframe as follows:
```
req = requests.get(url)
data = req.json()['results']
df = pd.DataFrame(data)
```

After the data is in the dataframe, do the following:
1. Plot each countries immigration statistics over those four years.
2. Plot the data on a map in your notebook.

## Problem 3

This problem is intentionally open-ended. Go to the [St. Louis Metro Police Department website](https://www.slmpd.org/Crimereports.shtml). Download 12 months worth of crime data. Using ```pandas```:
1. Bring them into a single dataframe.
2. Filter the data on a specific crime type.
3. Aggregated those types of crimes by month (or week or day).
4. Plot the number of times that crime occurred per month (or week or day) for the entire year.


# Project 2 - Choose One of the Following

## Goal: Apply your knowledge of the ArcGIS Python API and web services
## Asssigned: Week 5
## Due: Week 8
## Score: Out of 100 points. Anything exceeding 100 points is a A+!

## 1. Understand the Fragile States Index
The [Fragile States Index](http://fundforpeace.org/fsi/) is an open source dataset that ranks the fragility of the countries of the world. The FSI data is available as CSV files that ranks the courties in terms of fragility but also provides metrics on other aspects of each country's health, such as the econmony, human rights, and pliltical division. For this project, I want you to create a well documented Jupyter Notebook where you:
- Publish each FSI CSV file as a uniquly named feature service.
- Create a webmap containing each feature service symbolized so that I can tell which countries are worse and which are better.
- Describe the proocess and data along the way.
- Please be as concise as possible with your code. Use for loops where possible rather than repreating code.
 If you do all of these things, you will get an **A**
 
 If you want an **A+**, please complete of of the following additoinal tasks.
 Either:
 - Create a Storymap from your FSI Webmaps where your storymap has a new page for each year (this can be done manually, i.e. without Python).
 - Or, for each country, run the Mann-Kendall Test (mk_test.py) adn assess whether the FSI trend is improving, degrading, or unchanging over time.



## 2. Understanding Immigration Patterns
The Office of the United Nations High Commissioner for Refugees (UNHCR), also known as the UN Refugee Agency, is a United Nations agency mandated to protect and support refugees at the request of a government or the UN itself and assists in their voluntary repatriation, local integration or resettlement to a third country. Its headquarters are in Geneva, Switzerland and is a member of the United Nations Development Group. It provides data on immigration status for coutries across the world. In this project, I want you to use the [UNHCR Data API](http://popdata.unhcr.org/wiki/index52ce.html?title=API_Documentation) to create a series of Webmaps that show how many immigrants are finding assylum in each country listed [here](http://popdata.unhcr.org/api/stats/country_of_asylum.json) for all 12 months 2017. We will learn more about how to do this in week 3, so if you are interested in this project, please look ahead to week 3. To get the number of assylum seekers per month, see here: http://popdata.unhcr.org/api/stats/asylum_seekers_monthly.json?year=2017&month=1&coa=SRB&total=true.

For this project, I want you to create a well documented Jupyter Notebook where you:
- Publish 12 feature services, each showing the number of assylum seekers per country.
- Create a webmap containing each feature service symbolized so that I can tell which countries are taking in more assylumn seekers.
- Describe the proocess and data along the way.
- Please be as concise as possible with your code. Use for loops where possible rather than repreating code.
 If you do all of these things, you will get an **A**

 If you want an **A+**, please complete of of the following additoinal tasks.
 Either:
 - Create a Storymap from your UNHCR feature services where your storymap has a new page for each month (this can be done manually, i.e. without Python).
 - Or, for each country, run the Mann-Kendall Test (mk_test.py) adn assess whether the number of assylum seekers is increasing, decreasing, or unchanging over time.
