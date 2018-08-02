## Preparation: Please read Chapters 4, 5, and 6 or Rubalcava

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

#### Collections and Autocasting
Example
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

#### Final Thought: These concepts are hard to learn and understand without exploring them yourself!!!

### 3D Scenes


### Popups


## Classwork Problems:


## Homework:

