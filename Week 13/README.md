## Preparation: 

## Lecture:


## Classwork Exercises:


## Classwork Problems:
3. (**Optional**) In preparation for next week, add a popup to the ca_traffic_from_fl.html example. This can be done by definind a template:
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

