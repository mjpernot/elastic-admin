#!/usr/bin/python
# Classification (U)

"""Program:  elastic_db_admin.py

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
        elastic_db_admin.py -c elastic -d config -C disk -N

"""

# Libraries and Global Variables

# Standard
import sys

# Local
import lib.arg_parser as arg_parser
import lib.gen_libs as gen_libs
import lib.gen_class as gen_class
import elastic_lib.elastic_class as elastic_class
import elastic_lib.elastic_libs as elastic_libs
import version

__version__ = version.__version__


def help_message(**kwargs):

    """Function:  help_message

    Description:  Displays the program's docstring which is the help and usage
        message when -h option is selected.

    Arguments:

    """

    print(__doc__)


def list_nodes(es, **kwargs):

    """Function:  list_nodes

    Description:  Lists the current nodes in the Elasticsearch cluster.

    Arguments:
        (input) es -> Elasticsearch class instance.

    """

    print("\n{0:25}".format("List of Nodes"))

    for x in es.nodes:
        print("{0:25}".format(x))


def list_repos(es, **kwargs):

    """Function:  list_repos

    Description:  Lists the current repositories in the Elasticsearch database.

    Arguments:
        (input) es -> Elasticsearch class instance.

    """

    print("\n{0:25}".format("List of Repositories"))
    elastic_libs.list_repos2(es.repo_dict)


def list_master(es, **kwargs):

    """Function:  list_master

    Description:  Displays the current master node name.

    Arguments:
        (input) es-> Elasticsearch class instance.

    """

    print("\n{0:25}".format("Master Node"))
    print("{0:25}".format(es.master))


def failed_dumps(es, **kwargs):

    """Function:  failed_dumps

    Description:  Lists dumps that failed for some reason under the current
        repository.

    Arguments:
        (input) es -> Elasticsearch class instance.
        (input) **kwargs:
            args_array -> Dict of command line options and values.

    """

    args_array = dict(kwargs.get("args_array"))
    ed = elastic_class.ElasticDump(es.node, args_array.get("-F", None),
                                   es.port, **kwargs)

    if ed.repo_name:
        print("\n{0:25}".format("List of Failed Dumps"))
        elastic_libs.list_dumps(es.dump_list)

    else:
        print("WARNING:  Repository name not set")


def list_dumps(es, **kwargs):

    """Function:  list_dumps

    Description:  Lists the dumps under the current repository.

    Arguments:
        (input) es -> Elasticsearch class instance.
        (input) **kwargs:
            args_array -> Dict of command line options and values.

    """

    args_array = dict(kwargs.get("args_array"))
    ed = elastic_class.ElasticDump(es.node, args_array.get("-L", None),
                                   es.port, **kwargs)

    if ed.repo_name:
        print("\n{0:25}".format("List of Dumps"))
        elastic_libs.list_dumps(ed.dump_list, **kwargs)

    else:
        print("WARNING:  Repository name not set")


def get_status(es, **kwargs):

    """Function:  get_status

    Description:  Display status on a number of different options in an
        Elasticsearch database cluster.

    Arguments:
        (input) es -> Elasticsearch class instance.
        (input) **kwargs:
            args_array -> Dict of command line options and values.
            status_call -> Contains class method names for the '-D' option.

    """

    ec = elastic_class.ElasticStatus(es.node, es.port, **kwargs)
    args_array = dict(kwargs.get("args_array"))
    display_list = list(args_array.get("-D", []))
    json = args_array.get("-j", False)
    func_call = dict(kwargs.get("status_call"))

    if not display_list or "all" in display_list:
        print(ec.get_all(json))

    else:
        if json:
            data = gen_libs.merge_two_dicts(ec.get_cluster(json),
                                            ec.get_nodes(json))

        else:
            data = ec.get_cluster() + "\n" + ec.get_nodes()

        for opt in display_list:
            if opt in func_call:
                if json:
                    # Call class method using option passed and merge results
                    data = \
                         gen_libs.merge_two_dicts(data,
                            getattr(ec, func_call[opt])(json))

                else:
                    # Call method using option passed & concatenate results
                    data = data + "\n" + getattr(ec, func_call[opt])()

            else:
                print("Warning:  Option '{%s}' is not supported" % (opt))

        print(data)


def check_status(es, **kwargs):

    """Function:  check_status

    Description:  Check status on a number of different options in an
        Elasticsearch database cluster.

    Arguments:
        (input) es -> Elasticsearch class instance.
        (input) **kwargs:
            args_array -> Dict of command line options and values.
            check_call -> Contains class method names for the '-C' option.
            cfg -> Configuration variables from configuration file.

    """

    args_array = dict(kwargs.get("args_array"))
    check_list = list(args_array.get("-C", []))
    json = args_array.get("-j", False)
    cutoff_mem = args_array.get("-m", None)
    cutoff_cpu = args_array.get("-u", None)
    cutoff_disk = args_array.get("-p", None)
    func_call = dict(kwargs.get("check_call"))
    cfg = kwargs.get("cfg")

    if cutoff_mem:
        cutoff_mem = int(cutoff_mem)

    if cutoff_cpu:
        cutoff_cpu = int(cutoff_cpu)

    if cutoff_disk:
        cutoff_disk = int(cutoff_disk)

    cfg_cutoff_mem = cfg.cutoff_mem if hasattr(cfg, "cutoff_mem") else None
    cfg_cutoff_cpu = cfg.cutoff_cpu if hasattr(cfg, "cutoff_cpu") else None
    cfg_cutoff_disk = cfg.cutoff_disk if hasattr(cfg, "cutoff_disk") else None

    ec = elastic_class.ElasticStatus(es.node, es.port, cfg_cutoff_mem,
                                     cfg_cutoff_cpu, cfg_cutoff_disk, **kwargs)

    if not check_list or "all" in check_list:
        err_msg = ec.chk_all(json, cutoff_cpu=cutoff_cpu,
                             cutoff_mem=cutoff_mem, cutoff_disk=cutoff_disk)

        if err_msg:
            print(err_msg)

    else:
        err_flag = False
        err_msg = ec.get_cluster(json)

        for opt in check_list:
            if opt in func_call:
                results = getattr(ec, func_call[opt])(json,
                                                      cutoff_cpu=cutoff_cpu,
                                                      cutoff_mem=cutoff_mem,
                                                      cutoff_disk=cutoff_disk)

                if results:
                    err_flag = True

                    if json:
                        err_msg = gen_libs.merge_two_dicts(err_msg, results)

                    else:
                        err_msg = err_msg + "\n" + results

            else:
                print("Warning:  Option '{%s}' is not supported" % (opt))

        if err_flag:
            print(err_msg)


def run_program(args_array, func_dict, **kwargs):

    """Function:  run_program

    Description:  Creates class instance and controls flow of the program.
        Create a program lock to prevent other instantiations from running.

    Arguments:
        (input) args_array -> Dict of command line options and values.
        (input) func_dict -> Dictionary list of functions and options.
        (input) **kwargs:
            status_call -> Contains class method names for the '-D' option.
            check_call -> Contains class method names for the '-C' option.

    """

    args_array = dict(args_array)
    func_dict = dict(func_dict)
    cfg = gen_libs.load_module(args_array["-c"], args_array["-d"])

    try:
        prog_lock = gen_class.ProgramLock(sys.argv, cfg.host)

        # Intersect args_array & func_dict to find which functions to call.
        for opt in set(args_array.keys()) & set(func_dict.keys()):
            es = elastic_class.ElasticCluster(cfg.host, cfg.port, **kwargs)
            func_dict[opt](es, args_array=args_array, cfg=cfg, **kwargs)

        del prog_lock

    except gen_class.SingleInstanceException:
        print("Warning:  elastic_db_admin lock in place for: %s" % (cfg.host))


def main():

    """Function:  main

    Description:  Initializes program-wide used variables and processes command
        line arguments and values.

    Variables:
        check_call -> contains '-C' option values and associated
            Elastic_Status class method names.
        dir_chk_list -> contains options which will be directories.
        func_dict -> dictionary list for the function calls or other options.
        opt_def_dict -> contains options with their default values.
        opt_multi_list -> contains the options that will have multiple values.
        opt_req_list -> contains options that are required for the program.
        opt_val -> List of options that allow 0 or 1 value for option.
        opt_val_list -> contains options which require values.
        status_call -> contains '-D' option values and associated
            Elastic_Status class method names.

    Arguments:
        (input) argv -> Arguments from the command line.

    """

    dir_chk_list = ["-d"]
    func_dict = {"-F": failed_dumps, "-L": list_dumps, "-M": list_master,
                 "-R": list_repos, "-N": list_nodes, "-D": get_status,
                 "-C": check_status}
    opt_def_dict = {"-D": [], "-C": []}
    opt_multi_list = ["-D", "-C"]
    opt_req_list = ["-c", "-d"]
    opt_val = ["-F", "-L"]
    opt_val_list = ["-c", "-d", "-m", "-u", "-p"]
    status_call = {"node": "get_node_status", "server": "get_svr_status",
                   "memory": "get_mem_status", "shard": "get_shrd_status",
                   "general": "get_gen_status", "disk": "get_disk_status"}
    check_call = {"node": "chk_nodes", "server": "chk_server",
                  "memory": "chk_mem", "shard": "chk_shards",
                  "general": "chk_status", "disk": "chk_disk"}

    # Process argument list from command line.
    args_array = arg_parser.arg_parse2(sys.argv, opt_val_list, opt_def_dict,
                                       opt_val=opt_val,
                                       multi_val=opt_multi_list)

    if not gen_libs.help_func(args_array, __version__, help_message) \
       and not arg_parser.arg_require(args_array, opt_req_list) \
       and not arg_parser.arg_dir_chk_crt(args_array, dir_chk_list):
        run_program(args_array, func_dict, status_call=status_call,
                    check_call=check_call)


if __name__ == "__main__":
    sys.exit(main())
