# Preparation: 
1. Please read Chapters 1, 2, and 3 of [Introducing ArcGIS API 4 for Javascript](https://www.apress.com/us/book/9781484232811). Chapters 1 and 2 are really short!
2. Samples for the book can be found on [Github](https://github.com/Apress/introducing-arcgis-api-4-for-javascript/tree/master/intro-arcgis-js-api-4)

# Unit 1 Homework Solutions item options
Any volunteers to discuss their solutions?
Here are the [Unit 1 Homework Solutions](https://codepen.io/collection/XJqVNB).

# [Unit 2 CodePen Samples](https://codepen.io/collection/DjRGgj)
This is a link to the Unit 2 CodePen examples I intend to show during class. 
Check them out. Modify them. Explore them. 


# GeoJSON
- [http://geojson.io](http://geojson.io)

# Terminology
- [ArcGIS API for Javascript](https://developers.arcgis.com/javascript/)
- [Asynchronous Module Definition](https://requirejs.org/docs/whyamd.html)
- [Dojo](https://dojotoolkit.org/) - Javascript toolkit that aids in development. Provides everything you need to build a WebApp.
- [Maps](https://developers.arcgis.com/javascript/latest/sample-code/intro-mapview/index.html)
- [Layers](https://developers.arcgis.com/javascript/latest/sample-code/layers-portal/index.html)
- [Views](https://developers.arcgis.com/javascript/latest/sample-code/scene-goto/index.html)
- Accessors - As a general term, functions that get something for you
- [Promises](https://developers.google.com/web/fundamentals/primers/promises) - Promises for asynchronous operations.
```
promise.then(function(result) {
  console.log(result); // "Stuff worked!"
}, function(err) {
  console.log(err); // Error: "It broke"
});
```
- UI - User Interface
- Widgets - Elements on the user interface that do something
- [Web Scenes](https://developers.arcgis.com/javascript/latest/sample-code/layers-scenelayer/index.html)
- [Local Scenes](https://developers.arcgis.com/javascript/latest/sample-code/scene-local/index.html)

Let's start by looking at the example Rubalcava lays out in Chapter 2.

To do this, we can follow the pattern in [Intro to MapView (2D)](https://developers.arcgis.com/javascript/latest/sample-code/intro-mapview/index.html) example.

Rather than look at the CSS, HTML, and Javascript, let's put it altogether in the HTML like last week.

Let's do this in [JSBin](https://jsbin.com/?html,output)

Once we have a map, change it to a Scene.

Let's save this as an app in Github and view it online!

# ArcGIS Layers
Let's learn about layers in ArcGIS!

- Go to ArcGIS Online
- Search for [traffic layers outside of your organization](https://www.arcgis.com/home/search.html?q=traffic&t=content&start=1&sortOrder=desc&sortField=relevance&restrict=false&focus=layers-weblayers-features)
- Find [California Traffic Layers](https://www.arcgis.com/home/search.html?q=traffic&t=content&start=1&sortOrder=desc&sortField=relevance&restrict=false&focus=layers-weblayers-features)
- Open up [the service](https://demographics5.arcgis.com/arcgis/login/?returnUrl=https://demographics5.arcgis.com/arcgis/rest/services/USA_Traffic_Counts/MapServer/0)
- Let's query the service
- Notice you can return HTML, JSON (Esri JSON), GeoJSON, etc.
- Let's add this to a Webmap.
- Change the renderer to heatmap.
- Change renderer back to some class breaks and save the Webmap.

**What's the point of this?**
*That we did in Leaflet can be done without code. But you can code it now with Leaflet and will be able to with ArcGIS JavaScript!*

# Completed Apps
## My first JSAPI App
- [App in CodePen](https://codepen.io/gbrunner/pen/MWjoKBG)
- [App in GitHub](https://gbrunner.github.io/my-first-app-refactored)
- [Code in GitHub](https://github.com/gbrunner/my-first-app-refactored)

##  App from Portal Item
- [App in CodePen](https://codepen.io/gbrunner/pen/LYRzRXg)
- [App in GitHub](https://gbrunner.github.io/add-layer-from-portal-item)
- [Code in GitHub](https://github.com/gbrunner/add-layer-from-portal-item)

## App from Feature Layer
- [App in CodePen](https://codepen.io/gbrunner/pen/MWjEbwr)
- [App in GitHub](https://gbrunner.github.io/add-feature-layer)
- [Code in GitHub](https://github.com/gbrunner/add-feature-layer)

## App from Imagery Layer
- [App in CodePen](https://codepen.io/gbrunner/pen/yLazVOp)
- [App in GitHub](https://gbrunner.github.io/add-imagery-layer)
- [Code in GitHub](https://github.com/gbrunner/add-imagery-layer)

## App from CSV
- [App in CodePen](https://codepen.io/gbrunner/pen/zYKEoKm)
- [App in GitHub](https://gbrunner.github.io/add-csv-layer)
- [Code in GitHub](https://github.com/gbrunner/add-csv-layer)

## App from Web Scene
- [App in CodePen](https://codepen.io/gbrunner/pen/dypVpjQ)
- [App in GitHub](https://gbrunner.github.io/intro-to-scene-view)
- [Code in GitHub](https://github.com/gbrunner/intro-to-scene-view)

# Unit 2 Assignment
1. Finish the **Classwork\Homework Problems** and submit them as **Assignment 2**.
2. Read Chapters 4 and 5 of [Rubalcava](https://www.apress.com/us/book/9781484232811) on **API Core Fundamentals** and **Scenes**
3. Project 1 assigned!

## Exercises
1. [Create a starter app](https://developers.arcgis.com/labs/javascript/create-a-starter-app/)
2. [Select a basemap](https://developers.arcgis.com/labs/javascript/select-a-basemap/)
3. [Add layers to a map](https://developers.arcgis.com/labs/javascript/add-layers-to-a-map/)

## Classwork\Homework Problems:
Please complete problems 1, 2, and 3. Problem 4 is optional, but I think it is achievable and that you will find some satisfaction in completing it and learning the topic.

1. Search through ArcGIS Online and find 2 feature layers that overlap (not including the basemap). You will create two apps that show both layers on the map. **Please submit your code and app using GitHub. The app should be hosted on GitHub using GitHub Pages.**

**App 1**
- Create one by adding the layers to the app [From a Webmap](https://developers.arcgis.com/javascript/latest/sample-code/webmap-basic/) and then loading the Webmap object into the ArcGIS Javascript API
- Start with the [Load a Basic Webmap Example](https://developers.arcgis.com/javascript/latest/sample-code/webmap-basic/)
- Create a Webmap in [http://slustl.maps.arcgis.com/home/index.html](http://slustl.maps.arcgis.com/home/index.html). After you have saved it, make sure to *Share* it with everyone.
- After you make the map, take the **webmap ID** and load use it as the id below:
```
      var webmap = new WebMap({
        portalItem: { // autocasts as new PortalItem()
          id: "f2e9b762544945f390ca4ac3671cfa72"
        }
      });
```
- The Webmap ID is the long alpha-numeric string at the end of the arcgis.com url. For example, for this webmap:
```
http://slustl.maps.arcgis.com/home/item.html?id=d2e5c37512054e62a15464955dc65d95
```
The ID is:
```
d2e5c37512054e62a15464955dc65d95
```

**App 2**
- Using the same layers you added to the Webmap, create a web application by adding the layers as Feature Layers like in the [Intro to Feature Layer](https://developers.arcgis.com/javascript/latest/sample-code/layers-featurelayer/index.html) example. **Please submit your code and app using GitHub. The app should be hosted on GitHub using GitHub Pages.**

- For this problem, you'll have to load multiple layers, similar to this:
```
var featureLayer_1 = new FeatureLayer({
  url: "https://services.arcgis.com/V6ZHFr6zdgNZuVG0/arcgis/rest/services/Landscape_Trees/FeatureServer/0"
});

map.add(featureLayer_1);

var featureLayer_2 = new FeatureLayer({
  url: "https://services.arcgis.com/V6ZHFr6zdgNZuVG0/arcgis/rest/services/Landscape_Trees/FeatureServer/0"
});

map.add(featureLayer_2);
```

2. Create a webapp that uses the [CSV Layer](https://developers.arcgis.com/javascript/latest/sample-code/layers-csv/index.html) to map crime over St. Louis from the [STL Crime CSV](https://raw.githubusercontent.com/gbrunner/adv-programming-for-gis-and-rs/master/Web%20Development%20Module/Unit%202%20-%20ArcGIS%20JavaScript%20API/stl_crime_wgs_84.csv) in this folder. **Please submit your code and app using GitHub. The app should be hosted on GitHub using GitHub Pages.**

- Start with [my CSV Layer example](https://codepen.io/gbrunner/pen/zYKEoKm) or [Esri's CSV Layer example](https://developers.arcgis.com/javascript/latest/sample-code/layers-csv/index.html)
- Change the url to be:
```
var url = "https://raw.githubusercontent.com/gbrunner/adv-programming-for-gis-and-rs/master/Web%20Development%20Module/Unit%202%20-%20ArcGIS%20JavaScript%20API/stl_crime_wgs_84.csv";
```
- Change the symbol color.
- Change the *center* and the *zoom* to be over St. Louis, MO.


3. Change the renderer in the crime map to a [heatmap renderer](https://developers.arcgis.com/javascript/latest/sample-code/visualization-heatmap/index.html). Have some fun. Change the colors!

- Starting from the [Heatmap Visualization Example](https://developers.arcgis.com/javascript/latest/sample-code/sandbox/index.html?sample=visualization-heatmap), change the URL to be:
```
var url = "https://raw.githubusercontent.com/gbrunner/adv-programming-for-gis-and-rs/master/Web%20Development%20Module/Unit%202%20-%20ArcGIS%20JavaScript%20API/stl_crime_wgs_84.csv"
```
- Change the template to:
```
const template = {
   title: "Crime committed at {ILEADSStreet}"
};
```
- Change the CSV layer parameters to be:
```
const layer = new CSVLayer({
        url: url,
        title: "St. Louis Crime Heatmap",
        copyright: "St. Louis Police Department",
		latitudeField:"Lat",
        longitudeField:"Lon",
		popupTemplate: template,
		renderer: renderer
});
```
- Center the Map over St. Louis.
- Play around with the renderer colors.
- Have some fun!

4. (**Optional**) Following from this [server side raster function example](https://developers.arcgis.com/javascript/latest/sample-code/layers-imagery-popup/index.html), do the following:
- Change the service to point to the Landsat 8 Views Service (https://landsat2.arcgis.com/arcgis/rest/services/Landsat8_Views/ImageServer)
- Look at the service **RasterFunction Infos**. Change the Raster function template to one of the *NDVI* Raster Functions.
- Change the Zoom location to be over the Midwest.
- After you change it, does the *Popup* still work?
- If not, can you fix it? The Bands for Landsat 8 can be found [here](https://www.usgs.gov/faqs/what-are-band-designations-landsat-satellites?qt-news_science_products=0#qt-news_science_products). This data corresponds to the OLI sensor.

# Helpful Links
- [Esri GeoDav Hacker Lab JSAPI samples](https://github.com/Esri/geodev-hackerlabs/tree/master/develop/jsapi)
- [Heatmap Renderer](https://developers.arcgis.com/javascript/latest/sample-code/visualization-heatmap/index.html)
- [Colors as Hex Codes](http://www.color-hex.com/)
