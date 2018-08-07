## Preparation: 
1. Don't forget to work on Project 1.
2. Read Chapters 6 and 7 of Rubalcava. Chapter 7 can be a bit intimidating. Don't get concerned if you don't understand it. Rather than focus on creating widgets, we will focus on using them. After reading Chapter 7, please look at the following examples:
- [Legend Widget](https://developers.arcgis.com/javascript/latest/sample-code/widgets-legend/index.html)
- [Layer List Widget](https://developers.arcgis.com/javascript/latest/sample-code/widgets-layerlist-actions/index.html)
- [Search Widget](https://developers.arcgis.com/javascript/latest/sample-code/widgets-search-3d/index.html)

## Lecture 1 - Popups and Popup Template
Popups are ususally a uses first interaction with a map.

Let's take a look at how we can add popups to our apps.

### The Easy Way - Add a Popup through ArcGIS Online
Let's get started by mapping NHL Draft Prospects!
[2017 NHL Draft Products](http://slustl.maps.arcgis.com/home/item.html?id=d071140cea6c44818fc19a583bebf716)

We can find this Feature Layer by searching "NHL Draft" Feature Layers in ArcGIS Online.

Let's open this in a *Mew Map*.

Let's symbolize the players with a [puck](https://www.hockeyshot.ca/media/catalog/product/cache/3/image/9df78eab33525d08d6e5fb8d27136e95/b/l/black-puck.jpg)

Let's change the *Basemap*

Next, let's conficure a popup!

After that, let's save the Webmap.

Let's share the Webmap with everyone too.

Let's load the webmap into a JS API App.

Now, let's go to the [Webmap Basic](https://developers.arcgis.com/javascript/latest/sample-code/webmap-basic/index.html) example, and switch the basemap ID.

Pretty easy, right?

Let's copy that code into an HTML file and save it before leaving.

### Loading the Popup through Code using Popup Template
Let's open up the Popup teamplate Basic Example and start there:

Let's change the feature service to be: [NHL Prospects](https://services7.arcgis.com/fX3LzGegyrqMlv6s/ArcGIS/rest/services/2017NHLDraftProspects/FeatureServer/0)

Let's change the center map location to be:
```
center:[-90, 38],
zoom: 4
```
Now, let's change the *template* to reflect the feature service.

Easy, right?!

#### Now Let's Recreate the first Map's symbology, too!

Wee need to add a *renderer* and a *symbol*

**Our *Symbol***
```
 var symbol = {
      type: "picture-marker",  // autocasts as new PictureMarkerSymbol()
      url: "https://www.hockeyshot.ca/media/catalog/product/cache/3/image/9df78eab33525d08d6e5fb8d27136e95/b/l/black-puck.jpg",
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
        url: "https://services7.arcgis.com/fX3LzGegyrqMlv6s/ArcGIS/rest/services/2017NHLDraftProspects/FeatureServer/0",
        outFields: ["*"],
        renderer: renderer,
        popupTemplate: template
      });
      map.add(featureLayer);
```

## Lecture 2 - Widgets
My focus is not to get you writing your own widgets. That is beyond my intended scope of this class. My emphasis is that I want you to be able to use widgets. To do that, we'll look at specific out of the box widgets that come with the **ArcGIS API for Javascript 4**.

### Home Button Widget
Let's go back to Week 3 and look at the [3D Global Population app](https://gbrunner.github.io/Advanced_Python_for_GIS_and_RS/Week%203/world_pop_3d_w_home.html)

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

### Search Widget

### Legend Widget

### Layer Toggle Widget

## Classwork\Homework Problems:
1. Search ArcGIS Online for a feature layer of some data that you are interested in.  Take that feature layer, add it to a webmap, change the symbology, and create a popup for it. Then, following from the **The Easy Way...** lesson above, create a stad-alone application from that layer similar to the *popup_from_webmap_nhl.html* example.

If you are stuggling to find a feature layer, take a look at:
- [STL Neighborhoods](http://slustl.maps.arcgis.com/home/item.html?id=70fefcbe59ea421da9169a46b341dfa9)
- [St. Louis School Districts](http://slustl.maps.arcgis.com/home/item.html?id=cb8c591911fc4e3090b1371cb0f4ba87)
- [St. Louis Parishes](http://slustl.maps.arcgis.com/home/item.html?id=ebb8787f96424ea88649e228f2dcfef5)

*That's a lot of STL themed data...*

2. Use that same feature layer and create the same webapp and popup following from the *popup_from_fl_with_symbol.html*.

3. Add the following two widgets to the [3D Boston Planning](http://slustl.maps.arcgis.com/home/webscene/viewer.html?webscene=8046207c1c214b5587230f5e5f8efc77) Exameple that we made last weel.
- [Legend Widget](https://developers.arcgis.com/javascript/latest/sample-code/widgets-legend/index.html)
- [Layer List Widget](https://developers.arcgis.com/javascript/latest/sample-code/widgets-layerlist/index.html)

4. Take a look at the other widget examples on the [Sample Widget Page](https://developers.arcgis.com/javascript/latest/sample-code/index.html?search=Widget). Add a two of the following widgets to an existing sample that we have worked on in Week 2, 3, or 4.
- [Scale Bar Widget](https://developers.arcgis.com/javascript/latest/sample-code/widgets-scalebar/index.html)
- [Custom Basemap Widget](https://developers.arcgis.com/javascript/latest/sample-code/basemap-custom/index.html)
- [Expand Widget](https://developers.arcgis.com/javascript/latest/sample-code/widgets-expand/index.html)
- [Any of the other samples](https://developers.arcgis.com/javascript/latest/sample-code/index.html?search=Widget) that use widgets taht you want to play with!

## Homework:
1. Finish the **Problems** above.
2. Submit **Project 1!**
3. Read **Chapter 1** of **Mastering Geospatial Analysis with Python.** If you don't have the book, I will provide the chapter on **Blackboard**

