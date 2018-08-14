## Preparation: Please read Chapters 4 and 5 of Rubalcava

## Lecture:
### API Core Concepts

#### Accessors
- Used to *get* and *set* properties
- Rather than listening for events, you watch for changes
- So instead of having functions like:
  - onClick
  - onSelect
- We have 
  - .on("value-change", ...
  - .watch("value",...
  
Example, let's plug this code into the [Intro to MapView](https://developers.arcgis.com/javascript/latest/sample-code/intro-mapview/index.html) example:
```
view.watch("center, scale", (value, oldValue, propertyName)=>{
  if (propertyName === "center"){
    console.log(value.x, value.y);
  } else {
    console.log("New Value: "+value);
    console.log("Old Value: "+oldValue);
  }
});
```
**Cool! But different than Python, right?!**

#### watchUtils
Taken deeper, here we have an example where we watch a scene and update the overview map based on the scene extent.
[Overview Map](https://developers.arcgis.com/javascript/latest/sample-code/overview-map/index.html)

#### Autocasting - Passing data that looks like a certain type into that type.
Autocasting a Portal Item as a Webmap
Let's modify the [Intro to MapView](https://developers.arcgis.com/javascript/latest/sample-code/intro-mapview/index.html) code again!
```
"esri/WebMap
.
.
.
WebMap

var webmap = new WebMap({
  portalItem:{
     id:"4be43a7b42ef4320bf995e490dbad21b"
  }
});
```
#### Collections - Array like containers of data
**Example**
- [Graphic collection](https://developers.arcgis.com/javascript/latest/sample-code/layers-featurelayer-collection/index.html)
- Reads GeoJSON, converts to esri/Graphic collection, renders them on map.
- Autocasts the GeoJSON graphics into an array that becomes a feature service.
- Relating back to Python, C++, etc., in those languages, if we hat a number that was a string, but was really an integer, we would have to cast that string to an integer as follows
```
number_as_string = 1600
number = int(number_as_string)
```

#### [Promises](https://www.youtube.com/watch?v=H8Q83DPZy6E)
Different concept from event listeners, but very important and increasingly used throughough JavaScript web development.

At ArcGIS Javascript API v4 *promises* tell you when an "asynchronous" action is complete, or in other words, when a result is ready from some action that occurred over an unknown amount of time.  We call this "fulfilling" a promise.  If something fails along the way, we call this "rejecting" a promise.

For example, consider network traffic (network requests) to fetch data from a server. The outgoing request and the incoming data that you want to render on a web map takes time to complete. There's never a predictable guarantee of how long it will take to get back to your browser, if it even finishes successfully at all. A promise will be fulfilled when this example data is back in your arms after traveling all around the wilds of the Internet.

Event listeners can also be used sometimes in these situations, but the trend now is to differentiate a lot more between promises and event listeners.  One good way to think about event listeners is to use them as mechanisms for responding to user actions. They sit around and wait for an event to occur. For example, when the user of your website clicks their mouse on a button, then you respond to that action with more custom code inside of a click event listener.

#### TypeScript Integraion - Don't worry about this right now...

#### Final Thought: These concepts are hard to learn and understand without exploring them yourself!!!

### 3D Scenes
3D is probably the most exciting development\addition to the GIS web developer experience.

Opens up the ability to view 3D globes, scenes, and Lidar!

Loading a WebScene is ver easy. It follows the same pattern as loading a WebMap.

Let's create our first scene by building on top of the [SceneView Example](https://developers.arcgis.com/javascript/latest/sample-code/intro-sceneview/index.html)

FOr this example, let's use the [World Population in 3D Data](http://slustl.maps.arcgis.com/home/item.html?id=fbbbaa2fbfda41b8b3f96427c3ac5c79)
```
<script>
    require([
      "esri/WebScene",
      "esri/views/SceneView",
      "dojo/domReady!"
    ], function(WebScene, SceneView) {

      /*var map = new Map({
        basemap: "streets",
        ground: "world-elevation"
      });*/
      var scene = new WebScene({
        portalItem:{
         id:"fbbbaa2fbfda41b8b3f96427c3ac5c79" 
        }
      });

      var view = new SceneView({
        container: "viewDiv",
        map: scene
      });

    });
  </script>
  ```
Cool! Right?
Let's say we want to change the viewing mode. All we have to do is add:
```
var view = new SceneView({
    container: "viewDiv",
    map: scene,
		viewingMode:'local'
});
```

#### Camera Property
I think Rubalcava's camera property is a bit overkill. Instead, let's add some cameras to our worl population example.

Let's add a camera over st. louis on the world population scene:
```
camera: {
        position: [
          -90.1994, // lon
          38.6270, // lat
          5000000// elevation in meters
        ],

      heading: 0
      }
```
What happens when we modify the elevation?
What happens when we change the heading?

Let's add in a *tilt* parameter
```
position: [
          -90.1994, // lon
          38.6270, // lat
          5000000// elevation in meters
        ],
tilt:30,
```
Now, let's create an app that has some buttons to drive the cameras.
Walk through the world_pop_3d_w_buttons.html example.

#### Environment
Notice how the lighting goes right through the middle of the globe? **Let's fix that by adding an environment parameter**

Here's we'll add  alighting paramter to the SceneView that allows us to view the lighting so as to reflect the current tie of day.
```
var view = new SceneView({
        container: "viewDiv",
        map: scene,
        camera: camera,
        environment: {
            lighting: {
              date: new Date(),
              directShadowsEnabled: true,
              // don't update the view time when user pans.
              // The clock widget drives the time
              cameraTrackingEnabled: false
            }
        },
    });
```
There is a lot more we can do with this. Check out the samples!

#### Local Scenes
Let's change this to a local scene:
```
viewingMode:"local",
```
Does the lighting matter anymore?
Do the buttons still work?

#### Home Button
Let's add a *Home* button:
```
"esri/widgets/Home",
.
.
.
 ], function(WebScene, SceneView, Camera, Home) {
 .
 .
 .
 var homeBtn = new Home({
        view: view
      });

      // Add the home button to the top left corner of the view
    view.ui.add(homeBtn, "top-left");
```
That's all we have to do. Of course, we should change the home location to be different from the St. Louis, USA button :)


## Classwork Problems:
1. Change the world_pop_3d_w_buttons.html to use this webscene over Boston as the input portal item: http://slustl.maps.arcgis.com/home/webscene/viewer.html?webscene=8046207c1c214b5587230f5e5f8efc77

2. Change the two cameras to point at different areas of Boston.

3. Add a third camera (and button!) that looks towards downtown boston from the Atlantic Ocean.

4. Add a Home button that goes back to 42.3770° N, 71.1167° W or your initial MapView camera location.

5. What happens if you try to set ```viewingMode = "local"```? Why do you think this happens? If you want to find out, go to arcgis online, create a *New Local Scene* and try to add the [Boston Buildings](https://services2.arcgis.com/cFEFS0EWrhfDeVw9/arcgis/rest/services/Boston_current_buildings/SceneServer). What message do you get?

6. (**Challenge**) In preparation for next week:
- Add a popup to the [ca_traffic_from_fl.html](https://github.com/gbrunner/Advanced_Python_for_GIS_and_RS/blob/master/Week%202/ca_traffic_from_fl.html) example. This can be done by defining a template:
```
var template = { // autocasts as new PopupTemplate()
        title: "What Happened?",
        content: [{
          // It is also possible to set the fieldInfos outside of the content
          // directly in the popupTemplate. If no fieldInfos is specifically set
          // in the content, it defaults to whatever may be set within the popupTemplate.
          type: "fields",
          fieldInfos: [{
            fieldName: "Descriptn",
            label: "Description %",
            visible: true
          }]
        }]
      };
```
and adding these fields to the FeatureLayer definition.
```
outFields: ["*"],
popupTemplate: template
```
- Change the symbology by defining the renderer in the feature layer from this renderer:
```
var symbol = {
  type: "simple-marker", 
  color:"red"
};
var renderer = {
  type: "simple",  // autocasts as new SimpleRenderer()
  symbol: symbol
};
```

## Homework:
1. Complete this week's problems and submit them as **Assignment 3**.
2. Work on Project 1.
3. Read Chapters 6 and 7 of Rubalcava. Chapter 7 can be a bit intimidating. Don't get concerned if you don't understand it. Rather than focus on creating widgets, we will focus on using them. After reading Chapter 7, please look at the following examples:
- [Legend Widget](https://developers.arcgis.com/javascript/latest/sample-code/widgets-legend/index.html)
- [Layer List Widget](https://developers.arcgis.com/javascript/latest/sample-code/widgets-layerlist-actions/index.html)
- [Search Widget](https://developers.arcgis.com/javascript/latest/sample-code/widgets-search-3d/index.html)

## Links
- [3D Scene over St. Louis](http://www.arcgis.com/home/webscene/viewer.html?webscene=cdf7b9d41f1440068543cce2bb62ce7a)
