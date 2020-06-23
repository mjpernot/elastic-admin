# Changelog
All notable changes to this project will be documented in this file.

The format is based on "Keep a Changelog".  This project adheres to Semantic Versioning.


## [0.2.8] - 20200623
### Changed
- Documentation updates.


## [0.2.7] - 20200207
### Fixed
- failed_dumps:  Fixed incorrect parameter passing of class.
- print_dumps:  Set paramters as keyword arguments.
- list_dumps:  Fixed incorrect parameter passing of class.
- run_program: Replaced ElasticSearch with ElasticSearchStatus class.
- check_status:  Fixed incorrect reference to class attribute.
- get_status:  Fixed incorrect reference to class attribute.
- print_dumps:  Fixed incorrect reference to class attribute.
- print_failures:  Fixed incorrect reference to class attribute.


## [0.2.6] - 2019-11-15
- Breaking Change

### Added
- print_failures:  Print the failed dumps in the current repository.
- print_dumps:  Print the dumps in the current repository.

### Changed
- failed_dumps:  Refactored the function to print failed dumps in current repository or all repositories.
- list_dumps:  Refactored the function to print dumps in current repository or all repositories.
- check_status:  Removed -j option.
- \_process_data:  Removed -j option.
- get_status:  Removed -j option.
- \_get_data:  Removed -j option.
- get_status:  Replaced ElasticStatus with ElasticSearchStatus class instance call.
- check_status:  Replaced ElasticStatus with ElasticSearchStatus class instance call.
- run_program:  Replaced ElasticCluster with ElasticSearch class instance call.
- Documentation update.
- elastic.py.TEMPLATE:  Changed host variable to cluster setting.

### Removed
- Removed -j option (JSON formatting) as it's the only format available when checking.


## [0.2.5] - 2019-09-12
### Fixed
- \_get_data:  Added throwaway variables for gen_libs.merge_two_dicts call.
- get_status:  Added throwaway variables for gen_libs.merge_two_dicts call.
- \_process_data:  Added throwaway variables for gen_libs.merge_two_dicts call.
- failed_dumps:  Fixed mutable list/dictionary argument issue.
- list_dumps:  Fixed mutable list/dictionary argument issue.
- check_status:  Fixed mutable list/dictionary argument issue.
- run_program:  Fixed mutable list/dictionary argument issue.
- get_status:  Replaced "gen_libs.merge_2_dicts" with "gen_libs.merge_two_dicts".
- check_status:  Replaced "gen_libs.merge_2_dicts" with "gen_libs.merge_two_dicts".

### Changed
- check_status:  Reduced code complexity in function by calling private function.
- get_status:  Reduced code complexity in function by calling private function.
- main:  Refactored "if" statements.
- run_program:  Changed variables to standard naming convention.
- check_status:  Changed variables to standard naming convention.
- get_status:  Changed variables to standard naming convention.
- list_dumps:  Changed variables to standard naming convention.
- failed_dumps:  Changed variables to standard naming convention.
- list_master:  Changed variable to standard naming convention.
- list_repos:  Changed variable to standard naming convention.
- list_nodes:  Changed variable to standard naming convention.

### Added
- \_process_data:  Private function for check_status().  Process data from database.
- \_get_data:  Private function for get_status().  Get data from database.


## [0.2.4] - 2018-11-19
### Updated
- list_repos:  Replaced "elastic_libs.list_repos" with "elastic_libs.list_repos2" call.
- failed_dumps:  Replaced "elastic_libs.list_dump_format" with "elastic_libs.list_dumps" call.
- get_status:  Changed mutable assignment to copying the list passed.
- check_status:  Changed mutable assignment to copying the list passed.
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
- List_Nodes function.
- List_Master function.
- List_Repos function.
- Failed_Dumps function.

### Removed
- main:  Remove -F, -L, and -R options from XOR function.

### Changed
- main:  Add print titles for main options.
- List_Dumps:  Add check to see if repository name has been set.


## [0.0.1] - 2017-09-18
- Pre-Alpha release.

