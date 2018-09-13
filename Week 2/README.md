## Preparation: 
1. Please read Chapters 1, 2, and 3 of [Introducing ArcGIS API 4 for Javascript](https://www.apress.com/us/book/9781484232811). Chapters 1 and 2 are really short!
2. Samples for the book can be found on [Github](https://github.com/Apress/introducing-arcgis-api-4-for-javascript/tree/master/intro-arcgis-js-api-4)

## Lecture:
### Review Homework Problem
- Any volunteers to discuss their solutions?

### GeoJSON
- [http://geojson.io](http://geojson.io)

### Terminology
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

### ArcGIS Layers
Let's learn about layers in ArcGIS!

- Go to ArcGIS Online
- Search for [traffic layers outside of your organization](http://slustl.maps.arcgis.com/home/search.html?q=traffic&t=content&start=1&sortOrder=desc&sortField=relevance&restrict=false&focus=layers-weblayers-features)
- Find [California Traffic Layers](http://slustl.maps.arcgis.com/home/search.html?q=traffic&t=content&start=1&sortOrder=desc&sortField=relevance&restrict=false&focus=layers-weblayers-features)
- Open up [the service](https://services1.arcgis.com/8CpMUd3fdw6aXef7/arcgis/rest/services/Vehicle_Traffic_Volumes_2016/FeatureServer)
- Let's query the service
- Notice you can return HTML, JSON (Esri JSON), GeoJSON, etc.
- Let's add this to a Webmap.
- Change the renderer to heatmap.
- Change renderer back to some class breaks and save the Webmap.

**What's the point of this?**
*That we did in Leaflet can be done without code. But you can code it now with Leaflet and will be able to with ArcGIS JavaScript!*

### How do we work with these in JavaScript?
#### From a WebMap
Let's start by creating an app from our traffic webmap
- Go to [Load a Basic WebMap](https://developers.arcgis.com/javascript/latest/sample-code/webmap-basic/index.html)
- Open in Sandbox
- Let's modify this to take your webmap
- Notice it even zooms over to the extent of your webmap?
- Play around with CSS and HTML parameters

#### From a Feature Layer
- Feature layers are probably the most prevalent layers
- Can be created from Portal Item or Service URL
- Let's edit the webmap example to use the Feature Service (ca_traffic_from_fl.html)
- What differences do you see between the webmap version and the heatmap version?

#### From an Imagery Layer
- Let's look at adding an imagery layer.
- Using the [Imagery Layers Intro](https://developers.arcgis.com/javascript/latest/sample-code/sandbox/index.html?sample=layers-imagerylayer)
- Open in Sandbox
- Let's change the imagery URL to the [Landsat 8 Views URL]("https://landsat2.arcgis.com/arcgis/rest/services/Landsat8_Views/ImageServer")

#### From a CSV
- Let's take a look at the [CSV Layer Example](https://developers.arcgis.com/javascript/latest/sample-code/layers-csv/index.html)
- From here, let's try to solve some problems ourselves!

## Classwork\Homework Problems:
1. Search through ArcGIS Online and find 2 layers that overlap (not including the basemap). Create two apps that show all two layers on the map. You choose the 2 layers from ArcGIS Online. 
**Part 1**
- Create one by adding the layers to the app [From a Webmap](https://developers.arcgis.com/javascript/latest/sample-code/webmap-basic/) and then loading the Webmap object into the ArcGIS Javascript API
- Start with the [Load a Basic Webmap Example](https://developers.arcgis.com/javascript/latest/sample-code/webmap-basic/)
- Create a Webmap in [http://slustl.maps.arcgis.com/home/index.html](http://slustl.maps.arcgis.com/home/index.html)
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

**Part 2**
- Using the same layers you added to the Webmap, create a web application by adding the layers as Feature Layers like in the [Intro to Feature Layer](https://developers.arcgis.com/javascript/latest/sample-code/layers-featurelayer/index.html) example.
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

2. Create a webapp that uses the [CSV Layer](https://developers.arcgis.com/javascript/latest/sample-code/layers-csv/index.html) to map crime over St. Louis from the [STL Crime CSV](https://github.com/gbrunner/Advanced_Python_for_GIS_and_RS/blob/master/Week%202/stl_crime_wgs_84.csv) in this folder.
- Start with the [CSV Layer example](https://developers.arcgis.com/javascript/latest/sample-code/layers-csv/index.html)
- Change the url to be:
```
var url = "https://raw.githubusercontent.com/gbrunner/Advanced_Python_for_GIS_and_RS/master/Week%202/stl_crime_wgs_84.csv";
```
- Change the renderer to be a *simple* renderer:
```
var symbol = {
   type: "simple-marker", 
   color:"red"
};

csvLayer.renderer = {
   type: "simple", // autocasts as new SimpleRenderer()
   symbol: symbol
};
```
- Change all the *SceneView* parameters to *MapView* parameters.
- Change the *center* and the *zoom* to be over St. Louis, MO.


3. Change the renderer in the crime map to a [heatmap renderer](https://developers.arcgis.com/javascript/latest/sample-code/visualization-heatmap/index.html). Have some fun. Change the colors!
- Starting from your code for **Problem 2**, after the last ```</style>```, add:
```
<script>
  var dojoConfig = {
    has: {
      "esri-featurelayer-webgl": 1
    }
  };
</script>
```
-  **Require** the legend:
```
    require([
      "esri/Map",
      "esri/layers/CSVLayer",
      "esri/views/MapView",
      "esri/config",
      "esri/core/urlUtils",
	  "esri/widgets/Legend",
      "dojo/domReady!"
    ], function(
      Map,
      CSVLayer,
      MapView,
      esriConfig,
      urlUtils,
	  Legend
    ) {
```
- Change the renderer:
```
const renderer = {
        type: "heatmap",
        colorStops: [
        {
          color: "rgba(63, 40, 102, 0)",
          ratio: 0
        },
        {
          color: "#472b77",
          ratio: 0.083
        },
        {
          color: "#4e2d87",
          ratio: 0.166
        },
        {
          color: "#563098",
          ratio: 0.249
        },
        {
          color: "#5d32a8",
          ratio: 0.332
        },
        {
          color: "#6735be",
          ratio: 0.415
        },
        {
          color: "#7139d4",
          ratio: 0.498
        },
        {
          color: "#7b3ce9",
          ratio: 0.581
        },
        {
          color: "#853fff",
          ratio: 0.664
        },
        {
          color: "#a46fbf",
          ratio: 0.747
        },
        {
          color: "#c29f80",
          ratio: 0.830
        },
        {
          color: "#e0cf40",
          ratio: 0.913
        },
        {
          color: "#ffff00",
          ratio: 1
        }],
        maxPixelIntensity: 100,
        minPixelIntensity: 1
      };
	  
```

- Set the template to be
```
const template = {
   title: "Crime committed at {ILEADSStreet}"
};
```
- Change the CSV layer parameters to be:
```
const csvLayer = new CSVLayer({
        url: "https://rawgit.com/gbrunner/Advanced_Python_for_GIS_and_RS/master/Week%202/stl_crime_wgs_84.csv",
        title: "St. Louis Crime Heatmap",
        copyright: "St. Louis Police Department",
		latitudeField:"Lat",
        longitudeField:"Lon",
		popupTemplate: template,
		renderer: renderer
});
```

4. (**Optional**) Following from this [server side raster function example](https://developers.arcgis.com/javascript/latest/sample-code/layers-imagery-popup/index.html), do the following:
- Change the service to point to the Landsat 8 Views Service (https://landsat2.arcgis.com/arcgis/rest/services/Landsat8_Views/ImageServer)
- Look at the service **RasterFunction Infos**. Change the Raster function template to one of the *NDVI* Raster Functions.
- Change the Zoom location to be over the Midwest.
- After you change it, does the *Popup* still work?
- If not, can you fix it? The Bands for Landsat 8 can be found [here](https://landsat.usgs.gov/what-are-band-designations-landsat-satellites). This data corresponds to the OLI sensor.

## Homework:
1. Finish the **Classwork\Homework Problems** and submit them as **Assignment 2**.
2. Read Chapters 4 and 5 of [Rubalcava](https://www.apress.com/us/book/9781484232811) on **API Core Fundamentals** and **Scenes**
3. Project 1 assigned!

## Helpful Links
- [Esri GeoDav Hacker Lab JSAPI samples](https://github.com/Esri/geodev-hackerlabs/tree/master/develop/jsapi)
- [Heatmap Renderer](https://developers.arcgis.com/javascript/latest/sample-code/visualization-heatmap/index.html)
- [Colors as Hex Codes](http://www.color-hex.com/)
