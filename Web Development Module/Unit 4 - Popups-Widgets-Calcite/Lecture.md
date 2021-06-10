# Preparation: 
1. Don't forget to work on Project 1.
2. Read Chapters 6 and 7 of Rubalcava. Chapter 7 can be a bit intimidating. Don't get concerned if you don't understand it. Rather than focus on creating widgets, we will focus on using them. After reading Chapter 7, please look at the following examples:
- [Legend Widget](https://developers.arcgis.com/javascript/latest/sample-code/widgets-legend/index.html)
- [Layer List Widget](https://developers.arcgis.com/javascript/latest/sample-code/widgets-layerlist-actions/index.html)
- [Search Widget](https://developers.arcgis.com/javascript/latest/sample-code/widgets-search-3d/index.html)

# Lecture 1 - Calcite, Popups, and Popup Template
## Calcite
- [JSAPI Themes](https://developers.arcgis.com/javascript/latest/styling/#themes)
- [Calcite Getting Started](http://esri.github.io/calcite-web/documentation/)
- [Calcite Buttons](http://esri.github.io/calcite-web/documentation/components/#buttons)

Here are the Calcite examples that I use:
- [calcite-buttons-and-themes](https://codepen.io/gbrunner/pen/VwmyMqP)
- [calcite-button-group](https://codepen.io/gbrunner/pen/gOLoGNo)
- [calcite-panel](https://codepen.io/gbrunner/pen/PobEOYR)


## The Easy Way - Add a Popup through ArcGIS Online
Popups are usually a users first interaction with a map.

Let's take a look at how we can add popups to our apps.

Let's get started by mapping NHL Draft Prospects!
[2017 NHL Draft Products](https://slustl.maps.arcgis.com/home/item.html?id=b427474f83b946efae5e5dd4bd021398)

We can find this Feature Layer by searching "NHL Draft" Feature Layers in ArcGIS Online.

Let's open this in a *New Map*.

Let's symbolize the players with a [puck](https://graphicriver.img.customer.envatousercontent.com/files/224145068/preview.jpg?auto=compress%2Cformat&q=80&fit=crop&crop=top&max-h=8000&max-w=590&s=60d4fe57e0a4ead05318f4b9ba91192a)

Let's change the *Basemap*

Next, let's conficure a popup!

After that, let's save the Webmap.

Let's share the Webmap with everyone too.

Let's load the webmap into a JS API App.

Now, let's go to the [Webmap Basic](https://developers.arcgis.com/javascript/latest/sample-code/webmap-basic/index.html) example, and switch the basemap ID.

Pretty easy, right?

Let's copy that code into an HTML file and save it before leaving.

### Final App
- [App in CodePen](https://codepen.io/gbrunner/pen/OJRQjYa)
- [App in GitHub](https://gbrunner.github.io/popup-from-webmap)
- [Code in GitHub](https://github.com/gbrunner/popup-from-webmap)

## Loading the Popup through Code using Popup Template
Let's open up the [Intro to Popup Tempate Example](https://developers.arcgis.com/javascript/latest/sample-code/sandbox/index.html?sample=intro-popuptemplate) and start there:

Let's change the feature service to be: [NHL Prospects](https://services2.arcgis.com/bB9Y1bGKerz1PTl5/arcgis/rest/services/NHL_Draft_Prospects_WFL1/FeatureServer)

Let's change the center map location to be:
```
center:[-90, 38],
zoom: 4
```
Now, let's change the *template* to reflect the feature service.

```
var template = { // autocasts as new PopupTemplate()
        title: "{Player} ({Position})",
        content: [{
          // It is also possible to set the fieldInfos outside of the content
          // directly in the popupTemplate. If no fieldInfos is specifically set
          // in the content, it defaults to whatever may be set within the popupTemplate.
          type: "fields",
          fieldInfos: [{
            fieldName: "Height",
            label: "Height: ",
            visible: true
          }, {
            fieldName: "Weight",
            label: "Weight: ",
            visible: true,
            format: {
              digitSeparator: true,
              places: 0
            }
          }, {
            fieldName: "Shot",
            label: "Shoots: ",
            visible: true,
            format: {
              digitSeparator: true,
              places: 0
            }
          }, {
            fieldName: "Team",
            label: "Team",
            visible: true,
            format: {
              digitSeparator: true,
              places: 0
            }
          }]
        }]
      };
```

Easy, right?!

### Final App
- [App in CodePen](https://codepen.io/gbrunner/pen/yLavzNY)
- [App in GitHub](https://gbrunner.github.io/popup-from-feature-layer)
- [Code in GitHub](https://github.com/gbrunner/popup-from-feature-layer)

## Now Let's Recreate the first Map's symbology, too!

Wee need to add a *renderer* and a *symbol*

**Our *Symbol***
```
 var symbol = {
      type: "picture-marker",  // autocasts as new PictureMarkerSymbol()
      url: "https://graphicriver.img.customer.envatousercontent.com/files/224145068/preview.jpg?auto=compress%2Cformat&q=80&fit=crop&crop=top&max-h=8000&max-w=590&s=60d4fe57e0a4ead05318f4b9ba91192a",
      width: "48px",
      height: "48px"
};
```
**Our *renderer***
```
var renderer = {
      type: "simple",  // autocasts as new SimpleRenderer()
      symbol: symbol
    };
```
**Our *Feature Layer***
```
var featureLayer = new FeatureLayer({
        url: "https://services2.arcgis.com/bB9Y1bGKerz1PTl5/arcgis/rest/services/NHL_Draft_Prospects_WFL1/FeatureServer",
        outFields: ["*"],
        renderer: renderer,
        popupTemplate: template
      });
      map.add(featureLayer);
```

### Final App
- [App in CodePen](https://codepen.io/gbrunner/pen/KKgQXVp)
- [App in GitHub](https://gbrunner.github.io/popup-from-feature-layer-with-puck)
- [Code in GitHub](https://github.com/gbrunner/popup-from-feature-layer-with-puck)

# Lecture 2 - Widgets
My focus is not to get you writing your own widgets. That is beyond my intended scope of this class. My emphasis is that I want you to be able to use widgets. To do that, we'll look at specific out of the box widgets that come with the **ArcGIS API for Javascript 4**.

## Home Button Widget - We Did This Last Week
Let's go back to Week 3 and look at the [World Population 3D CodePen](https://codepen.io/gbrunner/pen/JjRrxJx)

Notice, we used the home button and that was imported via
```
 "esri/widgets/Home",
 ```
 
 The implementation was very straightforward and only required a few lines of code:
 ```
var homeBtn = new Home({
    view: view
});
// Add the home button to the top left corner of the view
view.ui.add(homeBtn, "top-left");
```

Implementing widgets is generally this easy. 
- We import it. 
- We assign it properties. 
- And we put it on the user interface.

## Search Widget
Let's take the global population example we were looking at last week, remove the buttons, and add a search widget.

Let's look at the [Search Widget Example](https://developers.arcgis.com/javascript/latest/sample-code/widgets-search-3d/index.html)

All we have to do is add:
```
	  var searchWidget = new Search({
        view: view
      });

      // Add the search widget to the top right corner of the view
      view.ui.add(searchWidget, {
        position: "top-right"
      });
```

Easy, right?!

### Final App
- [App in CodePen](https://codepen.io/gbrunner/pen/wvzyrqw)
- [App in GitHub](https://gbrunner.github.io/world-population-3d-with-search)
- [Code in GitHub](https://github.com/gbrunner/world-population-3d-with-search)

## Legend Widget
Now, let's add a Legend!

Check out the [legend example](https://developers.arcgis.com/javascript/latest/sample-code/widgets-legend/index.html).

All we should need to do is add:
```
view.when(function() {
// get the first layer in the collection of operational layers in the WebMap
// when the resources in the MapView have loaded.
var featureLayer = scene.layers.getItemAt(0);

var legend = new Legend({
  view: view,
  layerInfos: [{
    layer: featureLayer,
    title: "World Population"
  }]
});

// Add widget to the bottom right corner of the view
view.ui.add(legend, "bottom-right");
```
Again, it's that easy! Now it's time for you to play!

### Final App
- [App in CodePen](https://codepen.io/gbrunner/pen/wvzyrqw)
- [App in GitHub](https://gbrunner.github.io/world-population-3d-with-legend)
- [Code in GitHub](https://github.com/gbrunner/world-population-3d-with-legend)

# Exercises
1. [Configure pop-ups](https://developers.arcgis.com/labs/javascript/configure-pop-ups/)
2. [Driving Directions](https://developers.arcgis.com/labs/javascript/driving-directions/)
3. [Search for an address](https://developers.arcgis.com/labs/javascript/search-for-an-address/)
4. [Find places](https://developers.arcgis.com/labs/javascript/find-places/)

# Classwork\Homework Problems:
First, do not forget to submit **Project 1**. For homework, complete **Problems 1 and 3** and **optionally, Problems 2 and 4**. Submit the link to your apps in either CodePen or GitHub Pages.

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
```
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
