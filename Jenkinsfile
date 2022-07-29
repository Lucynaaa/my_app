pipeline {
    agent none
    stages {
	stage("set up") {
		    sh 'sudo apt-get install podman'
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
