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

#### Pomises
The evolution of event listeners.
Back in my day, we had events listeners, functions like:


At ArcGIS Javascript API 4, *promises* tell you when an action is complete or when something is ready

#### TypeScript Integraion - Don't worry about this right now...

#### Final Thought: These concepts are hard to learn and understand without exploring them yourself!!!

### 3D Scenes



## Classwork Problems:

4. (**Optional**) In preparation for next week, add a popup to the ca_traffic_from_fl.html example. This can be done by definind a template:
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


## Homework:

