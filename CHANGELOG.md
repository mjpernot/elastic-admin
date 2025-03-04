# Changelog
All notable changes to this project will be documented in this file.

The format is based on "Keep a Changelog".  This project adheres to Semantic Versioning.


## [0.3.0] - 2025-02-25
- Field release
- Breaking Changes

- Removed support for Python 2.7.
- Updated python-lib==4.0.0
- Updated elastic-lib==4.1.0
- Updated certifi==2024.12.14
- Updated urllib3==1.26.20

### Added
- process_data: Process data from Elasticsearch database.
- get_data: Get data from Elasticsearch database.

### Changed
- get_status: Replaced \_get_data call with get_data call and replaced \process_data call with process_data call.
- Replaced list() with [].
- Converted strings to f-strings.
- Documentation changes.

### Removed
- \_get_data function.
- \_process_data function.

## [0.2.16] - 2024-11-22
- Updated certifi==2024.6.2 for Python 3.
- Updated distro==1.9.0 for Python 3.
- Added idna==2.10 for Python 3.
- Updated urllib3==1.26.19 for Python 3.
- Updated requests==2.25.0 for Python 3.
- Added elastic-transport==8.10.0 for Python 3.
- Updated elasticsearch==8.11.1 for Python 3.
- Updated python-lib to v3.0.8
- Updated elastic-lib to v4.0.7

### Deprecated
- Support for Python 2.7


## [0.2.15] - 2024-09-27
- Updated simplejson==3.13.2 for Python 3
- Updated python-lib to v3.0.5
- Updated elastic-lib to v4.0.5


## [0.2.14] - 2024-08-08
- Updated simplejson==3.13.2
- Updated requests==2.25.0
- Added certifi==2019.11.28
- Added idna==2.10
- Updated elastic-lib to v4.0.4

### Changed
- Updates to requirements.txt.


## [0.2.13] - 2024-07-31
- Set urllib3 to 1.26.19 for Python 2 for security reasons.
- Set requests to 2.22.0 for Python 2
- Updated elastic-lib to v4.0.3

### Changed
- main: Removed parsing from gen_class.ArgParser call and called arg_parse2 as part of "if" statement.


## [0.2.12] - 2024-03-04
- Updated to work in Red Hat 8
- Updated python-lib to v3.0.3
- Updated elastic-lib to v4.0.2

### Changed
- set elasticsearch to 7.17.9 for Python.
- Set simplejson to 3.12.0 for Python 3.
- Set chardet to 3.0.4 for Python 2.
- Documentation updates.


## [0.2.11] - 2023-10-06
- Updated to work in Elasticsearch v8.5.2
- Replaced the arg_parser code with gen_class.ArgParser code.

### Changed
- Multiple functions: Replaced the arg_parser code with gen_class.ArgParser code.
- main, run_program: Removed gen_libs.get_inst call.
- Documentation update.


## [0.2.10] - 2022-12-22
- Updated to work in Python 3 too
- Updated elastic-lib to v4.0.1
- Upgraded python-lib to v2.9.4

### Changed
- run_program: Set flavor_id for ProgramLock to "elasticadmin".
- config/elastic.py.TEMPLATE: Set new syntax for host entry.
- requirements.txt: Added certifi==2019.11.28 and updated requests==2.6.0 entries.
- Converted imports to use Python 2.7 or Python 3.


## [0.2.9] - 2021-12-03
- Updated to work in Elasticsearch 7.17.0
- Updated elastic-lib to v4.0.0
- Added login credentials and SSL capability.

### Fixed
- main: Added -o option to opt_val_list.
- print_failures, print_dumps: Changed reference call to elasticsearch class instance.

### Added
- data_out: Determine where the data will be sent to such as email, file, or standard out.

### Changed
- print_dumps: Pulled only the database dump list from the elastic_class.get_dump_list call.
- print_failure: Refactored function, also included all states of dumps other then success.
- check_status, get_status:  Added hostname to the data set.
- main:  Set up option settings for email, out file, standard out suppression, and JSON flattening.
- print_failures, print_dumps:  Removed ElasticSearchDump instance call and used the existing ElasticSearchStatus instance.
- get_status:  Remove ElasticSearchStatus instance call and used the passed in ElasticSearchStatus instance, added datetime to data set and replaced print with call to data_out.
- check_status:  Refactored function, added list of nodes to data set and replaced print with call to data_out.
- \_process_data:  Refactored function.
- run_program:  Added connect call, check for elasticsearch connection status, and set login credentials and SSL connection settings.
- config/elastic.py.TEMPLATE:  Added login credentials and SSL entries.
- Removed non-required \*\*kwargs from function parameter list.
- Documentation updates.


## [0.2.8] - 2020-06-23
### Fixed:
- run_program:  Fixed handling command line arguments from SonarQube scan finding.
- main:  Fixed handling command line arguments from SonarQube scan finding.
- list_dumps:  Handle a repository that does not exist.

### Added
- Added global variable print template.

### Changed
- Added print template to a number of functions.
- Changed variable names to standard naming convention in a number of functions.
- Documentation updates.


## [0.2.7] - 2020-02-07
### Fixed
- failed_dumps, list_dumps:  Fixed incorrect parameter passing of class.
- print_dumps:  Set paramters as keyword arguments.
- run_program: Replaced ElasticSearch with ElasticSearchStatus class.
- check_status, get_status, print_dumps, print_failures:  Fixed incorrect reference to class attribute.


## [0.2.6] - 2019-11-15
- Breaking Change

### Added
- print_failures:  Print the failed dumps in the current repository.
- print_dumps:  Print the dumps in the current repository.

### Changed
- failed_dumps:  Refactored the function to print failed dumps in current repository or all repositories.
- list_dumps:  Refactored the function to print dumps in current repository or all repositories.
- check_status, \_process_data, get_status, \_get_data:  Removed -j option.
- get_status, check_status, run_program:  Replaced ElasticStatus with ElasticSearchStatus class instance call.
- elastic.py.TEMPLATE:  Changed host variable to cluster setting.
- Documentation update.

### Removed
- Removed -j option (JSON formatting) as it is the only format available when checking.


## [0.2.5] - 2019-09-12
### Fixed
- \_get_data, get_status, \_process_data:  Added throwaway variables for gen_libs.merge_two_dicts call.
- failed_dumps, list_dumps, check_status, run_program:  Fixed mutable list/dictionary argument issue.
- get_status, check_status:  Replaced "gen_libs.merge_2_dicts" with "gen_libs.merge_two_dicts".

### Changed
- check_status, get_status:  Reduced code complexity in function by calling private function.
- main:  Refactored "if" statements.
- run_program:  Changed variables to standard naming convention in a number of functions.

### Added
- \_process_data:  Private function for check_status().  Process data from database.
- \_get_data:  Private function for get_status().  Get data from database.


## [0.2.4] - 2018-11-19
### Updated
- list_repos:  Replaced "elastic_libs.list_repos" with "elastic_libs.list_repos2" call.
- failed_dumps:  Replaced "elastic_libs.list_dump_format" with "elastic_libs.list_dumps" call.
- get_status, check_status:  Changed mutable assignment to copying the list passed.
- Documentation updates.


## [0.2.3] - 2018-04-17
Breaking Change

### Changed
- list_dumps:  Passed dump list to "elastic_libs.list_dumps" instead of class.
- Changed "gen_libs" calls to new naming schema.
- Changed "arg_parser" calls to new naming schema.
- Changed "gen_class" calls to new naming schema.
- Changed "elastic_class" calls to new naming schema.
- Changed "elastic_libs" calls to new naming schema.
- Changed function names from uppercase to lowercase.
- Setup single-source version control.

### Removed
- main:  Removed opt_xor_dict variable and arg_parser.arg_xor_dict call.


## [0.2.2] - 2018-04-17
### Added
- Added single-source version control.

### Changed
- Run_Program:  Changed "cfg.name" to "cfg.host".
- Changed to use support libraries in sub-directories.


## [0.2.1] - 2017-10-10
### Changed
- Documentation changes.


## [0.2.0] - 2017-10-09
- Beta release.


## [0.1.0] - 2017-10-03
- Alpha release.


## [0.0.6] - 2017-10-02
### Added
- main:  Add disk status to -D option.
- main:  Add disk check to -C option.
- main:  Add -p option for the disk threshold cutoff value.


## [0.0.5] - 2017-09-29
### Changed
- Get_Status:  Refactored function.


## [0.0.4] - 2017-09-28
### Added
- Check_Status function.

### Changed
- main:  Add check status options that include checking for problems in memory, nodes, shards, server, and cluster.


## [0.0.3] - 2017-09-26
### Added
- Get_Status function.

### Changed
- main:  Add status options, that include returning status on cluster, nodes, server, memory, shard, and general status.  Also have status checks for memory, nodes, shards, server and general.


## [0.0.2] - 2017-09-19
### Added
- List_Nodes function
- List_Master function
- List_Repos function
- Failed_Dumps function

### Removed
- main:  Remove -F, -L, and -R options from XOR function.

### Changed
- main:  Add print titles for main options.
- List_Dumps:  Add check to see if repository name has been set.


## [0.0.1] - 2017-09-18
- Pre-Alpha release.

