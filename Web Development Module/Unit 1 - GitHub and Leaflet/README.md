# Github
## [What is GitHub?](https://www.youtube.com/watch?v=w3jLJU7DT5E)


Throughout this course, we will be using GitHub. 
If you are new to GitHub, please watch this video. 
If you are already familiar with it, I recommend 
you watch it anyway to expand your understanding of it. 
If you don't have an account yet, please create on at
[github.com](www.github.com).

## [What is GitHub Pages?](https://www.youtube.com/watch?v=2MsN8gpT6jY)

Have you ever created a web page? 
Did you know you can create web pages with GitHub and 
host them on GitHub? This video will teach you how 
and we will create our first web pages using GitHub 
during the first lecture.

Please watch this video to learn how to use GitHub 
pages to create and host a web page on GitHub. 
This will be how we create websites from our maps!


# [CodePen Examples for Unit 1](https://codepen.io/collection/XbJomQ)
All of the samples we will work with this week are in 
this CodePen folder. If you do not have a CodePen account,
I recommend that you create one and use it these first four weeks.

# [Leaflet Tutorial](https://leafletjs.com/)
Many of the examples I show you are taken from this Leaflet tutorial.
I highly recommend you take a look at this and follow some of the examples
beyond what we do here in class.

# [ArcGIS JavaScript API Samples](https://developers.arcgis.com/javascript/latest/sample-code/)
This is a link to the ArcGIS Javascript API samples. We will be working 
with these the first four weeks.

# [Awesome Leaflet Basemaps](https://leaflet-extras.github.io/leaflet-providers/preview/)
If you are looking for more basemap options for your Leaflet
maps, check out the basemaps [here](https://leaflet-extras.github.io/leaflet-providers/preview/).

# Forum: GitHub Account and Goals
Hi Class,
In the forum below, please share:
1. A link to your GitHub account
2. Two things you want to get out of taking this course.


# The Apps we will create today
- [First Web App in CodePen](https://codepen.io/gbrunner/pen/vYXJVLE?editors=1100)
- [First Web App as Stand Alone App in GitHub](https://gbrunner.github.io/my-first-app/), [Code](https://github.com/gbrunner/my-first-app)
- [First Web App in CodePen, Refactored](https://codepen.io/gbrunner/pen/MWjoKBG)
- [First Web App as Stand Alone App in GitHub, Refactored](https://gbrunner.github.io/my-first-app-refactored/), [Code](https://github.com/gbrunner/my-first-app-refactored)

# Let's Learn Leaflet!!!
Leaflet -> Is an open-source JavaScript library for 
interactive web maps. It's lightweight, simple, 
and flexible, and is probably the most popular 
open-source mapping library at the moment. 
Leaflet is developed by Vladimir Agafonkin 
(currently of MapBox) and other contributors.

**What Leaflet does:** "Slippy" maps with tiled base 
layers, panning and zooming, and feature layers that 
you supply. It handles various basic tasks like 
converting data to map layers and mouse interactions, 
and it's easy to extend with plugins. It will also 
work well across most types of devices. See Anatomy 
of a Web Map for an introduction to the most common 
kinds of web maps, which is what Leaflet is good for.

**What Leaflet does not do:** Provide any data for 
you! Leaflet is a framework for showing and interacting 
with map data, but it's up to you to provide that data, 
including a basemap. Leaflet is also not GIS, although 
it can be combined with tools like CartoDB for GIS-like 
capabilities. If you need total freedom of form, interaction, 
transitions, and map projections, consider working with 
something like D3.

Check out thie tutorial from 
[Maptime Boston](https://maptimeboston.github.io/leaflet-intro/) 
to learn more.

# The Anatomy of a Web Mapping Application using Leaflet.
- HTML
  - HyperText Markup Language
  - Provides the layout for a webpage
  - Is at the core of every web page
- CSS
  - Whereas HTML was the basic structure of your website, CSS is what gives your entire website its style. 
  - slick colors, interesting fonts, and background images -> thanks to CSS
- JavaScript
  - Programming language that lets web developers design interactive sites
  - Most of the dynamic behavior you'll see on a web page is thanks to JavaScript
  - And it's become a lot more than this!!!
  
 # GeoJSON
Data is read in [GeoJSON](http://geojson.org/) format, 
a format for encoding a variety of geographic data structures.

To learn more about GeoJSON, check out [GeoJSON.io](http://www.geojson.io)

  
# Our first Leaflet map
- Let's use the Leaflet [Quick Start Guide](https://leafletjs.com/examples/quick-start/) to create our first map!
- Let's do this in [CodePen](https://codepen.io/gbrunner/pen/yLaXYrg)
- Let's use the same example, but change the JS to be the following:
```
var mymap = L.map('mapid').setView([51.505, -0.09], 13);

L.tileLayer('http://a.tile.stamen.com/toner/{z}/{x}/{y}.png', {
        attribution: 'Map tiles by Stamen Design, under CC BY 3.0.',
        maxZoom: 18
}).addTo(mymap);
```
What city are we centered over?

# The Final Products & Applications
These are the apps that we are working towards

## First Leaflet App
- [Leaflet app in CodePen](https://codepen.io/gbrunner/pen/yLaoRqR)
- [Leaflet app in GitHub](https://gbrunner.github.io/my-first-leaflet-map/), [Code](https://github.com/gbrunner/my-first-leaflet-map)

Let's complete the tutorial and see where we end up :)

## Leaflet as a single file
- [Leaflet as a Single File](https://gbrunner.github.io/leaflet-app/), 
- [Code](https://github.com/gbrunner/leaflet-app)


## Leaflet from GeoJSON
Following from the Leaflet tutorial, [let's add some features in GeoJSON format](https://leafletjs.com/examples/geojson/).

- [GeoJSON Features in Leaflet in CodePen](https://codepen.io/gbrunner/pen/VwKMvyz)
- [GeoJSON Features in Leaflet in GitHub](https://github.com/gbrunner/leaflet-geojson-features-app)
- [GeoJSON Features in Leaflet Live](https://gbrunner.github.io/leaflet-geojson-features-app/)

## Leaflet from GeoJSON File
1. Use the Boston GeoJSON example here. https://gbrunner.github.io/Advanced_Python_for_GIS_and_RS/Week%2011/boston_heatmap.html
2. Use the Chicago ZIPs example too to show polygons. https://gbrunner.github.io/Advanced_Python_for_GIS_and_RS/Week%2011/chicago_zips.html

- [GeoJSON from File in Leaflet in CodePen](https://codepen.io/gbrunner/pen/oNzGjLY)
- [GeoJSON from File in Leaflet in GitHub](https://github.com/gbrunner/leaflet-geojson-from-file-app)
- [GeoJSON from File in Leaflet Live](https://gbrunner.github.io/leaflet-geojson-from-file-app/index.html)

## Leaflet Heatmap
Who doesn't like a heatmap?

- [Leaflet Heatmap in CodePen](https://codepen.io/gbrunner/pen/rNMGxGw)
- [Leaflet Heatmap in GitHub](https://github.com/gbrunner/leaflet-heatmap/)
- [Leaflet Heatmap Live](https://gbrunner.github.io/leaflet-heatmap/)

## Leaflet Clustermap
Clustermaps are fun too!

- [Leaflet Cluster Map in CodePen](https://codepen.io/gbrunner/pen/GRjMoxb)
- [Leaflet Cluster Map in GitHub](https://github.com/gbrunner/leaflet-cluster-map/)
- [Leaflet Cluster Map Live](https://gbrunner.github.io/leaflet-cluster-map/)

# Assignment 1
Complete the following problems and submit them as 
**Assignment 1**. If #1 and #2 were easy, please try 
to do #3 and\or #4. I am looking for you to use the examples 
we looked at today as your starting points. **Please submit to 
me links to working apps on GitHub! If you can't do that, 
submit links to your attempts to solve the problems in CodePen.**

Please read Chapters 1, 2, and 3 of 
[Introducing ArcGIS API 4 for JavaScript](https://www.apress.com/us/book/9781484232811). 
Chapeters 1 and 2 are really short!

1. Create a Leaflet map and **share it on GitHub** of 
5 restaurants that you'd like to go to in St. Louis. 
Include popups! If you're up to it, change the symbology for the points. 
*Hints:*
- look at [the leaflet geojson example](https://codepen.io/gbrunner/pen/VwKMvyz). 
- In quickstart_final.html, add 5 markers. For example:
```
var marker1 = L.marker([41.873, -87.629]).addTo(mymap);
var marker2 = L.marker([41.812, -87.628]).addTo(mymap);
.
.
.
```
- Bind a Popup to each one:
```
marker1.bindPopup("<b>Resturant 1</b><br>Spiros").openPopup();
marker2.bindPopup("<b>Resturant 2</b><br>Annie Gunns").openPopup();
.
.
.
```
- Remove the other markers (Circle, Polygon, etc.)

2. Create a Leaflet map and **share it on GitHub** showing the San Francisco Crime points from the GeoJSON found [here](https://github.com/gbrunner/Advanced_Python_for_GIS_and_RS/blob/master/Week%201/sf_crime.geojson). Please add a relevant icon to the points. See the [Leaflet tutorial here](https://maptimeboston.github.io/leaflet-intro/) if you need help with that.
*Hints:*
- Start with the [leaflet from geoJSON file example](https://codepen.io/gbrunner/pen/oNzGjLY) example.
- Change the ```view``` to be over San Francisco: ```var map = L.map('map').setView([37.7, -122.4], 10);```
- Change the basemap to a Stamen Basemap ```L.tileLayer('https://stamen-tiles-{s}.a.ssl.fastly.net/toner/{z}/{x}/{y}{r}.{ext}'``` that is listed below.
- Change ```$.getJSON("https://raw.githubusercontent.com/gbrunner/adv-python-for-gis-and-rs/master/Week%201/sf_crime.geojson",function(data){``` to look at the [sf_crime.geojson](https://github.com/gbrunner/Advanced_Python_for_GIS_and_RS/blob/master/Week%201/sf_crime.geojson) file
- Add the symbol following from the [leaflet tutorial](http://maptimeboston.github.io/leaflet-intro/) like:
```
 var ratIcon = L.icon({
    iconUrl: ''http://maptimeboston.github.io/leaflet-intro/rat.gif'',
    iconSize: [50,40]
  }); 
  L.geoJson(data  ,{
    pointToLayer: function(feature,latlng){
	  return L.marker(latlng,{icon: ratIcon});
    }
  } 
```

3. **Optional Challenge** Create a Leaflet heatmap from the crime points GeoJSON that you used above.
*Hints:*
- Start with [leaflet heatmap example](https://codepen.io/gbrunner/pen/rNMGxGw)
- Change the view of the map ```var map = L.map('map').setView([42.35, -71.08], 13);``` to be over San Francisco.
- Change the basemap to a Stamen Basemap ```L.tileLayer('http://tiles.mapc.org/basemap/{z}/{x}/{y}.png'``` that is listed below.
- Change *rodents.geojson* to the [sf_crime.geojson](https://github.com/gbrunner/Advanced_Python_for_GIS_and_RS/blob/master/Week%201/sf_crime.geojson)

4. **Optional Challenge** Create a Leaflet cluster map from the crime points GeoJSON that you used above. Make sure you have a default icon set. Can you change the color on the clusters?
- Start with [leaflet-cluster-map example](https://codepen.io/gbrunner/pen/GRjMoxb)
- Change the view of the map ```var map = L.map('map').setView([42.35, -71.08], 13);``` to be over San Francisco.
- Change the basemap to a Stamen Basemap ```L.tileLayer('http://tiles.mapc.org/basemap/{z}/{x}/{y}.png'``` that is listed below.
- Change *rodents.geojson* to the [sf_crime.geojson](https://raw.githubusercontent.com/gbrunner/adv-python-for-gis-and-rs/master/Week%201/sf_crime.geojson)
- Change the icon url ```iconUrl: 'http://andywoodruff.com/maptime-leaflet/rat.png',```. Search the internet for an icon or [use the one that I found](https://effect.org/wp-content/uploads/2016/01/crime-icon.png).


# If you finish this in class, there's one more thing I want to show you
[Esri Leaflet Examples](https://github.com/Esri/geodev-hackerlabs/tree/master/develop/leaflet)


# Fun Links
Basemaps from Stamen Design http://maps.stamen.com
- [Stamen Watercolor](http://maps.stamen.com/#watercolor) `https://stamen-tiles.a.ssl.fastly.net/watercolor/{z}/{x}/{y}.png`
- [Stamen Toner](http://maps.stamen.com/#toner) `https://stamen-tiles.a.ssl.fastly.net/toner/{z}/{x}/{y}.png`
- [Stamen Terrain](http://maps.stamen.com/#terrain) `https://stamen-tiles.a.ssl.fastly.net/terrain/{z}/{x}/{y}.png`
- [Coca-Cola from Stamen Watercolor](http://a.sm.mapstack.stamen.com/(watercolor,$eb0000[hsl-color])[soft-light]/0/0/0.png) ```http://a.sm.mapstack.stamen.com/(watercolor,$eb0000[hsl-color])[soft-light]/{z}/{x}/{y}.png```

[GeoJSON Viewer](https://github.com/gavinr/geojson-viewer)

[Convert CSV to GeoJSON](https://github.com/gavinr/csv-to-geojson)

[GeoJSON.io](http://geojson.io/)

[More than you ever wanted to know about GeoJSON](https://macwright.org/2015/03/23/geojson-second-bite.html#projections)

[Esri-Leaflet](https://esri.github.io/esri-leaflet/examples/) - Use Esri services with Leaflet. Probably a more advanced topic, but something you should know about.

[Awesome Leaflet Basemaps](https://leaflet-extras.github.io/leaflet-providers/preview/)
