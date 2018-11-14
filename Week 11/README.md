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

### Choose your own adventure

[Option 1: SVG `<svg>`](https://developer.mozilla.org/en-US/docs/Web/SVG)

> Scalable Vector Graphics (SVG) is an XML-based markup language for describing two dimensional based  vector graphics. SVG is essentially to graphics what HTML is to text.

- HTML: `<svg>` parent element with children elements such as `<rect>`, `<path>`, `<circle>`, `<text>`

- JavaScript and CSS: used to manipulate contents, attributes, and styling of SVG-related HTML elements

[Option 2: Canvas `<canvas>`](https://developer.mozilla.org/en-US/docs/HTML/Canvas)

> ...the HTML `<canvas>` element can be used to draw graphics via scripting in JavaScript. For example, it can be used to draw graphs, make photo compositions, create animations, or even do real-time video processing or rendering.

- HTML: `<canvas>` element only

- JavaScript: used to send drawing and styling commands to the `<canvas>` element; think of drawing a picture with code

### Exercise 1: manually make an SVG chart

<details>
  <summary>Expand for details...</summary>

  ```html
  <!DOCTYPE html>
  <html>

  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>SVG Demo</title>

    <style>
      body {
        font-family: sans-serif;
      }

      svg {
        max-width: 500px;
        max-height: 500px;
        outline: 2px solid steelblue;

        /* experiment with other CSS properties */
        /* stroke-linejoin: round; */
        /* stroke-linecap: round; */
      }

      rect {
        fill: lightgray;
        stroke: deeppink;
        stroke-width: 2px;
        vector-effect: non-scaling-stroke;
      }
    </style>
  </head>

  <body>
    <p>SVG Demo</p>

    <svg viewBox="0 0 100 100">
      <!-- the data values are encoded in these properties -->
      <rect x="5" y="0" width="10" height="50"></rect>
      <rect x="25" y="0" width="10" height="15"></rect>
      <rect x="45" y="0" width="10" height="75"></rect>
      <rect x="65" y="0" width="10" height="66.666"></rect>
      <rect x="85" y="0" width="10" height="33.333"></rect>
    </svg>
  </body>

  </html>
  ```

</details>

### Exercise 2: manually make a Canvas chart

<details>
  <summary>Expand for details...</summary>

  ```html
  <!DOCTYPE html>
  <html>

  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>Canvas Demo</title>

    <style>
      body {
        font-family: sans-serif;
      }

      #canvasElement {
        outline: 2px solid steelblue;
      }
    </style>
  </head>

  <body>
    <p>Canvas Demo</p>

    <canvas id="canvasElement" width="500" height="500"></canvas>

    <script>
      // get reference to the canvas element
      var canvas = document.querySelector('#canvasElement');

      // get the canvas element's 2-D rendering context
      // (this is where we give it drawing instructions)
      var ctx = canvas.getContext('2d');

      // set styles for the next set of drawing commands below
      ctx.fillStyle = 'lightgray';
      ctx.strokeStyle = 'deeppink'
      ctx.lineWidth = 2;

      // experiment with some other style properties
      // ctx.lineJoin = 'round';
      // ctx.lineCap = 'round';

      // NOTE: this will create a graphic nearly identical to the SVG demo;
      // all these numbers came from the SVG demo but were multiplied by 5 because the
      // <canvas> handles width/height differently and is actually 5x bigger than the SVG

      // draw rectangle fills
      ctx.fillRect(25, 0, 50, 250);
      ctx.fillRect(125, 0, 50, 75);
      ctx.fillRect(225, 0, 50, 375);
      ctx.fillRect(325, 0, 50, 333.333);
      ctx.fillRect(425, 0, 50, 166.666);

      // draw rectangle outlines
      ctx.strokeRect(25, 0, 50, 250);
      ctx.strokeRect(125, 0, 50, 75);
      ctx.strokeRect(225, 0, 50, 375);
      ctx.strokeRect(325, 0, 50, 333.333);
      ctx.strokeRect(425, 0, 50, 166.666);
    </script>
  </body>

  </html>
  ```

</details>

### Time to get help from a JavaScript charting library

[Search online for "JavaScript charting libraries"](https://duckduckgo.com/?q=JavaScript+charting+libraries)

:scream: How do we pick one?! :scream:

A few highlights:

- [D3: Data-Driven Documents](https://d3js.org/) :star2: :star2: :star2:

- [Chart.js](https://www.chartjs.org/)

- [C3.js](https://c3js.org/)

- [CHARTIST.JS](http://gionkunz.github.io/chartist-js/index.html)

- [plotly.js](https://plot.ly/javascript/) (also available for [Python](https://plot.ly/python/) :snake:)

- Some interesting (but complex) examples of charting with the ArcGIS API for JavaScript: <https://developers.arcgis.com/javascript/latest/sample-code/index.html?search=chart>

### Exercise 3: Leaflet + Chart.js

- Walkthrough of `leaflet-demo.html`

- Make a dynamic chart with feature layer data attributes

- Continue to customize it and make it your own

### Exercise 4: ArcGIS API for JavaScript + plotly.js

- Walkthrough of `esri-demo.html`

- Make a dynamic chart with feature layer data attributes

- Continue to customize it and make it your own
