#!/bin/bash

WMSHOST=$1
BODID=$2
LEGENDS_FOLDER=chsdi/static/images/legends/
echo "WMSHOST: $WMSHOST"
echo "BODID: $BODID"
WMS_URL="https://$WMSHOST?SERVICE=WMS&VERSION=1.3.0&REQUEST=GetLegendGraphic&FORMAT=image/png&TRANSPARENT=true&LAYER=$BODID&SLD_VERSION=1.1.0&LANG="
LANGS=(de fr it en rm)

for lang in ${LANGS[@]}; do
  IMG_LOCATION=${LEGENDS_FOLDER}${BODID}_$lang.png
  wget $WMS_URL$lang -O $IMG_LOCATION
  IMG_WIDTH=$(convert $IMG_LOCATION -print "%w" /dev/null)
  IMG_HEIGHT=$(convert $IMG_LOCATION -print "%h" /dev/null)
  if (( $IMG_WIDTH > 480 )); then
    echo "Image width bigger than 480 px, shrinking the image:"
    convert $IMG_LOCATION -resize 480x$IMG_HEIGHT $IMG_LOCATION
  fi
  echo "Image optimization:"
  optipng -o3 $IMG_LOCATION
done
echo "Please make sure your legend are correctly displayed:"
echo "$API_URL${IMG_LOCATION:5}"
