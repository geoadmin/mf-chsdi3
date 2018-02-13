#!/usr/bin/env groovy

node(label: "jenkins-slave") {
  try {
    stage("Checkout") {
      sh 'echo Checking out code from github'
      checkout scm
    }
    stage("Build") {
      sh '''
        echo Starting the build...
      '''
    }
    stage("Run") {
      sh '''
        echo Starting the containers...
      '''
    }
    stage("Test") {
      sh '''
        echo Starting the tests...
      '''
    }
  catch (e) {
    throw e
  }
  finally {
    sh 'echo All dockers have been purged'
  }
}
