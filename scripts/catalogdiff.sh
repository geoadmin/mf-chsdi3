#!/bin/bash

# Each time that this script is executed, this script does the following: 
# - One commit is done for the catalog at prod phase
# - One commit is done for the catalog at dev phase
# - The output github link shows the differences between the phases for each file

# NOW THE SCRIPT GIVES THE DIFFERENCES BETWEEN THE OLD AND CATALOG SERVICE
# Later it could be adjusted to return differences of catalog between two phases

set -e

# Output color of echo
black=`tput setaf 0`
red=`tput setaf 1`
reset=`tput sgr0`
background=`tput setab 7`

# **************************** !!IMPORTANT!! *************************************
# THE FIRST TIME BEFORE EXECUTING THE SCRIPT :
# (re-)initialize Git repository & clone the <catalog_review> branch of the db project from github
# git init
# git clone -b catalog_review --single-branch git@github.com:geoadmin/db.git 
# ********************************************************************************

# If permission is denied when executing the bash script, do: chmod u+x <name>
# At the <catalog_review> branch all the changes are commited between the different phases (production - dev phases)
# for different dates (a history of changes between the different phases is being kept)
git stash
cd ../db
git checkout catalog_review

# Now we are inside geoadmin/db and here the script is executable 
# mkdir -p catalog_review 
cd catalog_review

# Date and time of executing the script
now=$(date +%Y-%m-%d--%H:%M:%S)
prodJsons="https://api3.geo.admin.ch/rest/services/blw/CatalogServer|blw.json
       https://api3.geo.admin.ch/rest/services/are/CatalogServer|are.json
       https://api3.geo.admin.ch/rest/services/bafu/CatalogServer|bafu.json
       https://api3.geo.admin.ch/rest/services/swisstopo/CatalogServer|swisstopo.json
       https://api3.geo.admin.ch/rest/services/kgs/CatalogServer|kgs.json
       https://api3.geo.admin.ch/rest/services/funksender/CatalogServer|funksender.json
       https://api3.geo.admin.ch/rest/services/nga/CatalogServer|nga.json
       https://api3.geo.admin.ch/rest/services/ivs/CatalogServer|ivs.json
       https://api3.geo.admin.ch/rest/services/sachplan/CatalogServer|sachplan.json
       https://api3.geo.admin.ch/rest/services/geol/CatalogServer|geol.json
       https://api3.geo.admin.ch/rest/services/luftbilder/CatalogServer|luftbilder.json
       https://api3.geo.admin.ch/rest/services/wildruhezonen/CatalogServer|wildruhezonen.json
       https://api3.geo.admin.ch/rest/services/vu/CatalogServer|vu.json
       https://api3.geo.admin.ch/rest/services/aviation/CatalogServer|aviation.json
       https://api3.geo.admin.ch/rest/services/verteidigung/CatalogServer|verteidigung.json
       https://api3.geo.admin.ch/rest/services/gewiss/CatalogServer|gewiss.json
       https://api3.geo.admin.ch/rest/services/geothermie/CatalogServer|geothermie.json
       https://api3.geo.admin.ch/rest/services/schneesport/CatalogServer|schneesport.json
       https://api3.geo.admin.ch/rest/services/energie/CatalogServer|energie.json
       https://api3.geo.admin.ch/rest/services/cadastre/CatalogServer|cadastre.json
       https://api3.geo.admin.ch/rest/services/inspire/CatalogServer|inspire.json
       https://api3.geo.admin.ch/rest/services/ech/CatalogServer|ech.json"
NUMOFLINES=0

echo "${background}${black}Now we are at the production phase${reset}"

for pJson in $prodJsons
do
  # split string to take fisrt and last field
  wget ${pJson%|*} -O ${pJson##*|}
  # each json is one line, so here it is being separated at commas to be comparable
  perl -pi -e 's/,/,\n/g' ${pJson##*|}  
  NUMOFLINES=$[$NUMOFLINES+$(wc -l < ${pJson##*|})]
done

# if the number of lines is greater than 22: the comparison of json files is possible
if [ $NUMOFLINES -gt 22 ]; then
  echo "${background}${black}The copy of files at the production phase was successfully done!${reset}"
else
  echo "${background}${black}The proper copy of the files at the production phase failed. Please repeat the process!${reset}" 
  exit
fi
echo "${background}${black}Current Git-status${reset}"
git status
echo "${background}${black}Git-adding the files${reset}"
git add .
echo "${background}${black}Current Git-status${reset}"
git status
echo "${background}${black}Git-commit at production phase${reset}"
git commit -m "Production $now"
echo "${background}${black}Current Git-status${reset}"
git status
echo "${background}${black}Push at production phase!${reset}"
git push origin catalog_review 

devJsons="https://mf-chsdi3.dev.bgdi.ch/kom_catalog/rest/services/blw/CatalogServer|blw.json
      https://mf-chsdi3.dev.bgdi.ch/kom_catalog/rest/services/are/CatalogServer|are.json
      https://mf-chsdi3.dev.bgdi.ch/kom_catalog/rest/services/bafu/CatalogServer|bafu.json
      https://mf-chsdi3.dev.bgdi.ch/kom_catalog/rest/services/swisstopo/CatalogServer|swisstopo.json
      https://mf-chsdi3.dev.bgdi.ch/kom_catalog/rest/services/kgs/CatalogServer|kgs.json
      https://mf-chsdi3.dev.bgdi.ch/kom_catalog/rest/services/funksender/CatalogServer|funksender.json
      https://mf-chsdi3.dev.bgdi.ch/kom_catalog/rest/services/nga/CatalogServer|nga.json
      https://mf-chsdi3.dev.bgdi.ch/kom_catalog/rest/services/ivs/CatalogServer|ivs.json
      https://mf-chsdi3.dev.bgdi.ch/kom_catalog/rest/services/sachplan/CatalogServer|sachplan.json
      https://mf-chsdi3.dev.bgdi.ch/kom_catalog/rest/services/geol/CatalogServer|geol.json
      https://mf-chsdi3.dev.bgdi.ch/kom_catalog/rest/services/luftbilder/CatalogServer|luftbilder.json
      https://mf-chsdi3.dev.bgdi.ch/kom_catalog/rest/services/wildruhezonen/CatalogServer|wildruhezonen.json
      https://mf-chsdi3.dev.bgdi.ch/kom_catalog/rest/services/vu/CatalogServer|vu.json
      https://mf-chsdi3.dev.bgdi.ch/kom_catalog/rest/services/aviation/CatalogServer|aviation.json
      https://mf-chsdi3.dev.bgdi.ch/kom_catalog/rest/services/verteidigung/CatalogServer|verteidigung.json
      https://mf-chsdi3.dev.bgdi.ch/kom_catalog/rest/services/gewiss/CatalogServer|gewiss.json
      https://mf-chsdi3.dev.bgdi.ch/kom_catalog/rest/services/geothermie/CatalogServer|geothermie.json
      https://mf-chsdi3.dev.bgdi.ch/kom_catalog/rest/services/schneesport/CatalogServer|schneesport.json
      https://mf-chsdi3.dev.bgdi.ch/kom_catalog/rest/services/energie/CatalogServer|energie.json
      https://mf-chsdi3.dev.bgdi.ch/kom_catalog/rest/services/cadastre/CatalogServer|cadastre.json
      https://mf-chsdi3.dev.bgdi.ch/kom_catalog/rest/services/inspire/CatalogServer|inspire.json
      https://mf-chsdi3.dev.bgdi.ch/kom_catalog/rest/services/ech/CatalogServer|ech.json"
NUMOFLINES=0

echo "${background}${black}Now we are at the dev phase${reset}"

for iJson in $devJsons
do
  # split string to take fisrt and last field
  wget ${iJson%|*} -O ${iJson##*|}
  # each json is one line so separate it in lines to make it comparable
  perl -pi -e 's/,/,\n/g' ${iJson##*|}  
  NUMOFLINES=$[$NUMOFLINES+$(wc -l < ${iJson##*|})]
done

# if the number of lines is greater than 22: the comparison of json files is possible
if [ $NUMOFLINES -gt 22 ]; then
  echo "${background}${black}The copy of files at the dev phase was successfully done!${reset}"
else
  echo "${background}${black}The proper copy at the dev phase of the files failed. Please repeat the process!${reset}"
  exit
fi
echo "${background}${black}Current Git-status${reset}"
git status
echo "${background}${black}Git-adding the files${reset}"
git add .
echo "${background}${black}Current Git-status${reset}"
git status
echo "${background}${black}Git-commit at dev phase${reset}"
git commit -m "DEV $now"
echo "${background}${black}Current Git-status${reset}"
git status
echo "${background}${black}Push at dev phase!${reset}"
git push origin catalog_review

#git show
# Id number of the last commit
var=$(git log -1 --pretty=format:%H)

echo "${background}${black}Check the differences between the two phases at ${red}https://github.com/geoadmin/bod/commit/$var ${reset}"

cd ../mf-chsdi3/ 
git stash apply stash@{0}
