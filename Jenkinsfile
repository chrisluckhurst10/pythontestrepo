pipeline {
    
//    environment {
//        WORKFLOW_SCRIPTS = "/home/cloudera/JenkinsScripts"
//        ARTIFACTORY = credentials("Artifactory")
//    }

        

//    options {
//        timestamps()
//    }

    agent any

    stages {
        stage("Quality Assurance") {
            steps {
                script {
 //                   commonLib = load("${WORKFLOW_SCRIPTS}//common.groovy")
                    sh 'wget  https://raw.githubusercontent.com/chrisluckhurst10/pythontestrepo/master/pythontest/dist/pythontest-0.0.0.zip'
                }
            }
        }
    }
}
                    

