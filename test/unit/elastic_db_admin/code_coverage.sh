#!/bin/bash
# Unit test code coverage for elastic_db_admin program.
# This will run the Python code coverage module against all unit test modules.
# This will show the amount of code that was tested and which lines of code
#	that was skipped during the test.

coverage erase

echo ""
echo "Running unit test modules in conjunction with coverage"
coverage run -a --source=elastic_db_admin test/unit/elastic_db_admin/check_status.py
coverage run -a --source=elastic_db_admin test/unit/elastic_db_admin/failed_dumps.py
coverage run -a --source=elastic_db_admin test/unit/elastic_db_admin/get_data.py
coverage run -a --source=elastic_db_admin test/unit/elastic_db_admin/get_status.py
coverage run -a --source=elastic_db_admin test/unit/elastic_db_admin/help_message.py
coverage run -a --source=elastic_db_admin test/unit/elastic_db_admin/list_dumps.py
coverage run -a --source=elastic_db_admin test/unit/elastic_db_admin/list_master.py
coverage run -a --source=elastic_db_admin test/unit/elastic_db_admin/list_nodes.py
coverage run -a --source=elastic_db_admin test/unit/elastic_db_admin/list_repos.py
coverage run -a --source=elastic_db_admin test/unit/elastic_db_admin/print_dumps.py
coverage run -a --source=elastic_db_admin test/unit/elastic_db_admin/process_data.py
coverage run -a --source=elastic_db_admin test/unit/elastic_db_admin/run_program.py
coverage run -a --source=elastic_db_admin test/unit/elastic_db_admin/main.py

echo ""
echo "Producing code coverage report"
coverage combine
coverage report -m
 
