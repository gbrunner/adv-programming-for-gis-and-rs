## Preparation: 
1. Don't forget to work on Project 1.
2. Read Chapters 6 and 7 of Rubalcava. Chapter 7 can be a bit intimidating. Don't get concerned if you don't understand it. Rather than focus on creating widgets, we will focus on using them. After reading Chapter 7, please look at the following examples:
- [Legend Widget](https://developers.arcgis.com/javascript/latest/sample-code/widgets-legend/index.html)
- [Layer List Widget](https://developers.arcgis.com/javascript/latest/sample-code/widgets-layerlist-actions/index.html)
- [Search Widget](https://developers.arcgis.com/javascript/latest/sample-code/widgets-search-3d/index.html)

## Lecture:
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

## Classwork Exercises:


## Classwork Problems:

## Homework:

