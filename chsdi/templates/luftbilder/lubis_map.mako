<%def name="init_map(ebkey, width, height, rotation, target)">
        var TILE_SIZE = 256;
        var MAX_INSTANCES = 4;
        var curInstance = MAX_INSTANCES;
        var width = parseInt(${width | u});
        var height = parseInt(${height | u});
        var rotation= parseInt(${rotation if rotation != 'None' and rotation is not None else 0 | u}) * Math.PI / 180;

        var url = '//aerialimages{curInstance}.geo.admin.ch/tiles/${ebkey}/';
        var resolutions = [1]; // 1 is the min resolution of the pyramid (for all images)
        var curResolution = resolutions[0];
        var maxResolution = Math.max(width, height) / TILE_SIZE;

        var Xn = 0.950470;
        var Yn = 1;
        var Zn = 1.088830;
        var t0 = 4 / 29;
        var t1 = 6 / 29;
        var t2 = 3 * t1 * t1;
        var t3 = t1 * t1 * t1;
        var twoPi = 2 * Math.PI;


        /**
         * Convert an RGB pixel into an HCL pixel.
         * @param {Array.<number>} pixel A pixel in RGB space.
         * @return {Array.<number>} A pixel in HCL space.
        */
        function rgb2hcl(pixel) {
          var red = rgb2xyz(pixel[0]);
          var green = rgb2xyz(pixel[1]);
          var blue = rgb2xyz(pixel[2]);

          var x = xyz2lab(
            (0.4124564 * red + 0.3575761 * green + 0.1804375 * blue) / Xn);
          var y = xyz2lab(
            (0.2126729 * red + 0.7151522 * green + 0.0721750 * blue) / Yn);
          var z = xyz2lab(
            (0.0193339 * red + 0.1191920 * green + 0.9503041 * blue) / Zn);

          var l = 116 * y - 16;
          var a = 500 * (x - y);
          var b = 200 * (y - z);

          var c = Math.sqrt(a * a + b * b);
          var h = Math.atan2(b, a);
          if (h < 0) {
            h += twoPi;
          }

          pixel[0] = h;
          pixel[1] = c;
          pixel[2] = l;

          return pixel;
        }


        /**
         * Convert an HCL pixel into an RGB pixel.
         * @param {Array.<number>} pixel A pixel in HCL space.
         * @return {Array.<number>} A pixel in RGB space.
        */
        function hcl2rgb(pixel) {
          var h = pixel[0];
          var c = pixel[1];
          var l = pixel[2];

          var a = Math.cos(h) * c;
          var b = Math.sin(h) * c;

          var y = (l + 16) / 116;
          var x = isNaN(a) ? y : y + a / 500;
          var z = isNaN(b) ? y : y - b / 200;

          y = Yn * lab2xyz(y);
          x = Xn * lab2xyz(x);
          z = Zn * lab2xyz(z);

          pixel[0] = xyz2rgb(3.2404542 * x - 1.5371385 * y - 0.4985314 * z);
          pixel[1] = xyz2rgb(-0.9692660 * x + 1.8760108 * y + 0.0415560 * z);
          pixel[2] = xyz2rgb(0.0556434 * x - 0.2040259 * y + 1.0572252 * z);

          return pixel;
        }

        function xyz2lab(t) {
          return t > t3 ? Math.pow(t, 1 / 3) : t / t2 + t0;
        }

        function lab2xyz(t) {
          return t > t1 ? t * t * t : t2 * (t - t0);
        }

        function rgb2xyz(x) {
          return (x /= 255) <= 0.04045 ? x / 12.92 : Math.pow((x + 0.055) / 1.055, 2.4);
        }

        function xyz2rgb(x) {
          return 255 * (x <= 0.0031308 ?
            12.92 * x : 1.055 * Math.pow(x, 1 / 2.4) - 0.055);
        }

        // in case you want to add a slider, add a degree parameter (value range:0-200)
        function getPixelValue(pixel, mean, equalizedValues){
          var hcl = rgb2hcl(pixel);
          var l = parseInt(hcl[2]);
          var equalizedValue = equalizedValues[l];
          var new_l;
          var degree = 150;

          if (degree<100){
            new_l = mean * (1 - (degree / 100)) + l * (degree / 100);
          }else{
            new_l = l * (2 - (degree / 100)) + ((degree / 100)-1) * 100 * equalizedValue;
          }

          hcl[2] = new_l;
          return hcl2rgb(hcl);
        }


        while (curResolution < maxResolution) {
          curResolution *= 2;
          resolutions.unshift(curResolution);
        }

        var tileimage = new ol.source.TileImage({
          crossOrigin: 'anonymous',
          tileGrid: new ol.tilegrid.TileGrid({
            origin: [0, 0],
            resolutions: resolutions
          }),
          tileUrlFunction: function(tileCoord, pixelRatio, projection) {
            var coords = tileCoord;
            if (coords[0] < 0 || coords[1] < 0 || coords[2] < 0) {
              return undefined;
            }
            var factor = this.getTileGrid().getTileSize() * this.getTileGrid().getResolutions()[coords[0]];
            if (coords[1] * factor > width || coords[2] * factor > height) {
              return undefined;
            }
            curInstance = (++curInstance > MAX_INSTANCES) ? 0 : curInstance;
            return url.replace('{curInstance}', curInstance) + tileCoord.join('/') + ".jpg";
          }
        });

        var tile = new ol.layer.Tile({
          preload: 0,
          source: tileimage,
          visible: true
        });

        var raster = new ol.source.Raster({
          sources: [tileimage],
          crossOrigin: 'anonymous',
          operation: function(pixels, data) {
            var pixel = pixels[0];
            if (data.equalizedValues && pixel[3]!=0){
              pixel = getPixelValue(pixel, data.mean, data.equalizedValues);
            }
            return pixel;
          },
          lib:{
            getPixelValue: getPixelValue,
            rgb2hcl: rgb2hcl,
            hcl2rgb: hcl2rgb,
            rgb2xyz: rgb2xyz,
            lab2xyz: lab2xyz,
            xyz2lab: xyz2lab,
            xyz2rgb: xyz2rgb,
            Xn: Xn,
            Yn: Yn,
            Zn: Zn,
            t0: t0,
            t1: t1,
            t2: t2,
            t3: t3,
            twoPi: twoPi
          }
        });

        var contrastLayer = new ol.layer.Image({
          source: raster,
          visible: false
        });

        var lubisMap = new ol.Map({
          layers: [
            tile, contrastLayer
          ],
          controls: ol.control.defaults().extend([new ol.control.FullScreen()]),
          renderer: 'canvas',
          target: ${target},
          logo: false,
          view: new ol.View({
            projection: new ol.proj.Projection({
              code: 'PIXELS',
              units: 'pixels',
              extent: [0, 0, TILE_SIZE * resolutions[0], TILE_SIZE * resolutions[0]] // max extent of the pyramid at zoom level 0
            }),
            maxZoom: resolutions.length + 1 // The min resolution of the pyramid is 1, so we add 2 client zoom equivalent to resolutions 0.5 and 0.25
          })
        });
        lubisMap.getView().fit([0, 0, width, height], lubisMap.getSize());
        lubisMap.getView().setRotation(rotation);
</%def>

