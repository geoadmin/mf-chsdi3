source rc_${deploy_target}
export APACHE_BASE_PATH=${GIT_BRANCH}
export API_URL=//mf-chsdi3.${DEPLOY_TARGET}.BGDI.CH/${GIT_BRANCH}
export GEODATA_STAGING=test
export GEOADMINHOST=mf-geoadmin3.${DEPLOY_TARGET}.BGDI.CH
export HOST=mf-chsdi3.${DEPLOY_TARGET}.bgdi.ch
export DBSTAGING=dev
