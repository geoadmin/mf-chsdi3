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
cd ../db
git checkout prod_vs_int_review

# Now we are inside geoadmin/db and here the script is executable 
# mkdir -p prod_vs_int_review 
cd prod_vs_int_review

# Date and time of executing the script
now=$(date +%Y-%m-%d--%H:%M:%S)
prodJsons="https://api3.geo.admin.ch/rest/services/all/MapServer/layersConfig|allLayersConfig.json
       https://api3.geo.admin.ch/rest/services/ech/MapServer/layersConfig|echLayersConfig.json
       https://api3.geo.admin.ch/rest/services/swissmaponline/MapServer/layersConfig|swissmaponlineLayersConfig.json
       https://api3.geo.admin.ch/rest/services/api/MapServer|apiMapServer.json
       https://api3.geo.admin.ch/rest/services/all/faqlist|faqlist.json"
NUMOFLINES=0

echo "${background}${black}Now we are at the production phase${reset}"
wget https://wmts.geo.admin.ch/1.0.0/WMTSCapabilities.xml -O WMTSCapabilities.xml

for pJson in $prodJsons
do
  # split string to take fisrt and last field
  wget ${pJson%|*} -O ${pJson##*|}
  # each json is one line, so here it is being separated at commas to be comparable
  perl -pi -e 's/,/,\n/g' ${pJson##*|}  
  NUMOFLINES=$[$NUMOFLINES+$(wc -l < ${pJson##*|})]
done

# if the number of lines is greater than 5: the comparison of json files is possible
if [ $NUMOFLINES -gt 5 ]; then
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
git push origin prod_vs_int_review 

intJsons="https://mf-chsdi3.int.bgdi.ch/rest/services/all/MapServer/layersConfig|allLayersConfig.json
      https://mf-chsdi3.int.bgdi.ch/rest/services/ech/MapServer/layersConfig|echLayersConfig.json
      https://mf-chsdi3.int.bgdi.ch/rest/services/swissmaponline/MapServer/layersConfig|swissmaponlineLayersConfig.json
      https://mf-chsdi3.int.bgdi.ch/rest/services/api/MapServer|apiMapServer.json
      https://mf-chsdi3.int.bgdi.ch/rest/services/all/faqlist|faqlist.json"
NUMOFLINES=0

echo "${background}${black}Now we are at the integration phase${reset}"
wget https://mf-chsdi3.int.bgdi.ch/1.0.0/WMTSCapabilities.xml -O WMTSCapabilities.xml

for iJson in $intJsons
do
  # split string to take fisrt and last field
  wget ${iJson%|*} -O ${iJson##*|}
  # each json is one line so separate it in lines to make it comparable
  perl -pi -e 's/,/,\n/g' ${iJson##*|}  
  NUMOFLINES=$[$NUMOFLINES+$(wc -l < ${iJson##*|})]
done

# if the number of lines is greater than 5: the comparison of json files is possible
if [ $NUMOFLINES -gt 5 ]; then
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
echo "${background}${black}Push at integration phase!${reset}"
git push origin prod_vs_int_review 

#git show
# Id number of the last commit
var=$(git log -1 --pretty=format:%H)

echo "${background}${black}Check the differences between the two phases at ${red}https://github.com/geoadmin/bod/commit/$var ${reset}"

cd ../mf-chsdi3/ 
git stash apply stash@{0}
