pipeline {
    agent any
    stages {
	stage("set up") {
            steps {
	            sh 'ln -s /usr/bin/podman /usr/bin/docker'
	    }
	}
        stage("build") {
	    agent { 
		    docker { image 'python:2.7' }
	    }
            steps {
		    echo 'building the application...'
		    sh 'pip install -r requirements.txt'
		    sh 'pip install -r test_requirements.txt'
	    }
	}
        stage("test") {
            steps {
	            echo 'testing the application...'
	    }
	}
	stage("deploy") {
	    steps {
		    echo 'deplying the application...'
            }
        }
    }
}
