pipeline {
    agent any 
    environment {
        ARTIFACTORY_CREDS = credentials("Artifactory")
        ARTIFACTORY_STRING = "quickstart.cloudera:8081/artifactory/api/pypi/pypi-local/simple"
        ARTIFACTORY_PACKAGE_DIR = "pythontest"
        
        DIR = "/home/cloudera/"
        
        ARTIFACTS_DIR = "${DIR}/artifacts"
        CREDS_STRING = "${ARTIFACTORY_CREDS_USR}:${ARTIFACTORY_CREDS_PSW}"
    }
    
    stages {
        stage("Deploy") {
            steps {
                script {
                    sh "sh deploy.sh"
                    //make an output directory
//                    sh "mkdir -p ${ARTIFACTS_DIR}"
            
//                    sh '''
//                        pip install -U pythontest -i "http://admin:admin@quickstart.cloudera:8081/artifactory/api/pypi/pypi-local/simple" \
//                        --trusted-host quickstart.cloudera --user
//                    '''
            
//                    sh '''

//                        for module in `cat $(ls -d1 ${SITE_PACKAGES_DIR}/* | grep "${ARTIFACTORY_PACKAGE_DIR}-.*egg.info$")/top_level.txt`; do
//                            echo -n "Preparing $module"
//                            cd $SITE_PACKAGES_DIR && zip -r ${ARTIFACTS_DIR}/${module}.zip "$module" > /dev/null
//                            echo "Done"
//                            echo "Transferring $module to HDFS..."
//                            hdfs dfs -copyFromLocal -f $ARTIFACTS_DIR/${module}.zip /user/cloudera/pythontest > /dev/null
//                        done
//                        rm -rf ${ARTIFACTS_DIR}
//                    '''
                }
            }
        }
    }
}
//pip install -U pythontest -i "http://admin:admin@quickstart.cloudera:8081/artifactory/api/pypi/pypi-local/simple" \
//--trusted-host quickstart.cloudera --user
