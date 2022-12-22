#!/bin/bash
# Integration testing program for the elastic_db_admin.py module.
# This will run all the integrations tests for this program.
# Will need to run this from the base directory where the module file 
#   is located at.

echo ""
echo "Unit test:"
/usr/bin/python test/integration/elastic_db_admin/check_status.py
/usr/bin/python test/integration/elastic_db_admin/data_out.py
/usr/bin/python test/integration/elastic_db_admin/failed_dumps.py
/usr/bin/python test/integration/elastic_db_admin/get_data.py
/usr/bin/python test/integration/elastic_db_admin/get_status.py
/usr/bin/python test/integration/elastic_db_admin/list_dumps.py
/usr/bin/python test/integration/elastic_db_admin/list_master.py
/usr/bin/python test/integration/elastic_db_admin/list_nodes.py
/usr/bin/python test/integration/elastic_db_admin/list_repos.py
/usr/bin/python test/integration/elastic_db_admin/print_dumps.py
/usr/bin/python test/integration/elastic_db_admin/print_failures.py
/usr/bin/python test/integration/elastic_db_admin/process_data.py
/usr/bin/python test/integration/elastic_db_admin/run_program.py
/usr/bin/python test/integration/elastic_db_admin/main.py
