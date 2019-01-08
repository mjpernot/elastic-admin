# Changelog
All notable changes to this project will be documented in this file.

The format is based on "Keep a Changelog".  This project adheres to Semantic Versioning.


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

