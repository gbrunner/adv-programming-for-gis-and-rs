## Preaparation
Watch Jacob Wasilkowski's lecture from April 2018.

## Lecture
### Let's Learn Leaflet!!!
Leaflet -> Is an open-source JavaScript library for interactive web maps. It's lightweight, simple, and flexible, and is probably the most popular open-source mapping library at the moment. Leaflet is developed by Vladimir Agafonkin (currently of MapBox) and other contributors.

**What Leaflet does:** "Slippy" maps with tiled base layers, panning and zooming, and feature layers that you supply. It handles various basic tasks like converting data to map layers and mouse interactions, and it's easy to extend with plugins. It will also work well across most types of devices. See Anatomy of a Web Map for an introduction to the most common kinds of web maps, which is what Leaflet is good for.

**What Leaflet does not do:** Provide any data for you! Leaflet is a framework for showing and interacting with map data, but it's up to you to provide that data, including a basemap. Leaflet is also not GIS, although it can be combined with tools like CartoDB for GIS-like capabilities. If you need total freedom of form, interaction, transitions, and map projections, consider working with something like D3.

Check out thie tutorial from [Maptime Boston](https://maptimeboston.github.io/leaflet-intro/) to learn more.

### Let's Get Started!
#### The Anatomy of a Web Mapping Application using Leaflet.
- HTML
  - HyperText Markup Language
  - Provides the layout for a webpage
  - Is at the core of every web page
- CSS
  - Whereas HTML was the basic structure of your website, CSS is what gives your entire website its style. 
  - slick colors, interesting fonts, and background images -> thanks to CSS
- Javascript
  - Programming language that lets web developers design interactive sites
  - Most of the dynamic behavior you'll see on a web page is thanks to JavaScrip
  - And it's become a lot more than this!!!
  
#### Our first Leaflet map
Let's use the Leaflet [Quick Start Guide](https://leafletjs.com/examples/quick-start/) to create our first map!

Let's do this in [JSBin](https://jsbin.com/)

Let's use the same example, but change the JS to be the following:
```
var mymap = L.map('mapid').setView([41.8781, -87.6298], 13);
L.tileLayer('http://a.tile.stamen.com/toner/{z}/{x}/{y}.png', {
    attribution: 'Map tiles by Stamen Design, under CC BY 3.0.',
    maxZoom: 18,
    id: 'mapbox.streets'
}).addTo(mymap);
```
What city are we centered over?

#### How does this look if we jam it into a single HTML file?
See quickstart.html

Let's complete the tutorial and see where we end up :)

### Working with Data in Leaflet
Data is read in [GeoJSON](http://geojson.org/) format, a format for encoding a variety of geographic data structures.

#### Let's Add Some Objects in GeoJSON format
Following from the leaflet tutorial, [let's add some features in GeoJSON format](https://leafletjs.com/examples/geojson/).

### Reading GeoJSON and Using it
1. Use the Boston GeoJSON example here. https://gbrunner.github.io/Advanced_Python_for_GIS_and_RS/Week%2011/boston_heatmap.html
2. Use the Chicago ZIPs example too to show polygons. https://gbrunner.github.io/Advanced_Python_for_GIS_and_RS/Week%2011/chicago_zips.html


### Powerful, fun capabilities of Leaflet

#### Leaflet Heatmap
Who doesn't like a *heatmap*?

Ever wonder how that works?

Demonstrate the Boston Heatmap example.

#### Leaflet Clustermap
Clustermaps are fun too!

Demonstrate the Boston Clustermap too. https://gbrunner.github.io/Advanced_Python_for_GIS_and_RS/Week%2011/boston_cluster.html

## Classwork Problems
1. Create a Leaflet map of 5 resturants that you'd like to go to in St. Louis. Include popups! If you're up to it, change the symbology for the points.
2. Create a Leaflet showing the San Francisco Crime points from the GeoJSON found [here](https://github.com/gbrunner/Advanced_Python_for_GIS_and_RS/blob/master/Week%201/sf_crime.geojson). Please add a relevant icon to the points. See the [Leaflet tutorial here](https://maptimeboston.github.io/leaflet-intro/) if you need help with that.
3. **Challenge** Create a Leaflet heatmap from the crime points GeoJSON that you used above.
4. **Challenge** Create a Leaflet cluster map from the crime points GeoJSON that you used above.

## Homework
1. Complete the classwork problems and submit them. If #1 and #2 were easy, please try to do #3 and\or #4.
2. Please read Chapters 1, 2, and 3 of [Introducing ArcGIS API 4 for Javascript](https://www.apress.com/us/book/9781484232811). Chapeters 1 and 2 are really short!

## Fun Links
Basemaps
- [Stamen Watercolor](http://a.tile.stamen.com/watercolor/{z}/{x}/{y}.png)
- [Stamen Terrain](http://a.tile.stamen.com/toner/{z}/{x}/{y}.png)
- [Stament Toner](http://a.tile.stamen.com/terrain/{z}/{x}/{y}.png)

[GeoJSON Viewer](https://github.com/gavinr/geojson-viewer)

[Convert CSV to GeoJSON](https://github.com/gavinr/csv-to-geojson)

[GeoJSON.io](http://geojson.io/)

[More than you ever wanted to know about GeoJSON](https://macwright.org/2015/03/23/geojson-second-bite.html#projections)

