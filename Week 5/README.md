## Preparation: Read Chapter 1 of **Mastering Geospatial Analysis with Python**.

## Lecture:
- Start with an introduction to ArcGIS Pro
- Seguey into ArcGIS Pro and Pyhon Package mangemeent
- Discuss Anaconda distribution of Python
- Setup Jupyter (if necessary). Use instructionf from last semester
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
2. Crete a Jupyter Notebook that:
- Searched for an ACLED feature service in the ArcGIS Portal (if you are adventurous, feel free to search for a different point feature service)
- Adds that ACLED (or other service) to the map object as:
  - A point layer using a simple renderer (see *Hint* below for help).
  - A Classed Size Renderer that renders on the TOTAL_FATALITIES field.
  ```
  classed_size = { "renderer": "ClassedSizeRenderer", "field_name":"TOTAL_FATALITIES"}
  ```
- [Saves each map as a Webmap](https://developers.arcgis.com/python/guide/working-with-web-maps-and-web-scenes/#Saving-or-Updating-a-web-map)  
3. Create a second notebook that geocodes the attached CSVs (Thunder_Departed.csv and Thunder_Acquisitions.csv) of addresses and adds each to the same map opject with a differernt symbology. Save this as a webmap following from this example (https://developers.arcgis.com/python/guide/working-with-web-maps-and-web-scenes/#Saving-or-Updating-a-web-map). Be sure to go to ArcGIS online and check that the Webmap is there!
*Hint:* You can change the symbology by changing the renderer. For example, if you change the color values inthis renderer, the points will change color accordingly.
```
simple_renderer = {
  "renderer": {
    "type": "simple",
    "symbol": {
      "color": [
        0,
        0,
        128,
        128
      ],
      "size": 15,
      "angle": 0,
      "xoffset": 0,
      "yoffset": 0,
      "type": "esriSMS",
      "style": "esriSMSCircle",
      "outline": {
        "color": [
          0,
          0,
          128,
          255
        ],
        "width": 0.99975,
        "type": "esriSLS",
        "style": "esriSLSSolid"
      }
    }
  }
}

map1.add_layer(acled, simple_renderer)
```

## Helpful Links
- [Publishing a CSV File](https://developers.arcgis.com/python/sample-notebooks/publishing-sd-shapefiles-and-csv/)
- [Understanding Geocoders](https://developers.arcgis.com/python/guide/understanding-geocoders/)

## Homework:
- Please complete the classwork and submit it as Assignment 1.
- Watch this video: https://www.youtube.com/watch?v=0LfJrk2_VRg
- Explore the different tabs on the online doc and get familiar with the general layout and the content available
  - https://developers.arcgis.com/python/ 
- Download the ArcGIS API for Python samples 
  - https://github.com/Esri/arcgis-python-api
