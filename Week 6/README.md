## Preparation for Class: [Watch this Video](https://www.youtube.com/watch?v=hWl4WXVZcIQ)

## Lecture
### Intro to Github
1.	Go to GitHub.com
  - Register
  -	Create a new repo
  -	Initialize with a readme
2.	Clone Repo in SourceTree
3.	Modify Readme in Source Tree
4.	Commit to GitHub.com
5.	Push
6.	Go to Github and se the update
7.	Add script to repo folder
8.	Commit and Push
9.	Visualize the changes
10.	Fork a repo
11.	Add a person to a repo

**Break**

### Administering ArcGIS Online
1. Go to ArcGIS Online.
2. Show users the *Overview* tab.
3. Show users the *Members* tab.
4. Show *Licenses*, *Status*, and *Settings* tabs.
5. Go to user: Gregory Brunner
6. Show students options to change on their personal user info.
7. Show students *Groups*.
8. Create a new *Group*.
9. Invite the students.
10. Add Content to the *Group*.

### Python Demos:
1. [Users and Groups Notebook](https://github.com/gbrunner/Advanced_Python_for_GIS_and_RS/blob/master/Week%206/Lecture%201%20-%20Users%20and%20Groups.ipynb)

## Optional Classwork Exercises
These exercises are optional this week. You don't need to explicitly do them but please use them to guide you on the classwork problems below. Look at them in this order. Numbers one and two should be particularly helpful.
1. [Accessing and Managing Groups](https://developers.arcgis.com/python/guide/accessing-and-managing-groups/)
2. [Accessing and Managing Users](https://developers.arcgis.com/python/guide/accessing-and-managing-users/)
3. [How to share your content](https://developers.arcgis.com/labs/python/share-your-content/)
4. [Batch Creation of Groups](https://developers.arcgis.com/python/sample-notebooks/batch-creation-of-groups/)

## Classwork Problems
For the Classwork problems, please follow the instructions, hints and **helpful links** below.

1. Using Python, create 3 groups in ArcGIS Online: 
 - *YOUR_FIRST_NAME*_Webmaps
 - *YOUR_FIRST_NAME*_Feature_Services
 - *YOUR_FIRST_NAME*_All_Content
 
 *Hints:* 
 - Look at the help for [**create**](https://esri.github.io/arcgis-python-api/apidoc/html/arcgis.gis.toc.html?highlight=create%20group#arcgis.gis.GroupManager.create)
 - [Creating new groups](https://developers.arcgis.com/python/guide/accessing-and-managing-groups/#Creating-new-groups)
 - Look at the [batch group creation example](http://notebooks.esri.com/user/lQucDqTaF2lPQWZtPFh4ja4vd/notebooks/samples/03_org_administrators/batch_creation_of_groups.ipynb). Note that I am not looking for you to create a CSV to do this. Just use the [gis.groups.create](https://esri.github.io/arcgis-python-api/apidoc/html/arcgis.gis.toc.html?highlight=create%20group#arcgis.gis.GroupManager.create) function as listed above.
 
2. Using Python, share any webmaps you have in your ArcGIS Online account with *YOUR_FIRST_NAME*_Webmaps. Share any Feature Services you have with *YOUR_FIRST_NAME*_Feature_Services,and share all content you have with *YOUR_FIRST_NAME*_All_Content. Note that if you have no webmaps or feature services, publish a feature service and create a webmap beforehand.

*Hints:*
- You can list your items using **gis.users.me.items()**
- [Sharing your items to new groups](https://developers.arcgis.com/python/guide/accessing-and-managing-groups/#Sharing-content-to-groups)

3. Export all ArcGIS Online users to a CSV file. In the CSV file, please list the username, email address, user level, and user type.

*Hints:*
- [Accessing and Managing Users](https://developers.arcgis.com/python/guide/accessing-and-managing-users/)
- [*User* help page](https://esri.github.io/arcgis-python-api/apidoc/html/arcgis.gis.toc.html?highlight=user#arcgis.gis.GIS.users)

## Homework
1. Please complete the problems above and submit it as Assignment 6.
2. Watch these two videos: [Publishing](https://www.youtube.com/watch?v=4AzOodYTHs4) and [Automating your WebGIS](https://www.youtube.com/watch?v=0LfJrk2_VRg). This video will mostly recap what we've been doing in Week 1 and 2 and give some perspective on other things that you can do with Python.
3. Work on **Project 2**

## Helpful Links
- [Accessing and Managing Groups](https://developers.arcgis.com/python/guide/accessing-and-managing-groups/)
- [Accessing and Managing Users](https://developers.arcgis.com/python/guide/accessing-and-managing-users/)
- [How to share your content](https://developers.arcgis.com/labs/python/share-your-content/)
- [Batch Creation of Groups](https://developers.arcgis.com/python/sample-notebooks/batch-creation-of-groups/)
