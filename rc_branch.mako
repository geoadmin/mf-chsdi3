source rc_${deploy_target}
export APACHE_BASE_PATH=${git_branch}
export API_URL=//mf-chsdi3.${deploy_target}.bgdi.ch/${git_branch}
export GEODATA_STAGING=${branch_staging}
export GEOADMINHOST=mf-geoadmin3.${deploy_target}.bgdi.ch
export HOST=mf-chsdi3.${deploy_target}.bgdi.ch
