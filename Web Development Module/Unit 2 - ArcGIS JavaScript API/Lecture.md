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

# How do we work with these in JavaScript?
## From a WebMap
Let's start by creating an app from our traffic webmap
- Go to [Load a Basic WebMap](https://developers.arcgis.com/javascript/latest/sample-code/webmap-basic/index.html)
- Open in Sandbox
- Let's modify this to take your webmap
- Notice it even zooms over to the extent of your webmap?
- Play around with CSS and HTML parameters

### Final App
- [App in CodePen](https://codepen.io/gbrunner/pen/MWjoKBG)
- [App in GitHub](https://gbrunner.github.io/my-first-app-refactored)
- [Code in GitHub](https://github.com/gbrunner/my-first-app-refactored)

## From a Portal Item
You can build a web app direcly from the portal item. This wep app will inherit the properties of the Portal Item. 
In this case, you can think of the Portal Item as the starting point for the app you want to create.

### Final App
- [App in CodePen](https://codepen.io/gbrunner/pen/LYRzRXg)
- [App in GitHub](https://gbrunner.github.io/add-layer-from-portal-item)
- [Code in GitHub](https://github.com/gbrunner/add-layer-from-portal-item)


## From a Feature Layer
- Feature layers are probably the most prevalent layers
- Can be created from Portal Item or Service URL
- Let's edit the webmap example to use the Feature Service (ca_traffic_from_fl.html)
- What differences do you see between the webmap version and the heatmap version?

### Final App
- [App in CodePen](https://codepen.io/gbrunner/pen/MWjEbwr)
- [App in GitHub](https://gbrunner.github.io/add-feature-layer)
- [Code in GitHub](https://github.com/gbrunner/add-feature-layer)

## From an Imagery Layer
- Let's look at adding an imagery layer.
- Using the [Imagery Layers Intro](https://developers.arcgis.com/javascript/latest/sample-code/sandbox/index.html?sample=layers-imagerylayer)
- Open in Sandbox
- Let's change the imagery URL to the [USA Forest Type URL]("https://landscape4.arcgis.com/arcgis/rest/services/USA_Forest_Type/ImageServer")

### Final App
- [App in CodePen](https://codepen.io/gbrunner/pen/yLazVOp)
- [App in GitHub](https://gbrunner.github.io/add-imagery-layer)
- [Code in GitHub](https://github.com/gbrunner/add-imagery-layer)

## From a CSV
- Let's take a look at the [CSV Layer Example](https://developers.arcgis.com/javascript/latest/sample-code/layers-csv/index.html)
- From here, let's try to solve some problems ourselves!

### Final App
- [App in CodePen](https://codepen.io/gbrunner/pen/zYKEoKm)
- [App in GitHub](https://gbrunner.github.io/add-csv-layer)
- [Code in GitHub](https://github.com/gbrunner/add-csv-layer)

## Loading a Web Scene
Next week, we will work with 3D scenes. If you are interested, you can get started using this example.

### Final App
- [App in CodePen](https://codepen.io/gbrunner/pen/dypVpjQ)
- [App in GitHub](https://gbrunner.github.io/intro-to-scene-view)
- [Code in GitHub](https://github.com/gbrunner/intro-to-scene-view)

# Helpful Links
- [Esri GeoDav Hacker Lab JSAPI samples](https://github.com/Esri/geodev-hackerlabs/tree/master/develop/jsapi)
- [Heatmap Renderer](https://developers.arcgis.com/javascript/latest/sample-code/visualization-heatmap/index.html)
- [Colors as Hex Codes](http://www.color-hex.com/)
