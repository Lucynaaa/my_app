pipeline {
    agent any
    stages {
        stage("build") {
            steps {
		    echo 'building the application...'
		    pip install -r requirements.txt
		    pip install -r test_requirements.txt
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
