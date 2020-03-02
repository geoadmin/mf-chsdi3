#!/usr/bin/env groovy

node(label: "jenkins-slave") {

  try {
    stage("Checkout") {
      checkout scm
    }
    stage("Build") {
      sh 'eval $(cat rc_dev) && make cleanall all'
    }
    stage("Lint") {
      sh 'make lint'
    }
    stage("Test") {
      parallel (
        'integration': {
          sh '.venv/bin/nosetests tests/integration/'
        },
        'functional': {
          sh  '.venv/bin/nosetests tests/functional/'
        }
      )
    }
  } catch (e) {
    throw e
  }
  finally {
    stage("Clean") {
      sh 'make cleanall'
      sh 'git clean -dx --force'
    }
  }
}
