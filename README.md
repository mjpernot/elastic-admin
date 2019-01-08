# Python project for the adminstration of an Elasticsearch database.
# Classification (U)

# Description:
  This project is used to adminstrate an Elasticsearch database.  This includes monitoring and checking the status of an Elasticsearch database, monitoring the master and other nodes in Elasticsearch cluster, and monitoring database dump status.


###  This README file is broken down into the following sections:
  * Features
  * Prerequisites
  * Installation
  * Configuration
  * Program Description
  * Program Help Function
  * Help Message
  * Testing
    - Unit
    - Integration
    - Blackbox


# Features:
  * Check/display status on general server items.
  * Check/display status on server memory.
  * Check/display status on nodes in the cluster.
  * Check/display status on shards in the database.
  * Check/display status on disks in the database.

# Prerequisites:

  * List of Linux packages that need to be installed on the server.
    - python-libs
    - python-devel
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
pip install -r requirements-requests-lib.txt --target elastic_lib/requests_lib --trusted-host pypi.appdev.proj.coe.ic.gov
```

# Configuration:

Create configuration file.
  * Replace **{Python_Project}** with the baseline path of the python program.

```
cd config
cp elastic.py.TEMPLATE elastic.py
```

Make the appropriate change to the environment.
  * Make the appropriate changes to connect to Elasticsearch.
    - host = "HOSTNAME"

```
vim elastic.py
chmod 600 elastic.py
```


# Program Descriptions:
### Program: elastic_db_admin.py
##### Description: Runs administration tasks on an Elasticsearch database.


# Program Help Function:

  The program has a -h (Help option) that will show display an usage message.  The help message will usually consist of a description, usage, arugments to the program, example, notes about the program, and any known bugs not yet fixed.  To run the help command:
  * Replace **{Python_Project}** with the baseline path of the python program.

```
{Python_Project}/elastic-admin/elastic_db_admin.py -h
```


# Help Message:
  Below is the help message for the program.  Recommend running the -h option on the command line to see the latest help message.

    Program:  elastic_db_admin.py

    Description:  Runs administration tasks on an Elasticsearch database.

    Usage:
        elastic_db_admin.py -c file -d path {-L [repo_name] | -R | -M | -N |
        -D [option1 {option2 ...}] | -D [option1 {option2 ...}] |
        -F [repo_name] {-j} {-m value | -u value} [-v | -h]

    Arguments:
        -C [all | general | memory | node | server | shard | disk] => Check
            for problems for the one or more options selected.
                all => Check status on all options.
                general => Check general cluster status information.
                memory => Check for memory usage threshold.
                node => Check for failed nodes.
                server => Check for CPU usage threshold.
                shard => Check for failed shards.
                disk => Check on disk usage.
        -D [all | general | memory | node | server | shard | disk] => Display
            the current status for the one or more options selected.
                all => Display status on all options.
                general => Display general status information and tasks.
                memory => Display memory usage and total memory.
                node => Display available and failed nodes.
                server => Display available and active CPUs and uptime.
                shard => Display available, used, and failed shards.
                disk => Display disk usage for each node in cluster.
        -L [repo_name] => List of database dumps for an Elasticsearch
            database.  repo_name is name of repository to dump.  repo_name is
            required if multiple repositories exist.
        -F [repo_name] => List of database dumps that have failed for some
            reason.  repo_name is name of repository to dump.  repo_name is
            required if multiple repositories exist.
        -R => List of repositories in the Elasticsearch database.
        -M => List the name of the master node.
        -N => List the nodes in the Elasticsearch cluster.
        -c file => ISSE Guard configuration file.  Required argument.
        -d dir path => Directory path for option '-c'.  Required argument.
        -j => Display output in JSON format, if possible.
        -m value => Threshold cutoff for memory usage.  Used with '-C' option.
        -u value => Threshold cutoff for cpu usage.  Used with '-C' option.
        -p value => Threshold cutoff for disk usage.  Used with '-C' option.
        -v => Display version of this program.
        -h => Help and usage message.

        NOTE 1:  -v or -h overrides all other options.
        NOTE 2:  -m, -u  and -p values override their corresponding counterpart
            in the configuration file, if set.

    Notes:
        Elasticsearch configuration file format (elastic.py).  The
        configuration file format for the Elasticsearch connection to a
        database.

            # Elasticsearch configuration file.
            host = "HOSTNAME"
            port = PORT_NUMBER (default of Elasticsearch is 9200)
            # Threshold cutoff for Memory check in whole numbers
            cutoff_mem = 75
            # Threshold cutoff for CPU usage check in whole numbers
            cutoff_cpu = 75
            # Threshold cutoff for Disk usage check in whole numbers
            cutoff_disk = 75
        
        Configuration modules -> Name is runtime dependent as it can be used to
        connect to different databases with different names.

    Example:
        elastic_db_admin.py -c elastic -d config -D disk -N


# Testing:


# Unit Testing:

### Description: Testing consists of unit testing for the functions in the elastic_db_admin.py program.

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
pip install -r requirements-requests-lib.txt --target elastic_lib/requests_lib --trusted-host pypi.appdev.proj.coe.ic.gov
```


# Unit test runs for elastic_db_admin.py:
  * Replace **{Python_Project}** with the baseline path of the python program.

```
cd {Python_Project}/elastic-admin
```

### Unit:  help_message
```
test/unit/elastic_db_admin/help_message.py
```

### Unit:  
```
test/unit/elastic_db_admin/
```

### Unit:  
```
test/unit/elastic_db_admin/
```

### Unit:  run_program
```
test/unit/elastic_db_admin/run_program.py
```

### Unit:  main
```
test/unit/elastic_db_admin/main.py
```

### All unit testing
```
test/unit/elastic_db_admin/unit_test_run.sh
```

### Code coverage program
```
test/unit/elastic_db_admin/code_coverage.sh
```


# Integration Testing:

### Description: Testing consists of integration testing of functions in the elastic_db_admin.py program.

### Installation:
  * Replace **{Python_Project}** with the baseline path of the python program.

Install these programs using git.

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
pip install -r requirements-requests-lib.txt --target elastic_lib/requests_lib --trusted-host pypi.appdev.proj.coe.ic.gov
```

### Configuration:
  * Replace **{Python_Project}** with the baseline path of the python program.

Create Elasticsearch configuration file.

```
cd test/integration/elastic_db_admin/config
cp ../../../../config/elastic.py.TEMPLATE elastic.py
```

Make the appropriate change to the environment.
  * Make the appropriate changes to connect to Elasticsearch.
    - host = "HOSTNAME"

```
vim elastic.py
chmod 600 elastic.py
```

# Integration test runs for elastic_db_admin.py:
  * Replace **{Python_Project}** with the baseline path of the python program.

```
cd {Python_Project}/elastic-admin
```

### Integration:  
```
test/integration/elastic_db_admin/
```

### All integration testing
```
test/integration/elastic_db_admin/integration_test_run.sh
```

### Code coverage program
```
test/integration/elastic_db_admin/code_coverage.sh
```


# Blackbox Testing:

### Description: Testing consists of blackbox testing of the elastic_db_admin.py program.

### Installation:

Install these programs using git.
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
pip install -r requirements-requests-lib.txt --target elastic_lib/requests_lib --trusted-host pypi.appdev.proj.coe.ic.gov
```

### Configuration:

Create Elasticsearch configuration file.
  * Replace **{Python_Project}** with the baseline path of the python program.

```
cd test/blackbox/elastic_db_admin/config
cp ../../../../config/elastic.py.TEMPLATE elastic.py
```

Make the appropriate change to the  environment.
  *  Make the appropriate changes to connect to Elasticsearch.
     - host = "HOSTNAME"

```
vim elastic.py
chmod 600 elastic.py
```

# Blackbox test run for elastic_db_admin.py:
  * Replace **{Python_Project}** with the baseline path of the python program.

```
cd {Python_Project}/elastic-admin
```

### Blackbox:  
```
test/blackbox/elastic_db_admin/blackbox_test.sh
```

