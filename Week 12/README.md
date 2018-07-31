## Preparation: 
1. Please read Chapters 1, 2, and 3 of [Introducing ArcGIS API 4 for Javascript](https://www.apress.com/us/book/9781484232811). Chapeters 1 and 2 are really short!
2. Samples for the book can be found on [Github](https://github.com/Apress/introducing-arcgis-api-4-for-javascript/tree/master/intro-arcgis-js-api-4)

## Lecture:
### Terminology
- [ArcGIS API for Javascript](https://developers.arcgis.com/javascript/)
- [Assynchronous Module Definition](https://requirejs.org/docs/whyamd.html)
- [Dojo](https://dojotoolkit.org/) - Javascript toolkit that aids in development. Provides everything you need to build a WebApp.
- [Maps](https://developers.arcgis.com/javascript/latest/sample-code/intro-mapview/index.html)
- [Layers](https://developers.arcgis.com/javascript/latest/sample-code/layers-portal/index.html)
- [Views](https://developers.arcgis.com/javascript/latest/sample-code/scene-goto/index.html)
- Accessors - As a general term, functions that get something for you
- [Promises](https://developers.google.com/web/fundamentals/primers/promises) - Promises for assynchronous operations.
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

- Go to ArcGIS ONline
- Search for [traffice layers outside of your organization](http://slustl.maps.arcgis.com/home/search.html?q=traffic&t=content&start=1&sortOrder=desc&sortField=relevance&restrict=false&focus=layers-weblayers-features)
- Find [California Traffic Layers](http://slustl.maps.arcgis.com/home/search.html?q=traffic&t=content&start=1&sortOrder=desc&sortField=relevance&restrict=false&focus=layers-weblayers-features)
- Open up [the service](https://services1.arcgis.com/8CpMUd3fdw6aXef7/arcgis/rest/services/Vehicle_Traffic_Volumes_2016/FeatureServer)
- Let's query the service
- Notice you can return HTML, JSON (Esri JSON), GeoJSON, etc.
- Let's add this to a Webmap.
- Change the renderer to heatmap.
- Change renderer back to some class breaks and save the Webmap.
**What's the point of this?**
*That we did in Leaflet can be done without code. But you can code it now with Leaflet and will be able to with ArcGIS Javasctipt!*

### How do we work with these in Javascript?



## Classwork Exercises:


## Classwork Problems:

## Homework:

