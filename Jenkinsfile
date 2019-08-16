pipeline {
    agent any
    stages {
        stage('build') {
            steps {
                sh 'python --version'
            }
        }
        stage('Test') {
            steps {
                dir ('lib') {
                    git branch: "master", credentialsId: "2cfb403c-be21-4fac-94d7-c8cd5c531feb", url: "https://gitlab.dicelab.net/JAC-IDM/python-lib.git"
                }
                dir ('elastic_lib') {
                    git branch: "master", credentialsId: "2cfb403c-be21-4fac-94d7-c8cd5c531feb", url: "https://gitlab.dicelab.net/JAC-IDM/elastic-lib.git"
                }
                dir ('elastic_lib/lib') {
                    git branch: "master", credentialsId: "2cfb403c-be21-4fac-94d7-c8cd5c531feb", url: "https://gitlab.dicelab.net/JAC-IDM/python-lib.git"
                }
                dir ('elastic_lib/requests_lib') {
                    git branch: "master", credentialsId: "2cfb403c-be21-4fac-94d7-c8cd5c531feb", url: "https://gitlab.dicelab.net/JAC-IDM/requests-lib.git"
                }
                sh """
                virtualenv test_env
                source test_env/bin/activate
                pip2 install mock --user
                pip2 install elasticsearch --user
                pip2 install requests --user
                ./test/unit/elastic_db_admin/check_status.py
                ./test/unit/elastic_db_admin/failed_dumps.py
                ./test/unit/elastic_db_admin/get_data.py
                ./test/unit/elastic_db_admin/get_status.py
                ./test/unit/elastic_db_admin/help_message.py
                ./test/unit/elastic_db_admin/list_dumps.py
                ./test/unit/elastic_db_admin/list_master.py
                ./test/unit/elastic_db_admin/list_nodes.py
                ./test/unit/elastic_db_admin/list_repos.py
                ./test/unit/elastic_db_admin/process_data.py
                ./test/unit/elastic_db_admin/run_program.py
                ./test/unit/elastic_db_admin/main.py
                deactivate
                rm -rf test_env
                """
            }
        }
        stage('SonarQube analysis') {
            steps {
                sh './test/unit/sonarqube_code_coverage.sh'
                sh 'rm -rf lib'
                sh 'rm -rf elastic_lib'
                script {
                    scannerHome = tool 'sonar-scanner';
                }
                withSonarQubeEnv('Sonar') {
                    sh "${scannerHome}/bin/sonar-scanner -Dproject.settings=sonar-project.JACIDM.properties"
                }
            
            }
        }
        stage('Artifactory upload') {
            steps {
                script {
                    server = Artifactory.server('Artifactory')
                    server.credentialsId = 'svc-highpoint-artifactory'
                    uploadSpec = """{
                        "files": [
                            {
                                "pattern": "./*.py",
                                "recursive": false,
                                "excludePatterns": [],
                                "target": "generic-local/highpoint/elastic-admin/"
                            },
                            {
                                "pattern": "./*.txt",
                                "recursive": false,
                                "excludePatterns": [],
                                "target": "generic-local/highpoint/elastic-admin/"
                            },
                            {
                                "pattern": "./*.md",
                                "recursive": false,
                                "excludePatterns": [],
                                "target": "generic-local/highpoint/elastic-admin/"
                            },
                            {
                                "pattern": "*.TEMPLATE",
                                "recursive": true,
                                "excludePatterns": [],
                                "target": "generic-local/highpoint/elastic-admin/config/"
                            }
                        ]
                    }"""
                    server.upload(uploadSpec)
                }
            }
        }
    }
}
