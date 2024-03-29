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
                    git branch: "mod/294", credentialsId: "2cfb403c-be21-4fac-94d7-c8cd5c531feb", url: "https://gitlab.code.dicelab.net/JAC-IDM/python-lib.git"
                }
                dir ('elastic_lib') {
                    git branch: "mod/401", credentialsId: "2cfb403c-be21-4fac-94d7-c8cd5c531feb", url: "https://gitlab.code.dicelab.net/JAC-IDM/elastic-lib.git"
                }
                dir ('elastic_lib/lib') {
                    git branch: "mod/294", credentialsId: "2cfb403c-be21-4fac-94d7-c8cd5c531feb", url: "https://gitlab.code.dicelab.net/JAC-IDM/python-lib.git"
                }
                sh """
                virtualenv test_env
                source test_env/bin/activate
                pip2 install mock==2.0.0 --user
                pip2 install elasticsearch==7.0.2 --user
                pip2 install requests==2.19.1 --user
                pip2 install urllib3==1.24.3 --user
                /usr/bin/python ./test/unit/elastic_db_admin/check_status.py
                /usr/bin/python ./test/unit/elastic_db_admin/data_out.py
                /usr/bin/python ./test/unit/elastic_db_admin/failed_dumps.py
                /usr/bin/python ./test/unit/elastic_db_admin/get_data.py
                /usr/bin/python ./test/unit/elastic_db_admin/get_status.py
                /usr/bin/python ./test/unit/elastic_db_admin/help_message.py
                /usr/bin/python ./test/unit/elastic_db_admin/list_dumps.py
                /usr/bin/python ./test/unit/elastic_db_admin/list_master.py
                /usr/bin/python ./test/unit/elastic_db_admin/list_nodes.py
                /usr/bin/python ./test/unit/elastic_db_admin/list_repos.py
                /usr/bin/python ./test/unit/elastic_db_admin/print_dumps.py
                /usr/bin/python ./test/unit/elastic_db_admin/print_failures.py
                /usr/bin/python ./test/unit/elastic_db_admin/process_data.py
                /usr/bin/python ./test/unit/elastic_db_admin/run_program.py
                /usr/bin/python ./test/unit/elastic_db_admin/main.py
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
                    server.credentialsId = 'art-svc-highpoint-dev'
                    uploadSpec = """{
                        "files": [
                            {
                                "pattern": "./*.py",
                                "recursive": false,
                                "excludePatterns": [],
                                "target": "pypi-proj-local/highpoint/elastic-admin/"
                            },
                            {
                                "pattern": "./*.txt",
                                "recursive": false,
                                "excludePatterns": [],
                                "target": "pypi-proj-local/highpoint/elastic-admin/"
                            },
                            {
                                "pattern": "./*.md",
                                "recursive": false,
                                "excludePatterns": [],
                                "target": "pypi-proj-local/highpoint/elastic-admin/"
                            },
                            {
                                "pattern": "*.TEMPLATE",
                                "recursive": true,
                                "excludePatterns": [],
                                "target": "pypi-proj-local/highpoint/elastic-admin/config/"
                            }
                        ]
                    }"""
                    server.upload(uploadSpec)
                }
            }
        }
    }
    post {
        always {
            cleanWs disableDeferredWipeout: true
        }
    }
}
