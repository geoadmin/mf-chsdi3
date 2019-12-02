"use strict";
// Doc https://github.com/Automattic/node-canvas/tree/v1.6.9
// node: v8.10.0
// libcairo2-dev: 1.14.6-1
// sudo apt-get install libcairo2-dev libjpeg-dev libpango1.0-dev libgif-dev build-essential g++

const fs = require('fs');
const request = require('request');
const JSONStream = require('JSONStream');
const { createCanvas, loadImage } = require('canvas');
const csv = require('fast-csv');
const async = require('async');
const scaleFactor = 1.5;

let styleFile,
    layerID;
if (process.argv.length == 3) {
  layerID = process.argv[2];
  styleFile = 'chsdi/static/vectorStyles/' + layerID + '.json';
}
console.log('Preparing ' + layerID);

let readStream = fs.createReadStream(styleFile, {encoding: 'utf8'});
let readJSONStream = JSONStream.parse();

let getStyleType = function(data) {
  let styleType;
  for (let value in data) {
    if (['ranges', 'values'].indexOf(value) != -1) {
      styleType = value;
    }
  }
  return styleType;
};

let getStylesByResolution = function(data, styleType) {
  let styles = {};
  for (let i=0; i < data[styleType].length; i++) {
    let resolutionHash = 'res';
    let style = data[styleType][i];
    if (String(style.vectorOptions.src).indexOf('nodata') == -1) {
      if (style.minResolution) {
        resolutionHash += '-min-' + style.minResolution.toString();
      }
      if (style.maxResolution) {
        resolutionHash += '-max-' + style.maxResolution.toString();
      }
      if (!styles.hasOwnProperty(resolutionHash)) {
        styles[resolutionHash] = [];
      }
      styles[resolutionHash].push(style);
    }
  }
  return styles;
};

let getXY = function(i) {
  // margin left
  let x = 30;
  let paddingTop = 20;
  let marginTop = 30;
  let y = paddingTop + marginTop * i;
  return { x: x, y: y };
};

let createImage = function(symbol, i) {
  let createImageCallback = function(context, cb) {
    //console.log(symbol.src);
    let requestSettings = {
      url: symbol.src,
      method: 'GET',
      encoding: null
    };
    // BIT in the middle: ignore fake CERTS
    // https://stackoverflow.com/questions/10888610/ignore-invalid-self-signed-ssl-certificate-in-node-js-with-https-request
    process.env["NODE_TLS_REJECT_UNAUTHORIZED"] = 0;
    loadImage(symbol.src).then((image) => {
      if (!image) {
        console.error("Error while loading image", symbol.src);
      } else {
        let c = getXY(i);
        context.drawImage(image, c.x, c.y, image.width, image.height);
        cb(null, context);
      }
    });
  };
  return createImageCallback;
};

let createTriangle = function(context, symbol, i) {
  let c = getXY(i);
  let radius = symbol.radius * scaleFactor;

  context.beginPath();
  context.moveTo(c.x - radius, c.y + radius);
  context.lineTo(c.x + radius, c.y + radius);
  context.lineTo(c.x, c.y - radius);
  context.lineTo(c.x - radius, c.y + radius);
  context.closePath();
  context.lineWidth = symbol.stroke.width * scaleFactor;
  context.strokeStyle = symbol.stroke.color;
  context.stroke();
  context.fillStyle = symbol.fill.color;
  context.fill();
  return context;
};

let createSquare = function(context, symbol, i) {
  let c = getXY(i);
  let radius = symbol.radius * scaleFactor;

  context.beginPath();
  context.moveTo(c.x - radius, c.y + radius);
  context.lineTo(c.x + radius, c.y + radius);
  context.lineTo(c.x + radius, c.y - radius);
  context.lineTo(c.x - radius, c.y - radius);
  context.closePath();
  context.lineWidth = symbol.stroke.width * scaleFactor;
  context.strokeStyle = symbol.stroke.color;
  context.stroke();
  context.fillStyle = symbol.fill.color;
  context.fill();
  return context;
};

let createPentagon = function(context, symbol, i) {
  let c = getXY(i);
  let radius = symbol.radius * scaleFactor;
  let sides = 5;
  let angle = (2 * Math.PI) / sides;

  // save translation and rotation definition before
  context.save();
  context.beginPath();
  context.translate(c.x, c.y);
  context.rotate(-Math.PI / 2);
  context.moveTo(radius, 0);
  for (let j=1; j<sides; j++) {
    let innerAngle = angle * j;
    let cx = radius * Math.cos(innerAngle);
    let cy = radius * Math.sin(innerAngle);
    context.lineTo(cx, cy);
  }
  context.closePath();
  // restore default translation and rotation
  context.restore();

  context.lineWidth = symbol.stroke.width * scaleFactor;
  context.strokeStyle = symbol.stroke.color;
  context.stroke();
  context.fillStyle = symbol.fill.color;
  context.fill();
  return context;
};

let createHexagon = function(context, symbol, i) {
  let c = getXY(i);
  let radius = symbol.radius * scaleFactor;
  let sides = 6;
  let angle = (2 * Math.PI) / sides;

  // save translation and rotation definition before
  context.save();
  context.beginPath();
  context.translate(c.x, c.y);
  context.rotate(-Math.PI / 2);
  context.moveTo(radius, 0);
  for (let j=1; j<sides; j++) {
    let innerAngle = angle * j;
    let cx = radius * Math.cos(innerAngle);
    let cy = radius * Math.sin(innerAngle);
    context.lineTo(cx, cy);
  }
  context.closePath();
  // restore default translation and rotation
  context.restore();

  context.lineWidth = symbol.stroke.width * scaleFactor;
  context.strokeStyle = symbol.stroke.color;
  context.stroke();
  context.fillStyle = symbol.fill.color;
  context.fill();
  return context;
};

let createStar = function(context, symbol, i) {
  let c = getXY(i);
  let radius = symbol.radius * scaleFactor;
  let radius2 = radius / 2;
  let spikes = 5;
  let rot = Math.PI / 2 * 3;
  let step = Math.PI/spikes;

  context.beginPath();
  context.moveTo(c.x, c.y - radius);

  for (let j=0; j<spikes; j++) {
    let cx, cy;
    cx = c.x + radius * Math.cos(rot);
    cy = c.y + radius * Math.sin(rot);
    context.lineTo(cx, cy);
    rot += step;

    cx = c.x + radius2 * Math.cos(rot);
    cy = c.y + radius2 * Math.sin(rot);
    context.lineTo(cx, cy);
    rot += step;
  }
  context.lineTo(c.x, c.y - radius);
  context.closePath();

  context.lineWidth = symbol.stroke.width * scaleFactor;
  context.strokeStyle = symbol.stroke.color;
  context.stroke();
  context.fillStyle = symbol.fill.color;
  context.fill();
  return context;
};

let createCross = function(context, symbol, i) {
  let c = getXY(i);
  let radius = symbol.radius * scaleFactor;
  context.beginPath();
  // First line
  context.moveTo(c.x, c.y - radius);
  context.lineTo(c.x, c.y + radius);
  // Second line
  context.moveTo(c.x - radius, c.y);
  context.lineTo(c.x + radius, c.y);
  context.lineWidth = symbol.stroke.width * scaleFactor;
  context.strokeStyle = symbol.stroke.color;
  context.stroke();
  return context;
};

//  { type: 'circle',
//    radius: 6,
//    fill: { color: 'rgba(106,44,90,0.9)' },
//    stroke: { color: 'black', width: 1 } } ]
let createCircle = function(context, symbol, i) {
  let c = getXY(i);
  let radius = symbol.radius * scaleFactor;

  // Then create the inner shape
  context.beginPath();
  context.arc(c.x,
              c.y,
              radius, 0,  2 * Math.PI, true);
  context.closePath();
  context.lineWidth = symbol.stroke.width * scaleFactor;
  context.strokeStyle = symbol.stroke.color;
  context.stroke();
  context.fillStyle = symbol.fill.color;
  context.fill();
  return context;
};

let createLabel = function(context, symbol, i, txt) {
  let c = getXY(i);
  // for drawn shapes : for icons TODO get image height and width
  let radius = symbol.radius ? symbol.radius * scaleFactor : 16 * scaleFactor;
  let marginLeft = c.x + radius + 15;
  let marginTop = symbol.radius ? c.y + 2.5 : c.y + 13.5;

  context.beginPath();
  context.font = 'bold 12px verdana, sans-serif';
  context.fillStyle = 'black';
  context.fillText(txt, marginLeft, marginTop);
  context.closePath();
  return context;
};

let createLegendRamp = function(data, labels, lang, cb) {
  let styleType = getStyleType(data);
  let styles = getStylesByResolution(data, styleType);
  let keys = Object.keys(styles);
  // availale res
  //let legendKey = keys.indexOf('res-max-50') !== -1 ? 'res-max-50' : keys[0];
  let legendKey = keys.indexOf('res-max-100') !== -1 ? 'res-max-100' : keys[0];

  // store all icon requests parameters
  let iconsReqParams = [];
  // Take the resolution
  let spec = styles[legendKey];
  // TODO compute height and width dynamically
  let canvas = createCanvas(480, 20 + spec.length * 30);
  let context = canvas.getContext('2d');
  for (let i=0; i < spec.length; i++) {
    let symbol = spec[i].vectorOptions;
    if (symbol.type === 'circle') {
      let range = spec[i].range;
      context = createCircle(context, symbol, i);
    } else if (symbol.type == 'triangle') {
      context = createTriangle(context, symbol, i);
    } else if (symbol.type == 'square') {
      context = createSquare(context, symbol, i);
    } else if (symbol.type == 'cross') {
      context = createCross(context, symbol, i);
    } else if (symbol.type == 'pentagon') {
      context = createPentagon(context, symbol, i);
    } else if (symbol.type == 'hexagon') {
      context = createHexagon(context, symbol, i);
    } else if (symbol.type == 'star') {
      context = createStar(context, symbol, i);
    } else if (symbol.type == 'icon') {
      iconsReqParams.push(createImage(symbol, i));
    }
    if (labels.length && labels[i]) {
      context = createLabel(context, symbol, i, labels[i][lang]);
    }
  }
  if (iconsReqParams.length) {
    loadImage(canvas.toBuffer()).then(img => {
      let composer = async.compose.apply(null, iconsReqParams);
      composer(context, function (err, result) {
        if (err) {
          console.log('Error in compose');
        } else {
          cb(canvas);
        }
      });
    });
  } else {
    cb(canvas);
  }
};

let labels = [];

async.series([
  function readCsv(step) {
    csv
      .fromPath('scripts/legend_labels.csv', {headers : true})
      .on('data', function(data) {
        if (layerID.indexOf(data.TECHNICAL_NAME_TX) !== -1) {
          labels.push(data);
        }
      })
      .on('end', function() {
        console.log('done');
        step();
      })
  },
  function createPNGs(step) {
    readJSONStream.on('data', function(data) {
      createLegendRamp(data, labels, 'LABEL_G', function(canvas) {
        canvas.pngStream().pipe(fs.createWriteStream('chsdi/static/images/legends/' + layerID + '_de.png'));
      });
      createLegendRamp(data, labels, 'LABEL_F', function(canvas) {
        canvas.pngStream().pipe(fs.createWriteStream('chsdi/static/images/legends/' + layerID + '_fr.png'));
      });
      createLegendRamp(data, labels, 'LABEL_I', function(canvas) {
        canvas.pngStream().pipe(fs.createWriteStream('chsdi/static/images/legends/' + layerID + '_it.png'));
      });
      createLegendRamp(data, labels, 'LABEL_E', function(canvas) {
        canvas.pngStream().pipe(fs.createWriteStream('chsdi/static/images/legends/' + layerID + '_en.png'));
      });
      createLegendRamp(data, labels, 'LABEL_G', function(canvas) {
        canvas.pngStream().pipe(fs.createWriteStream('chsdi/static/images/legends/' + layerID + '_rm.png'));
      });
      step();
    });
    readStream.pipe(readJSONStream);
  }
]);
