#!/bin/bash

WMSHOST=$1
BODID=$2
WMSCALELEGEND=
if [ -n "$3" ]; then
  WMSCALELEGEND=$3
fi
LEGENDS_FOLDER=chsdi/static/images/legends/
echo "WMSHOST: $WMSHOST"
echo "BODID: $BODID"
echo "WMSSCALELEGEND: $WMSCALELEGEND"
WMS_URL_GETCAP="https://$WMSHOST?SERVICE=WMS&VERSION=1.3.0&REQUEST=GetCapabilities"
COUNT_OCCURENCE=$(curl -s $WMS_URL_GETCAP | grep -c $BODID)

if [ "$COUNT_OCCURENCE" -eq "0" ]; then
  echo "$BODID does not exist."
  exit 1
fi

WMS_URL="https://$WMSHOST?SERVICE=WMS&VERSION=1.3.0&REQUEST=GetLegendGraphic&FORMAT=image/png&TRANSPARENT=true&LAYER=$BODID&SLD_VERSION=1.1.0"
if [ -n "$WMSCALELEGEND" ]; then
  WMS_URL="${WMS_URL}&SCALE=$WMSCALELEGEND"
fi
WMS_URL="${WMS_URL}&LANG="
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
