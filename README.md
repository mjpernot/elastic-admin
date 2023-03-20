# Python project for the adminstration of an Elasticsearch database.
# Classification (U)

# Description:
  Used to adminstrate an Elasticsearch database.  This includes monitoring and checking the status of an Elasticsearch database, monitoring the master and other nodes in Elasticsearch cluster, and monitoring database dump status.


###  This README file is broken down into the following sections:
  * Features
  * Installation
  * Configuration
  * Program Help Function
  * Testing
    - Unit
    - Integration


# Features:
  * Check/display status on general server items.
  * Check/display status on server memory.
  * Check/display status on nodes in the cluster.
  * Check/display status on shards in the database.
  * Check/display status on disks in the database.


# Installation:

Install these programs using git.
  * From here on out, any reference to **{Python_Project}** or **PYTHON_PROJECT** replace with the baseline path of the python program.

```
umask 022
cd {Python_Project}
git clone git@sc.appdev.proj.coe.ic.gov:JAC-DSXD/elastic-admin.git
```

Install/upgrade system modules.

```
cd elastic-admin
sudo bash
umask 022
pip install -r requirements.txt --upgrade --trusted-host pypi.appdev.proj.coe.ic.gov
exit
```

Install supporting classes and libraries.

```
pip install -r requirements-python-lib.txt --target lib --trusted-host pypi.appdev.proj.coe.ic.gov
pip install -r requirements-elastic-lib.txt --target elastic_lib --trusted-host pypi.appdev.proj.coe.ic.gov
pip install -r requirements-elastic-python-lib.txt --target elastic_lib/lib --trusted-host pypi.appdev.proj.coe.ic.gov
```

# Configuration:

Create configuration file.

Make the appropriate changes to the Elasticsearch environment.
  * Change these entries in the elasticsearch set up:
    - host = ["https://HOST_NAME1:9200", "https://HOST_NAME2:9200"]

  * If login credentials are required:
    - user = None
    - japd = None

  * If SSL connections are being used:
    - ssl_client_ca = None

  * Change these entries only if required and you know what you are doing:
    - port = 9200
    - scheme = "https"

```
cd config
cp elastic.py.TEMPLATE elastic.py
vim elastic.py
chmod 600 elastic.py
```


# Program Help Function:

  The program has a -h (Help option) that will show display an usage message.  The help message will usually consist of a description, usage, arugments to the program, example, notes about the program, and any known bugs not yet fixed.  To run the help command:

```
{Python_Project}/elastic-admin/elastic_db_admin.py -h
```


# Testing:

# Unit Testing:

### Installation:

Install the project using the procedures in the Installation section.

### Testing:

```
cd {Python_Project}/elastic-admin
test/unit/elastic_db_admin/unit_test_run.sh
```

### Code coverage:
```
cd {Python_Project}/elastic-admin
test/unit/elastic_db_admin/code_coverage.sh
```


# Integration Testing:

### Installation:

Install the project using the procedures in the Installation section.

### Configuration:

Make the appropriate changes to the Elasticsearch environment.
  * Change these entries in the elasticsearch set up:
    - host = ["https://HOST_NAME1:9200", "https://HOST_NAME2:9200"]

  * If login credentials are required:
    - user = None
    - japd = None

  * If SSL connections are being used:
    - ssl_client_ca = None

  * Change these entries only if required and you know what you are doing:
    - port = 9200
    - scheme = "https"

  * Change the following entries:
    - cutoff_cpu = 70
    - cutoff_disk = 65

```
cd test/integration/elastic_db_admin/config
cp ../../../../config/elastic.py.TEMPLATE elastic.py
vim elastic.py
sudo chown elasticsearch:elasticsearch elastic.py
```

### Testing:
  * These tests must be run as the elasticsearch account:

```
cd {Python_Project}/elastic-admin
test/integration/elastic_db_admin/integration_test_run.sh
```

### Code coverage:

```
cd {Python_Project}/elastic-admin
test/integration/elastic_db_admin/code_coverage.sh
```

