#!/bin/bash

# Each time that this script is executed, this script does the following: 
# - One commit is done for the copy of the files at production phase
# - One commit is done for the copy of the same files at integration phase
# - The output github link shows the differences between production-integration phase for each file

set -e

# Output color of echo
black=`tput setaf 0`
red=`tput setaf 1`
reset=`tput sgr0`
background=`tput setab 7`

# **************************** !!IMPORTANT!! *************************************
# THE FIRST TIME BEFORE EXECUTING THE SCRIPT :
# (re-)initialize Git repository & clone the <prod_vs_int_review> branch of the db project from github
# git init
# git clone -b prod_vs_int_review --single-branch git@github.com:geoadmin/db.git 
# ********************************************************************************

# If permission is denied when executing the bash script, do: chmod u+x <name>
# At the <prod_vs_int_preview> branch all the changes are commited between the different phases (production - integration phases)
# for different dates (a history of changes between the different phases is being kept)

git stash
git init
git clone --no-checkout git@github.com:geoadmin/db.git

cd ../db
git checkout --orphan prod_vs_int
mkdir prod_vs_int_review
cd prod_vs_int_review

# Now we are inside geoadmin/db and here the script is executable 
# mkdir -p prod_vs_int_review 
#cd prod_vs_int_review
#dir=`mktemp -d` && cd $dir

# Date and time of executing the script
now=$(date +%Y-%m-%d--%H:%M:%S)
prodDomain="https://api3.geo.admin.ch"
intDomain="https://mf-chsdi3.int.bgdi.ch"
jsons="/rest/services/all/MapServer/layersConfig|allLayersConfig.json
       /rest/services/ech/MapServer/layersConfig|echLayersConfig.json
       /rest/services/swissmaponline/MapServer/layersConfig|swissmaponlineLayersConfig.json
       /rest/services/api/MapServer|apiMapServer.json
       /rest/services/all/faqlist|faqlist.json
       /rest/services/blw/CatalogServer|blw.json
       /rest/services/are/CatalogServer|are.json
       /rest/services/bafu/CatalogServer|bafu.json
       /rest/services/swisstopo/CatalogServer|swisstopo.json
       /rest/services/kgs/CatalogServer|kgs.json
       /rest/services/funksender/CatalogServer|funksender.json
       /rest/services/nga/CatalogServer|nga.json
       /rest/services/ivs/CatalogServer|ivs.json
       /rest/services/sachplan/CatalogServer|sachplan.json
       /rest/services/geol/CatalogServer|geol.json
       /rest/services/luftbilder/CatalogServer|luftbilder.json
       /rest/services/wildruhezonen/CatalogServer|wildruhezonen.json
       /rest/services/vu/CatalogServer|vu.json
       /rest/services/aviation/CatalogServer|aviation.json
       /rest/services/verteidigung/CatalogServer|verteidigung.json
       /rest/services/gewiss/CatalogServer|gewiss.json
       /rest/services/geothermie/CatalogServer|geothermie.json
       /rest/services/schneesport/CatalogServer|schneesport.json
       /rest/services/energie/CatalogServer|energie.json
       /rest/services/cadastre/CatalogServer|cadastre.json
       /rest/services/inspire/CatalogServer|inspire.json
       /rest/services/ech/CatalogServer|ech.json"
NUMOFLINES=0


echo "${background}${black}Now we are at the production phase${reset}"
wget https://wmts.geo.admin.ch/1.0.0/WMTSCapabilities.xml -O WMTSCapabilities.xml

for json in $jsons
do
  # split string to take fisrt and last field
  wget $prodDomain${json%|*} -O ${json##*|}
  #echo $prodDomain${json%|*}
  #echo ${json##*|}
  # each json is one line, so here it is being separated at commas to be comparable
  perl -pi -e 's/,/,\n/g' ${json##*|}  
  NUMOFLINES=$[$NUMOFLINES+$(wc -l < ${json##*|})]
done

# if the number of lines is greater than 5: the comparison of json files is possible
if [ $NUMOFLINES -gt 27 ]; then
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


echo "${background}${black}Now we are at the integration phase${reset}"
wget https://mf-chsdi3.int.bgdi.ch/1.0.0/WMTSCapabilities.xml -O WMTSCapabilities.xml

for json in $jsons
do
  # split string to take fisrt and last field
  wget $intDomain${json%|*} -O ${json##*|}
  # each json is one line so separate it in lines to make it comparable
  perl -pi -e 's/,/,\n/g' ${json##*|}  
  NUMOFLINES=$[$NUMOFLINES+$(wc -l < ${json##*|})]
done

# if the number of lines is greater than 5: the comparison of json files is possible
if [ $NUMOFLINES -gt 27 ]; then
  echo "${background}${black}The copy of files at the integration phase was successfully done!${reset}"
else
  echo "${background}${black}The proper copy at the integration phase of the files failed. Please repeat the process!${reset}"
  exit
fi
echo "${background}${black}Current Git-status${reset}"
git status
echo "${background}${black}Git-adding the files${reset}"
git add .
echo "${background}${black}Current Git-status${reset}"
git status
echo "${background}${black}Git-commit at integration phase${reset}"
git commit -m "Integration $now"
echo "${background}${black}Current Git-status${reset}"
git status
echo "${background}${black}The differences are:${reset}"

git show
# Id number of the last commit
#var=$(git log -1 --pretty=format:%H)

#echo "${background}${black}Check the differences between the two phases at ${red}https://github.com/geoadmin/bod/commit/$var ${reset}"

cd ../mf-chsdi3/ 
git stash apply stash@{0}
