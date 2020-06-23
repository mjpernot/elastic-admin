# Python project for the adminstration of an Elasticsearch database.
# Classification (U)

# Description:
  Used to adminstrate an Elasticsearch database.  This includes monitoring and checking the status of an Elasticsearch database, monitoring the master and other nodes in Elasticsearch cluster, and monitoring database dump status.


###  This README file is broken down into the following sections:
  * Features
  * Prerequisites
  * Installation
  * Configuration
  * Program Help Function
  * Testing
    - Unit


# Features:
  * Check/display status on general server items.
  * Check/display status on server memory.
  * Check/display status on nodes in the cluster.
  * Check/display status on shards in the database.
  * Check/display status on disks in the database.

# Prerequisites:

  * List of Linux packages that need to be installed on the server.
    - git
    - python-pip

  * Local class/library dependencies within the program structure.
    - lib/gen_class
    - lib/arg_parser
    - lib/gen_libs
    - elastic_lib/elastic_class
    - elastic_lib/elastic_libs


# Installation:

Install these programs using git.
  * Replace **{Python_Project}** with the baseline path of the python program.

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
pip install -r requirements-python-lib.txt --target elastic_lib/lib --trusted-host pypi.appdev.proj.coe.ic.gov
```

# Configuration:

Create configuration file.
  * Replace **{Python_Project}** with the baseline path of the python program.

```
cd config
cp elastic.py.TEMPLATE elastic.py
```

Make the appropriate change to the Elasticsearch environment.
  * Change these entries in the elastic.py file.  List all the servers in the Elasticsearch cluster.
    - host = ["HOST_NAME1", "HOST_NAME2"]

```
vim elastic.py
chmod 600 elastic.py
```


# Program Help Function:

  The program has a -h (Help option) that will show display an usage message.  The help message will usually consist of a description, usage, arugments to the program, example, notes about the program, and any known bugs not yet fixed.  To run the help command:
  * Replace **{Python_Project}** with the baseline path of the python program.

```
{Python_Project}/elastic-admin/elastic_db_admin.py -h
```


# Testing:

# Unit Testing:

### Installation:

Install these programs using git
  * Replace **{Python_Project}** with the baseline path of the python program.
  * Replace **{Branch_Name}** with the name of the Git branch being tested.  See Git Merge Request.

```
umask 022
cd {Python_Project}
git clone --branch {Branch_Name} git@sc.appdev.proj.coe.ic.gov:JAC-DSXD/elastic-admin.git
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
pip install -r requirements-python-lib.txt --target elastic_lib/lib --trusted-host pypi.appdev.proj.coe.ic.gov
```


### Testing:
  * Replace **{Python_Project}** with the baseline path of the python program.

```
cd {Python_Project}/elastic-admin
test/unit/elastic_db_admin/unit_test_run.sh
```

### Code coverage:
```
cd {Python_Project}/elastic-admin
test/unit/elastic_db_admin/code_coverage.sh
```

