# Project 1 - Choose One of the Following
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
