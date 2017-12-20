#!/usr/bin/env groovy

checkout scm
try {
  stage("Build") {
    sh '''
      source rc_dev && make cleanall all
    '''
  }
  stage("Lint and Test") {
    sh '''
      make lint test
    '''
  }
catch (e) {
  throw e
}
finally {
  sh '''
    make cleanall
  '''
}
