pipeline {
    agent none
    stages {
        stage("build") {
	    agent { docker 'lucynaaa/my-first-docker:1' }
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
