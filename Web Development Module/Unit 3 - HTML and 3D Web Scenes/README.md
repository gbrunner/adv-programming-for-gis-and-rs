# Preparation 
Please read Chapters 4 and 5 of Rubalcava

# [Unit 2 Homework Solutions](https://codepen.io/collection/DEBerg)
Here are this week's homework solutions in CodePen.

# [Unit 3 CodePen Samples](https://codepen.io/collection/nGLOVV)
Here are the code pen samples that I will use for Unit 3.

## Additional Samples
Here are some extra examples that I discussed:
- [Earthquakes](https://codepen.io/gbrunner/pen/jOVaQMg?editors=0010)
- [SF Rodents](https://codepen.io/gbrunner/pen/gOLwgaz)
- [SF Poop Map](https://www.arcgis.com/apps/View/index.html?appid=b6fab720912642b6aedafdb02a76d2a4)
- [3D St. Louis](https://www.arcgis.com/home/webscene/viewer.html?webscene=a7a868efc9f640009fc2d5352bad6879&viewpoint=cam:-90.18096388,38.62194316,533.188;312.322,65.934)

# Final Apps

## Accessors Final App
- [App in CodePen](https://codepen.io/gbrunner/pen/BaLwMLK)
- [App in GitHub](https://gbrunner.github.io/map-view-watcher)
- [Code in GitHub](https://github.com/gbrunner/map-view-watcher)

## 3D Final App
- [App in CodePen](https://codepen.io/gbrunner/pen/KKgXJav)
- [App in GitHub](https://gbrunner.github.io/autocast-webmap)
- [Code in GitHub](https://github.com/gbrunner/autocast-webmap)

## 3D Final App
- [App in CodePen](https://codepen.io/gbrunner/pen/JjRrxJx)
- [App in GitHub](https://gbrunner.github.io/world-population-3d)
- [Code in GitHub](https://github.com/gbrunner/world-population-3d)

## Home Button Final App
- [App in CodePen](https://codepen.io/gbrunner/pen/XWjeOxo)
- [App in GitHub](https://gbrunner.github.io/world-population-3d-with-home-button)
- [Code in GitHub](https://github.com/gbrunner/world-population-3d-with-home-button)

## More Buttons Final App
- [App in CodePen](https://codepen.io/gbrunner/pen/LYRzqeK)
- [App in GitHub](https://gbrunner.github.io/world-population-3d-with-buttons)
- [Code in GitHub](https://github.com/gbrunner/world-population-3d-with-buttons)

# Unit 3 Assignment

## Exercises
1. [Get map coordinates](https://developers.arcgis.com/labs/javascript/get-map-coordinates/)
2. [Display a web scene](https://developers.arcgis.com/labs/javascript/display-a-web-scene/)
3. [Add a layers to a 3D scene](https://developers.arcgis.com/labs/javascript/add-layers-to-a-3d-scene/)

## Homework Problems:
This week, please begin working on Project 1 and read Chapters 6 and 7 of Rubalcava. Chapter 7 can be a bit intimidating. Don't get concerned if you don't understand it. Rather than focus on creating widgets, we will focus on using them. After reading Chapter 7, please look at the following examples:
- [Legend Widget](https://developers.arcgis.com/javascript/latest/sample-code/widgets-legend/index.html)
- [Layer List Widget](https://developers.arcgis.com/javascript/latest/sample-code/widgets-layerlist-actions/index.html)
- [Search Widget](https://developers.arcgis.com/javascript/latest/sample-code/widgets-search-3d/index.html)

Complete the following problems and submit either a link to your CodePen or your application hosted on GitHub Pages:
1. Change the [world-population-3d-with-home-buttons CodePen](https://codepen.io/gbrunner/pen/XWjeOxo) to use this webscene over Boston as the input portal item: http://slustl.maps.arcgis.com/home/webscene/viewer.html?webscene=8046207c1c214b5587230f5e5f8efc77
- Open [world-population-3d-with-home-buttons](https://codepen.io/gbrunner/pen/XWjeOxo).
- change the ```id:"fbbbaa2fbfda41b8b3f96427c3ac5c79" ``` to be ```id:"8046207c1c214b5587230f5e5f8efc77" ```
- Change the camera position from looking at St. Louis, to looking at Boston:
```
        position: [
           -71.060217,
          42.382655,
          2500// elevation in meters
        ],
```

2. Change the two cameras to point at different areas of Boston. Modify the parameters of ```var camera``` and ```var camera2```.
- Modify the parameters in ```var camera``` and ```var camera2``` to point at different parts of boston. You might have to play around to get the views you want. 
- Be sure to change the names on the buttons from ```St. Louis, USA``` and ```Beijing, China``` to something more meaningful.

3. Add a third camera (and button!) that looks towards downtown boston from the Atlantic Ocean.
- Add a button in the ```<>body<>``` like:   
```<button id="v3" class="off">Downtown</button>```
- Add an event listener to listen to the button. Fill in the *???* with actual values.
```
    v3.addEventListener('click', function() {
      // reuse the default camera position already established in the homeBtn
      view.goTo({
        position: {
          x: ???,
          y: ???, 
          z: ???
        },
        tilt: ???,
        heading: ???
      });
    });
   ````
- Add ```v3``` to the array here:
```
[v1, v2].forEach(function(button) {
      button.style.display = 'flex';
      view.ui.add(button, 'top-right');
    });
```
- Try it!

4. Add a Home button that goes back to 42.3770° N, 71.1167° W or your initial MapView camera location.
- Import the *Home* button:
```
"esri/widgets/Home",
.
.
.
 ], function(WebScene, SceneView, Camera, Home) {
 ```
 - Define the *Home* button:
 ```
 var homeBtn = new Home({
        view: view
 });
 ```
- Add the *Home* button to the UI:
```view.ui.add(homeBtn, "top-left");```
- Make sure that the ```camera``` specified in the ```view``` points to where you expect:
```      
var view = new SceneView({
        container: "viewDiv",
        map: scene,
        camera: camera
});
```
- Try it out!

5. What happens if you try to set ```viewingMode = "local"```? Why do you think this happens? If you want to find out, go to arcgis online, create a *New Local Scene* and try to add the [Boston Buildings](https://services2.arcgis.com/cFEFS0EWrhfDeVw9/arcgis/rest/services/Boston_current_buildings/SceneServer). What message do you get?

6. (**Challenge**) In preparation for next week:
- Add a popup to the [ca-traffic-from-feature-layer](https://codepen.io/gbrunner/pen/GRjQYEz) CodePen. This can be done by defining a template:
```
		var template = { // autocasts as new PopupTemplate()
        title: "What Happened?",
        content: [{
          // It is also possible to set the fieldInfos outside of the content
          // directly in the popupTemplate. If no fieldInfos is specifically set
          // in the content, it defaults to whatever may be set within the popupTemplate.
          type: "fields",
          fieldInfos: [{
            fieldName: "CollisnTyp",
            label: "Collision Type",
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

fl.renderer = renderer
```

# Links
- [3D Scene with Lidar over St. Louis](https://www.arcgis.com/home/webscene/viewer.html?webscene=a7a868efc9f640009fc2d5352bad6879&viewpoint=cam:-90.18096388,38.62194316,533.188;312.322,65.934)
