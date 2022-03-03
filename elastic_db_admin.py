#!/usr/bin/python
# Classification (U)

"""Program:  elastic_db_admin.py

    Description:  Runs administration tasks on an Elasticsearch database.

    Usage:
        elastic_db_admin.py -c file -d path
            {-D [all | general | memory | node | server | shard | disk]
                [-t email_addr [email_addr ...] -s subject_line]
                [-o dir_path/file [-a]] [-j] ]-z]|
             -C [all | general | memory | node | server | shard | disk]
                {-m value | -u value | -p value} |
             -L [repo_name] |
             -F [repo_name] |
             -R |
             -M |
             -N}
            [-v | -h]

    Arguments:
        -c file => Elasticsearch configuration file.  Required argument.
        -d dir path => Directory path for option '-c'.  Required argument.

        -D [all | general | memory | node | server | shard | disk] => Display
            the current status for the one or more options selected.
                all => Display status on all options.
                general => Display general status information and tasks.
                memory => Display memory usage and total memory.
                node => Display available and failed nodes.
                server => Display available and active CPUs and uptime.
                shard => Display available, used, and failed shards.
                disk => Display disk usage for each node in cluster.
            -t email_addr [email_addr ...] => Enables emailing out all output.
                    Sends the output to one or more email addresses.
                -s Subject Line => Subject line of email.  If none is provided
                    then a default one will be used.
            -o directory_path/file => Directory path and file name for output.
                -a => Append output to the file.  By default will overwrite.
            -j => Flatten JSON data structure.
            -z => Suppress standard out.

        -C [all | general | memory | node | server | shard | disk] => Check
            for problems for the one or more options selected.
                all => Check status on all options.
                general => Check general cluster status information.
                memory => Check for memory usage threshold.
                node => Check for failed nodes.
                server => Check for CPU usage threshold.
                shard => Check for failed shards.
                disk => Check on disk usage.
            -m value => Threshold cutoff for memory usage.
            -u value => Threshold cutoff for cpu usage.
            -p value => Threshold cutoff for disk usage.

        -L [repo_name] => List of database dumps for an Elasticsearch
            repository.  repo_name is name of repository to dump.  If no
            repo_name is passed then all dumps in all repositories are listed.

        -F [repo_name] => List of database dumps that have failed for some
            reason.  repo_name is name of repository to dump.  If no
            repo_name is passed then all dumps in all repositories are checked.

        -R => List of repositories in the Elasticsearch database.

        -M => List the name of the master node.

        -N => List the nodes in the Elasticsearch cluster.

        -v => Display version of this program.
        -h => Help and usage message.

        NOTE 1:  -v or -h overrides all other options.
        NOTE 2:  -m, -u  and -p values override their corresponding counterpart
            in the configuration file, if set.

    Notes:
        Elasticsearch configuration file format (config/elastic.py.TEMPLATE).
        The configuration file format for the Elasticsearch connection to a
        database.

            # Elasticsearch configuration file
            name = ["HOST_NAME1", "HOST_NAME2"]
            port = 9200

            # Login credentials
            user = None
            japd = None

            # SSL connection
            ssl_client_ca = None
            scheme = "https"

            # Threshold cutoffs
            cutoff_mem = 75
            cutoff_cpu = 75
            cutoff_disk = 75

        Configuration modules -> Name is runtime dependent as it can be used to
        connect to different databases with different names.

    Example:
        elastic_db_admin.py -c elastic -d config -C disk -N

"""

# Libraries and Global Variables

# Standard
import sys
import datetime
import socket

# Third Party
import json

# Local
import lib.arg_parser as arg_parser
import lib.gen_libs as gen_libs
import lib.gen_class as gen_class
import elastic_lib.elastic_class as elastic_class
import elastic_lib.elastic_libs as elastic_libs
import version

__version__ = version.__version__

# Global variables
PRT_TEMPLATE = "\n{0:25}"
SUBJ_LINE = "Elasticsearch_DB_Admin"


def help_message():

    """Function:  help_message

    Description:  Displays the program's docstring which is the help and usage
        message when -h option is selected.

    Arguments:

    """

    print(__doc__)


def list_nodes(els, **kwargs):

    """Function:  list_nodes

    Description:  Lists the current nodes in the Elasticsearch cluster.

    Arguments:
        (input) els -> Elasticsearch class instance.
        (input) **kwargs:
            args_array -> Dict of command line options and values.
            status_call -> Contains class method names for the '-D' option.
            check_call -> Contains class method names for the '-C' option.
            cfg -> Configuration variables from configuration file.

    """

    global PRT_TEMPLATE

    print(PRT_TEMPLATE.format("List of Nodes"))

    for item in els.nodes:
        print("{0:25}".format(item))


def list_repos(els, **kwargs):

    """Function:  list_repos

    Description:  Lists the current repositories in the Elasticsearch database.

    Arguments:
        (input) els -> Elasticsearch class instance.
        (input) **kwargs:
            args_array -> Dict of command line options and values.
            status_call -> Contains class method names for the '-D' option.
            check_call -> Contains class method names for the '-C' option.
            cfg -> Configuration variables from configuration file.

    """

    global PRT_TEMPLATE

    print(PRT_TEMPLATE.format("List of Repositories"))
    elastic_libs.list_repos2(els.repo_dict)


def list_master(els, **kwargs):

    """Function:  list_master

    Description:  Displays the current master node name.

    Arguments:
        (input) els-> Elasticsearch class instance.
        (input) **kwargs:
            args_array -> Dict of command line options and values.
            status_call -> Contains class method names for the '-D' option.
            check_call -> Contains class method names for the '-C' option.
            cfg -> Configuration variables from configuration file.

    """

    global PRT_TEMPLATE

    print(PRT_TEMPLATE.format("Master Node"))
    print("{0:25}".format(els.master))


def print_failures(els, repo):

    """Function:  print_failures

    Description:  Print the failed dumps in the current repository.

    Arguments:
        (input) els -> Elasticsearch class instance.
        (input) repo -> Repository name.

    """

    print("Repository: {0:25}".format(repo))

    elastic_libs.list_dumps(
        [dmp for dmp in elastic_class.get_dump_list(els, repo=repo)[0]
         if dmp["state"] != "SUCCESS"])


def failed_dumps(els, **kwargs):

    """Function:  failed_dumps

    Description:  Lists dumps that failed for some reason under the current
        repository.

    Arguments:
        (input) els -> Elasticsearch class instance.
        (input) **kwargs:
            args_array -> Dict of command line options and values.
            status_call -> Contains class method names for the '-D' option.
            check_call -> Contains class method names for the '-C' option.
            cfg -> Configuration variables from configuration file.

    """

    global PRT_TEMPLATE

    args_array = dict(kwargs.get("args_array"))
    repo = args_array.get("-F", None)
    print(PRT_TEMPLATE.format("List of Failed Dumps:"))

    if repo:
        print_failures(els, repo)

    else:
        for repo in elastic_class.get_repo_list(els.els):
            print_failures(els, repo)


def print_dumps(els, repo):

    """Function:  print_dumps

    Description:  Print the dumps in the current repository.

    Arguments:
        (input) els -> Elasticsearch class instance.
        (input) repo -> Repository name.

    """

    print("Repository: {0:25}".format(repo))
    elastic_libs.list_dumps(elastic_class.get_dump_list(els, repo=repo)[0])


def list_dumps(els, **kwargs):

    """Function:  list_dumps

    Description:  Lists the dumps under the current repository or list all
        dumps in all repositories.

    Arguments:
        (input) els -> Elasticsearch class instance.
        (input) **kwargs:
            args_array -> Dict of command line options and values.
            status_call -> Contains class method names for the '-D' option.
            check_call -> Contains class method names for the '-C' option.
            cfg -> Configuration variables from configuration file.

    """

    global PRT_TEMPLATE

    args_array = dict(kwargs.get("args_array"))
    repo = args_array.get("-L", None)

    if repo and repo not in els.repo_dict:
        print("Warning:  Repository '%s' does not exist." % (repo))

    elif repo:
        print(PRT_TEMPLATE.format("List of Dumps:"))
        print_dumps(els, repo)

    else:
        print(PRT_TEMPLATE.format("List of Dumps:"))

        for repo in elastic_class.get_repo_list(els.els):
            print_dumps(els, repo)


def data_out(data, args_array):

    """Function:  data_out

    Description:  Determine where the data will be sent to such as email, file,
        standard out and in the type of format it will be displayed.

    Arguments:
        (input) data -> Data to be sent out.
        (input) args_array -> Dict of command line options and values.

    """

    global SUBJ_LINE

    args_array = dict(args_array)
    data = dict(data)
    mode = "a" if args_array.get("-a") else "w"
    indent = 4 if args_array.get("-j") else None
    mail = gen_class.setup_mail(
        args_array.get("-t"),
        subj=args_array.get("-s", SUBJ_LINE)) if args_array.get("-t") else None
    ofile = args_array["-o"] if args_array.get("-o") else None

    if mail:
        mail.add_2_msg(json.dumps(data, indent=indent))
        mail.send_mail()

    if ofile:
        gen_libs.write_file(ofile, mode, json.dumps(data, indent=indent))

    if not args_array.get("-z", False):
        print(json.dumps(data, indent=indent))


def get_status(els, **kwargs):

    """Function:  get_status

    Description:  Display status on a number of different options in an
        Elasticsearch database cluster.

    Arguments:
        (input) els -> Elasticsearch class instance.
        (input) **kwargs:
            args_array -> Dict of command line options and values.
            status_call -> Contains class method names for the '-D' option.
            check_call -> Contains class method names for the '-C' option.
            cfg -> Configuration variables from configuration file.

    """

    args_array = dict(kwargs.get("args_array"))
    display_list = list(args_array.get("-D", []))

    if not display_list or "all" in display_list:
        data = els.get_all()

    else:
        data, _, _ = gen_libs.merge_two_dicts(
            els.get_cluster(), els.get_nodes())

        for opt in display_list:
            data = _get_data(data, els, opt, **kwargs)

    data["AsOf"] = datetime.datetime.strftime(
        datetime.datetime.now(), "%Y-%m-%d %H:%M:%S")
    data["HostName"] = socket.gethostname()
    data_out(data, args_array)


def _get_data(data, els, opt, **kwargs):

    """Function:  _get_data

    Description:  Private function for get_status function.  Get data from
        Elasticsearch database.

    Arguments:
        (input) data -> Data results.
        (input) els -> Elasticsearch status class instance.
        (input) opt -> Method to run in class instance.
        (input) **kwargs:
            status_call -> Contains class method names for the '-D' option.
            args_array -> Dict of command line options and values.
            check_call -> Contains class method names for the '-C' option.
            cfg -> Configuration variables from configuration file.
        (output) data -> Modified data results.

    """

    func_call = dict(kwargs.get("status_call"))
    data = dict(data)

    if opt in func_call:
        data, _, _ = gen_libs.merge_two_dicts(
            data, getattr(els, func_call[opt])())

    else:
        print("Warning:  Option '{%s}' is not supported" % (opt))

    return data


def check_status(els, **kwargs):

    """Function:  check_status

    Description:  Check status on a number of different options in an
        Elasticsearch database cluster.

    Arguments:
        (input) els -> Elasticsearch class instance.
        (input) **kwargs:
            args_array -> Dict of command line options and values.
            check_call -> Contains class method names for the '-C' option.
            status_call -> Contains class method names for the '-D' option.
            cfg -> Configuration variables from configuration file.

    """

    args_array = dict(kwargs.get("args_array"))
    check_list = list(args_array.get("-C", []))
    cfg = kwargs.get("cfg")
    cutoff_mem = args_array.get("-m", None)
    cutoff_cpu = args_array.get("-u", None)
    cutoff_disk = args_array.get("-p", None)

    if cutoff_mem:
        els.cutoff_mem = int(cutoff_mem)

    else:
        els.cutoff_mem = cfg.cutoff_mem if hasattr(
            cfg, "cutoff_mem") else els.cutoff_mem

    if cutoff_cpu:
        els.cutoff_cpu = int(cutoff_cpu)

    else:
        els.cutoff_cpu = cfg.cutoff_cpu if hasattr(
            cfg, "cutoff_cpu") else els.cutoff_cpu

    if cutoff_disk:
        els.cutoff_disk = int(cutoff_disk)

    else:
        els.cutoff_disk = cfg.cutoff_disk if hasattr(
            cfg, "cutoff_disk") else els.cutoff_disk

    if not check_list or "all" in check_list:
        data = els.chk_all(
            cutoff_cpu=els.cutoff_cpu, cutoff_mem=els.cutoff_mem,
            cutoff_disk=els.cutoff_disk)

        if data:
            data["AsOf"] = datetime.datetime.strftime(
                datetime.datetime.now(), "%Y-%m-%d %H:%M:%S")
            data, _, _ = gen_libs.merge_two_dicts(data, els.get_nodes())

    else:
        data = _process_data(
            check_list, els, cutoff_cpu=els.cutoff_cpu,
            cutoff_mem=els.cutoff_mem, cutoff_disk=els.cutoff_disk, **kwargs)

        if data:
            data["AsOf"] = datetime.datetime.strftime(
                datetime.datetime.now(), "%Y-%m-%d %H:%M:%S")
            data["HostName"] = socket.gethostname()
            data, _, _ = gen_libs.merge_two_dicts(data, els.get_cluster())
            data, _, _ = gen_libs.merge_two_dicts(data, els.get_nodes())

    if data:
        data_out(data, args_array)


def _process_data(check_list, esc, **kwargs):

    """Function:  _process_data

    Description:  Private function for check_status function.  Process data
        from Elasticsearch database.

    Arguments:
        (input) check_list -> Contains class method names for the '-C' option.
        (input) esc -> Elasticsearch status class instance.
        (input) **kwargs:
            check_call -> Contains class method names for the '-C' option.
            cutoff_cpu -> Cutoff value for CPU usage.
            cutoff_mem -> Cutoff value for Memory usage.
            cutoff_disk -> Cutoff value for Disk usage.
            args_array -> Dict of command line options and values.
            status_call -> Contains class method names for the '-D' option.
            cfg -> Configuration variables from configuration file.
        (output) err_flag -> True|False - Status of results.
        (output) err_msg -> Error message(s).

    """

    check_list = list(check_list)
    func_call = dict(kwargs.get("check_call"))
    cutoff_cpu = kwargs.get("cutoff_cpu")
    cutoff_mem = kwargs.get("cutoff_mem")
    cutoff_disk = kwargs.get("cutoff_disk")
    data = {}

    for opt in check_list:
        if opt in func_call:
            results = getattr(esc, func_call[opt])(
                cutoff_cpu=cutoff_cpu, cutoff_mem=cutoff_mem,
                cutoff_disk=cutoff_disk)

            if results:
                data, _, _ = gen_libs.merge_two_dicts(data, results)

        else:
            print("Warning:  Option '{%s}' is not supported" % (opt))

    return data


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

    cmdline = gen_libs.get_inst(sys)
    args_array = dict(args_array)
    func_dict = dict(func_dict)
    cfg = gen_libs.load_module(args_array["-c"], args_array["-d"])
    user = cfg.user if hasattr(cfg, "user") else None
    japd = cfg.japd if hasattr(cfg, "japd") else None
    ca_cert = cfg.ssl_client_ca if hasattr(cfg, "ssl_client_ca") else None
    scheme = cfg.scheme if hasattr(cfg, "scheme") else "https"

    try:
        prog_lock = gen_class.ProgramLock(cmdline.argv, cfg.host)

        # Intersect args_array & func_dict to find which functions to call.
        for opt in set(args_array.keys()) & set(func_dict.keys()):
            els = elastic_class.ElasticSearchStatus(
                cfg.host, port=cfg.port, user=user, japd=japd, ca_cert=ca_cert,
                scheme=scheme)
            els.connect()

            if els.is_connected:
                func_dict[opt](els, args_array=args_array, cfg=cfg, **kwargs)

            else:
                print("ERROR:  Failed to connect to Elasticsearch")

        del prog_lock

    except gen_class.SingleInstanceException:
        print("Warning:  elastic_db_admin lock in place for: %s" % (cfg.host))


def main():

    """Function:  main

    Description:  Initializes program-wide used variables and processes command
        line arguments and values.

    Variables:
        dir_chk_list -> contains options which will be directories.
        func_dict -> dictionary list for the function calls or other options.
        opt_con_req_list -> contains the options that require other options.
        opt_def_dict -> contains options with their default values.
        opt_multi_list -> contains the options that will have multiple values.
        opt_req_list -> contains options that are required for the program.
        opt_val -> List of options that allow 0 or 1 value for option.
        opt_val_list -> contains options which require values.
        status_call -> contains '-D' option values and associated
            ElasticSearchStatus class method names.
        check_call -> contains '-C' option values and associated
            ElasticSearchStatus class method names.

    Arguments:
        (input) argv -> Arguments from the command line.

    """

    cmdline = gen_libs.get_inst(sys)
    dir_chk_list = ["-d"]
    func_dict = {"-F": failed_dumps, "-L": list_dumps, "-M": list_master,
                 "-R": list_repos, "-N": list_nodes, "-D": get_status,
                 "-C": check_status}
    opt_con_req_list = {"-s": ["-t"]}
    opt_def_dict = {"-D": [], "-C": []}
    opt_multi_list = ["-D", "-C", "-t", "-s"]
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
    args_array = arg_parser.arg_parse2(
        cmdline.argv, opt_val_list, opt_def_dict, opt_val=opt_val,
        multi_val=opt_multi_list)

    if not gen_libs.help_func(args_array, __version__, help_message) \
       and not arg_parser.arg_require(args_array, opt_req_list) \
       and not arg_parser.arg_dir_chk_crt(args_array, dir_chk_list) \
       and arg_parser.arg_cond_req(args_array, opt_con_req_list):
        run_program(args_array, func_dict, status_call=status_call,
                    check_call=check_call)


if __name__ == "__main__":
    sys.exit(main())
