#!/bin/bash
# Unit testing program for the elastic_db_admin.py module.
# This will run all the units tests for this program.
# Will need to run this from the base directory where the module file 
#   is located at.

echo ""
echo "Unit test:"
test/unit/elastic_db_admin/check_status.py
test/unit/elastic_db_admin/failed_dumps.py
#test/unit/elastic_db_admin/get_status.py
test/unit/elastic_db_admin/help_message.py
test/unit/elastic_db_admin/list_dumps.py
test/unit/elastic_db_admin/list_master.py
test/unit/elastic_db_admin/list_nodes.py
test/unit/elastic_db_admin/list_repos.py
test/unit/elastic_db_admin/run_program.py
test/unit/elastic_db_admin/main.py
