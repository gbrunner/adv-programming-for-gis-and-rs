## Preparation: Read Chapter 1 of **Mastering Geospatial Analysis with Python**

## Lecture:
- Start with an introduction to ArcGIS Pro
- Seguey into ArcGIS Pro and Pyhon Package mangemeent
- Discuss Anaconda distribution of Python
- Setup Jupyter (if necessary). Use instructions from last semester.
- **Break**
- Introduction to ArcGIS Online
- Talk about Geocoding
- Add an address to webmap
- Introduction to the **ArcGIS API for Python.**
- [Markdown](https://www.markdowntutorial.com/) -> [Github Markdown Cheatsheet](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet#code)
- Create a Jupuyter notebook
- *GIS* Demo
- *Geocoding* Demo

## Classwork Exercises:
1. Working with Maps in Jupyter: https://developers.arcgis.com/python/guide/using-the-map-widget/
2. Geocoding with Jupyter: https://developers.arcgis.com/python/guide/using-the-geocode-function/
3. [Search and Geocode](https://developers.arcgis.com/labs/python/search-and-geocode/)
4. **Optional** [Display a webscene](https://developers.arcgis.com/labs/python/display-web-scene/)
4. **Optional** [More on geocoding](https://developers.arcgis.com/python/guide/understanding-geocoders/)

## Classwork Problems:
1. Create a new Jupyter Notebook that:
  - Contains a map
  - Zooms to a particular city of interest
  - Changes the basemap from the default Terrain basemap
  - Please use Markdown to apply meaningful discriptions of your steps.
2. Create a Jupyter Notebook that:
- Search for an ACLED feature service in the ArcGIS Portal (if you are adventurous, feel free to search for a different point feature service)
- Adds that ACLED (or other service) to the map object as:
  - A point layer using a simple renderer (see *Hint* below for help).
  - A Classed Size Renderer that renders on the TOTAL_FATALITIES field.
  ```
  classed_size = { "renderer": "ClassedSizeRenderer", "field_name":"TOTAL_FATALITIES"}
  ```
- [Saves each map as a Webmap](https://developers.arcgis.com/python/guide/working-with-web-maps-and-web-scenes/#Saving-or-Updating-a-web-map)  

## Helpful Links
- [Publishing a CSV File](https://developers.arcgis.com/python/sample-notebooks/publishing-sd-shapefiles-and-csv/)
- [Understanding Geocoders](https://developers.arcgis.com/python/guide/understanding-geocoders/)
- [Understanding Renderers](https://developers.arcgis.com/web-map-specification/objects/renderer/)
- [Publishing a CSV that contains Addresses](https://developers.arcgis.com/python/sample-notebooks/publishing-sd-shapefiles-and-csv/#Publish-a-CSV-file-and-move-it-into-a-folder)
- [Saving a map object as a webmap](https://developers.arcgis.com/python/guide/working-with-web-maps-and-web-scenes/#Saving-or-Updating-a-web-map)

## Homework:
- Please complete the classwork and submit it as Assignment 5.
- Watch this video: https://www.youtube.com/watch?v=0LfJrk2_VRg
- Explore the different tabs on the online doc and get familiar with the general layout and the content available
  - https://developers.arcgis.com/python/ 
- Download the ArcGIS API for Python samples 
  - https://github.com/Esri/arcgis-python-api
