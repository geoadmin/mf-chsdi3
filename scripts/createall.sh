#!/bin/bash

# https://docs.google.com/spreadsheets/d/1dmVyS3VRkF2n8-D_cJafgERSWZecnqUPOByQD1mTx7U/edit#gid=1198942164
# export as csv-comma-separated -> ./legend_labels.csv

METEO_LAYERS=(ch.meteoschweiz.messwerte-windgeschwindigkeit-kmh-10min ch.meteoschweiz.messwerte-wind-boeenspitze-kmh-10min ch.meteoschweiz.messwerte-taupunkt-10min ch.meteoschweiz.messwerte-sonnenscheindauer-relativ-1d ch.meteoschweiz.messwerte-sonnenscheindauer-10min ch.meteoschweiz.messwerte-niederschlag-1h ch.meteoschweiz.messwerte-niederschlag-1d ch.meteoschweiz.messwerte-niederschlag-10min ch.meteoschweiz.messwerte-neuschnee-1d ch.meteoschweiz.messwerte-lufttemperatur-24h-min-1h ch.meteoschweiz.messwerte-lufttemperatur-24h-max-1h ch.meteoschweiz.messwerte-lufttemperatur-10min ch.meteoschweiz.messwerte-luftfeuchtigkeit-10min ch.meteoschweiz.messwerte-luftdruck-qnh-10min ch.meteoschweiz.messwerte-luftdruck-qff-10min ch.meteoschweiz.messwerte-luftdruck-qfe-10min ch.meteoschweiz.messwerte-luftdruck-850hpa-flaeche-10min ch.meteoschweiz.messwerte-luftdruck-700hpa-flaeche-10min ch.meteoschweiz.messwerte-globalstrahlung-1d ch.meteoschweiz.messwerte-globalstrahlung-10min ch.meteoschweiz.messwerte-gesamtschnee-1d ch.meteoschweiz.messwerte-foehn-10min ch.meteoschweiz.messnetz-webcams ch.meteoschweiz.messnetz-pollen ch.meteoschweiz.messnetz-phaenologie ch.meteoschweiz.messnetz-partner ch.meteoschweiz.messnetz-manuell ch.meteoschweiz.messnetz-klima ch.meteoschweiz.messnetz-flugwetter ch.meteoschweiz.messnetz-beobachtungen ch.meteoschweiz.messnetz-automatisch ch.meteoschweiz.messnetz-atmosphaere  ch.meteoschweiz.messwerte-luftdruck-differenz-3h ch.meteoschweiz.messwerte-neuschnee-2d ch.meteoschweiz.messwerte-neuschnee-3d ch.meteoschweiz.messwerte-niederschlag-24h ch.meteoschweiz.messwerte-niederschlag-48h ch.meteoschweiz.messwerte-niederschlag-72h)

function download_and_lint_and_legend {
  wget https://data.geo.admin.ch/$1/testing/$1.json -O chsdi/static/vectorStyles/${1}_temp.json
  #wget https://data.geo.admin.ch/$1/$1.json -O chsdi/static/vectorStyles/${1}_temp.json
  node_modules/.bin/jsonlint chsdi/static/vectorStyles/${1}_temp.json > chsdi/static/vectorStyles/$1.json
  rm -f chsdi/static/vectorStyles/${1}_temp.json
  node scripts/createlegends.js ${1}
}

i=0
for layer in ${METEO_LAYERS[*]}; do
  if [[ ${layer} =~ "messnetz" ]]; then
    echo "ignoring ${layer}"
  else
    download_and_lint_and_legend $layer
  fi
  i=$(( $i + 1 ))
done
echo $i layer styles have been downloaded
node --version
