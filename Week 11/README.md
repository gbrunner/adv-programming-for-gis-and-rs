# Plotting with JavaScript

November 2018

Jacob Wasilkowski, <https://jwasilgeo.github.io>

## Background

- Review HTML &amp; JavaScript class activities from first few weeks of the semester.

- Review your experience so far with Python charting (e.g. `matplotlib`, `seaborn`) to see how it compares to charting your data in the web.

- Review April 2018 lecture: [Web Mapping Development Intro](https://github.com/gbrunner/Python_for_GIS_and_RS/tree/master/Week_14)

## Lecture

### Charting in the web with 2D graphics

Bookmark: <https://developer.mozilla.org/en-US/docs/Web/Guide/Graphics>

### Choose your own adventure: SVG or Canvas?

[Option 1: SVG `<svg>`](https://developer.mozilla.org/en-US/docs/Web/SVG)

> Scalable Vector Graphics (SVG) is an XML-based markup language for describing two dimensional based  vector graphics. SVG is essentially to graphics what HTML is to text.

- HTML: `<svg>` parent element with children elements such as `<rect>`, `<path>`, `<circle>`, `<text>`

- JavaScript and CSS: used to manipulate contents, attributes, and styling of SVG-related HTML elements

[Option 2: Canvas `<canvas>`](https://developer.mozilla.org/en-US/docs/HTML/Canvas)

> ...the HTML `<canvas>` element can be used to draw graphics via scripting in JavaScript. For example, it can be used to draw graphs, make photo compositions, create animations, or even do real-time video processing or rendering.

- HTML: `<canvas>` element only

- JavaScript: used to send drawing and styling commands to the `<canvas>` element; think of drawing a picture with code.

### Exercise 1: manually make an SVG chart

- Walkthrough of `svg-demo.html`

- It is all about HTML elements defining the vector graphics to render:

  ```html
  <!-- the data values are encoded in the height properties
    to simulate a bar chart with values from 0 to 100 -->
  <svg viewBox="0 0 100 100">
    <rect x="5" y="0" width="10" height="50"></rect>
    <rect x="25" y="0" width="10" height="15"></rect>
  </svg>
  ```

### Exercise 2: manually make a Canvas chart

- Walkthrough of `canvas-demo.html`

- It is all about JavaScript telling a single `<canvas>` element what image pixel graphics to render:

  ```html
  <canvas id="canvasElement"></canvas>

  <script>
    // get reference to the canvas element
    var canvas = document.querySelector('#canvasElement');

    // get the canvas element's 2-D rendering context
    // (this is where we give it drawing instructions)
    var ctx = canvas.getContext('2d');

    // draw a couple rectangle fills to simulate bars in a bar chart
    ctx.fillRect(25, 0, 50, 250);
    ctx.fillRect(125, 0, 50, 75);
  </script>
  ```

- Learn more about Canvas and get inspired:

  - <https://generativeartistry.com/>

  - <https://flaviocopes.com/canvas/>

  - <https://skilled.co/html-canvas/>

### Time to get help from a JavaScript charting library

[Search online for "JavaScript charting libraries"](https://duckduckgo.com/?q=JavaScript+charting+libraries)

:scream: How do we pick one?! :scream:

A few highlights:

- [D3: Data-Driven Documents](https://d3js.org/) :star2: :star2: :star2:

- [Chart.js](https://www.chartjs.org/)

- [plotly.js](https://plot.ly/javascript/) (_also available for [Python](https://plot.ly/python/)_ :snake:)

- [C3.js](https://c3js.org/)

- Some interesting (but complex) examples of charting with the ArcGIS API for JavaScript: <https://developers.arcgis.com/javascript/latest/sample-code/index.html?search=chart>

### Exercise 3: [Leaflet](https://leafletjs.com/) + [Chart.js](https://www.chartjs.org/)

- Walkthrough of `leaflet-demo.html`

- Make a dynamic chart with feature layer data attributes

- Continue to customize it and make it your own

### Exercise 4: [ArcGIS API for JavaScript](https://js.arcgis.com) + [plotly.js](https://plot.ly/javascript/)

- Walkthrough of `esri-demo.html`

- Make a dynamic chart with feature layer data attributes

- Continue to customize it and make it your own
