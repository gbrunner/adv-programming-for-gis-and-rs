# Preparation: 
1. Don't forget to work on Project 1.
2. Read Chapters 6 and 7 of Rubalcava. Chapter 7 can be a bit intimidating. Don't get concerned if you don't understand it. Rather than focus on creating widgets, we will focus on using them. After reading Chapter 7, please look at the following examples:
- [Legend Widget](https://developers.arcgis.com/javascript/latest/sample-code/widgets-legend/index.html)
- [Layer List Widget](https://developers.arcgis.com/javascript/latest/sample-code/widgets-layerlist-actions/index.html)
- [Search Widget](https://developers.arcgis.com/javascript/latest/sample-code/widgets-search-3d/index.html)

# [Unit 3 Homework Solutions](https://codepen.io/collection/ABgJqj)
Here are the links to the Unit 3 homework solutions in CodePen.

# [Unit 4 CodePen Samples](https://codepen.io/collection/DYkvrV)
Here are the unit 4 examples for this week.

# Esri Calcite
- [JSAPI Themes](https://developers.arcgis.com/javascript/latest/styling/#themes)
- [Calcite Getting Started](http://esri.github.io/calcite-web/documentation/)
- [Calcite Buttons](http://esri.github.io/calcite-web/documentation/components/#buttons)

These calcite examples are included in the CodePen samples. Here are the Calcite examples that I use:
- [calcite-buttons-and-themes](https://codepen.io/gbrunner/pen/VwmyMqP)
- [calcite-button-group](https://codepen.io/gbrunner/pen/gOLoGNo)
- [calcite-panel](https://codepen.io/gbrunner/pen/PobEOYR)

# Final Apps
## Hockey Draft Picks Final App
- [App in CodePen](https://codepen.io/gbrunner/pen/OJRQjYa)
- [App in GitHub](https://gbrunner.github.io/popup-from-webmap)
- [Code in GitHub](https://github.com/gbrunner/popup-from-webmap)

## Popup Template Final App
- [App in CodePen](https://codepen.io/gbrunner/pen/yLavzNY)
- [App in GitHub](https://gbrunner.github.io/popup-from-feature-layer)
- [Code in GitHub](https://github.com/gbrunner/popup-from-feature-layer)

## Popup Final App
- [App in CodePen](https://codepen.io/gbrunner/pen/KKgQXVp)
- [App in GitHub](https://gbrunner.github.io/popup-from-feature-layer-with-puck)
- [Code in GitHub](https://github.com/gbrunner/popup-from-feature-layer-with-puck)

## Search Final App
- [App in CodePen](https://codepen.io/gbrunner/pen/wvzyrqw)
- [App in GitHub](https://gbrunner.github.io/world-population-3d-with-search)
- [Code in GitHub](https://github.com/gbrunner/world-population-3d-with-search)

### Legend Final App
- [App in CodePen](https://codepen.io/gbrunner/pen/wvzyrqw)
- [App in GitHub](https://gbrunner.github.io/world-population-3d-with-legend)
- [Code in GitHub](https://github.com/gbrunner/world-population-3d-with-legend)

# Unit 4 Assignment

## Exercises
1. [Configure pop-ups](https://developers.arcgis.com/labs/javascript/configure-pop-ups/)
2. [Driving Directions](https://developers.arcgis.com/labs/javascript/driving-directions/)
3. [Search for an address](https://developers.arcgis.com/labs/javascript/search-for-an-address/)
4. [Find places](https://developers.arcgis.com/labs/javascript/find-places/)

## Classwork\Homework Problems:
First, do not forget to submit **Project 1**. 
For homework, complete **Problems 1 and 3** and **optionally, 
Problems 2 and 4**. Submit the link to your apps in either CodePen or GitHub Pages.

1. Starting from the [popup-from-feature-layer example](https://codepen.io/gbrunner/pen/yLavzNY), create an app that shows the STL Neighborhoods with a Popup:
- Use the [STL Neighborhoods Feature Layer](https://services2.arcgis.com/bB9Y1bGKerz1PTl5/ArcGIS/rest/services/STL_Neighborhood/FeatureServer/0)
- Starting with the  [popup-from-feature-layer example](https://codepen.io/gbrunner/pen/yLavzNY), comment out the *renderer*:
```
/*featureLayer.renderer = {
      type: "simple",  // autocasts as new SimpleRenderer()
      symbol: {
        type: "simple-marker",  // autocasts as new SimpleMarkerSymbol()
        size: 6,
        color: "red",
        outline: {  // autocasts as new SimpleLineSymbol()
          width: 0.5,
          color: "white"
        }
      }
    };*/
```
- Change the URL to ```https://services2.arcgis.com/bB9Y1bGKerz1PTl5/ArcGIS/rest/services/STL_Neighborhood/FeatureServer/0```
- Change the zoom and center to be over St. Louis:
```
        center:[-91.1, 38.6],
        zoom: 9
```
-  Modify the template title to be:
```         
title: "Neighborhood: {NHD_NAME}",
```
- Modify the template ```content``` to be print different field values.

- Change the title: ```<title>Intro to PopupTemplate - 4.8</title>```

2. (**Optional**) Do this with another STL dataset:
- [St. Louis School Districts](http://slustl.maps.arcgis.com/home/item.html?id=cb8c591911fc4e3090b1371cb0f4ba87)

3. Add the Legend Widget and Layer List Widget to the [3D Boston Planning](http://slustl.maps.arcgis.com/home/webscene/viewer.html?webscene=8046207c1c214b5587230f5e5f8efc77) Exameple that we made last week. Use the file [boston-globe-starting-point CodePen](https://codepen.io/gbrunner/pen/LYRQzNe) as your starting point.
- Let's start with the [Legend Widget](https://developers.arcgis.com/javascript/latest/sample-code/widgets-legend/index.html)
- Add ```"esri/widgets/Legend",``` to the ```require``` statement.
- Add ```Legend``` into the ```function(...)``` after ```Camera```
- Add a ```view.when``` function to create the legend and a ```view.ui.add(legend, "bottom-right");``` to add it to the interface:
```
view.when(function() {
	
          // get the first layer in the collection of operational layers in the WebMap
          // when the resources in the MapView have loaded.
        var featureLayer = scene.layers.getItemAt(1);

        var legend = new Legend({
          view: view,
          layerInfos: [{
            layer: featureLayer,
            title: "Major project buildings"
          }]
        });
      
   view.ui.add(legend, "bottom-right");
   });
```
- Next, add the [Layer List Widget](https://developers.arcgis.com/javascript/latest/sample-code/widgets-layerlist/index.html)
- Add ```"esri/widgets/LayerList",``` to the require statement after the Lenged.
- Add ```LayerList``` into the ```function(...)``` after the ```Legend```.
- Add the ```layerList``` withing the same ```view.when(function() {``` that you put the **Legend** within.
```
var layerList = new LayerList({
  view: view
});
```
- Add the Layer List to the UI. Do this within the ```view.when``` function:
```view.ui.add(layerList, "bottom-right");```


4. (**Optional**) Take a look at the other widget examples on the [Sample Widget Page](https://developers.arcgis.com/javascript/latest/sample-code/index.html?search=Widget). Add two of the following widgets to an existing sample that we have worked on in Week 2, 3, or 4.
- [Scale Bar Widget](https://developers.arcgis.com/javascript/latest/sample-code/widgets-scalebar/index.html)
- [Custom Basemap Widget](https://developers.arcgis.com/javascript/latest/sample-code/basemap-custom/index.html)
- [Expand Widget](https://developers.arcgis.com/javascript/latest/sample-code/widgets-expand/index.html)
- [Any of the other samples](https://developers.arcgis.com/javascript/latest/sample-code/index.html?search=Widget) that use widgets that you want to play with!
