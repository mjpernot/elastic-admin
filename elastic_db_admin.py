#!/usr/bin/python
# Classification (U)

"""Program:  elastic_db_admin.py

    Description:  Runs administration tasks on an Elasticsearch database.

    Usage:
        elastic_db_admin.py -c file -d path
            {-D [all | general | memory | node | server | shard | disk]
                [-t email_addr [email_addr ...] -s subject_line]
                [-o dir_path/file [-a]] [-j] ]-z]
             -C [all | general | memory | node | server | shard | disk]
                {-m value | -u value | -p value}
                [-t email_addr [email_addr ...] -s subject_line]
                [-o dir_path/file [-a]] [-j] ]-z]
             -L [repo_name] | -F [repo_name] | -R | -M | -N}
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
            -j => Non-flatten JSON data structure.
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
            -t email_addr [email_addr ...] => Enables emailing out all output.
                    Sends the output to one or more email addresses.
                -s Subject Line => Subject line of email.  If none is provided
                    then a default one will be used.
            -o directory_path/file => Directory path and file name for output.
                -a => Append output to the file.  By default will overwrite.
            -j => Non-flatten JSON data structure.
            -z => Suppress standard out.

        -L [repo_name] => Name of respository - list of database dumps for an
            Elasticsearch repository.  If no repo_name is passed then all dumps
            in all repositories are listed.
            -t email_addr [email_addr ...] => Enables emailing out all output.
                    Sends the output to one or more email addresses.
                -s Subject Line => Subject line of email.  If none is provided
                    then a default one will be used.
                -x => Override the default mail command and use mailx.
            -o directory_path/file => Directory path and file name for output.
                -a => Append output to the file.  By default will overwrite.
            -j => Expand JSON data structure.
            -z => Suppress standard out.

        -F [repo_name] => Name of respository - list of database dumps that
            have failed for some reason.  If no repo_name is passed then all 
            failed dumps in all repositories are listed.
            -t email_addr [email_addr ...] => Enables emailing out all output.
                    Sends the output to one or more email addresses.
                -s Subject Line => Subject line of email.  If none is provided
                    then a default one will be used.
                -x => Override the default mail command and use mailx.
            -o directory_path/file => Directory path and file name for output.
                -a => Append output to the file.  By default will overwrite.
            -j => Expand JSON data structure.
            -z => Suppress standard out.

        -R => List of repositories in the Elasticsearch database.

        -M => Return the name of the master node.
            -t email_addr [email_addr ...] => Enables emailing out all output.
                    Sends the output to one or more email addresses.
                -s Subject Line => Subject line of email.  If none is provided
                    then a default one will be used.
                -x => Override the default mail command and use mailx.
            -o directory_path/file => Directory path and file name for output.
                -a => Append output to the file.  By default will overwrite.
            -j => Expand JSON data structure.
            -z => Suppress standard out.

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
            name = ["https://HOST_NAME1:9200", "https://HOST_NAME2:9200"]

            # Login credentials
            user = None
            japd = None

            # SSL connection
            ssl_client_ca = None

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
import pprint

try:
    import simplejson as json
except ImportError:
    import json

# Local
try:
    from .lib import gen_libs
    from .lib import gen_class
    from .elastic_lib import elastic_class
    from .elastic_lib import elastic_libs
    from . import version

except (ValueError, ImportError) as err:
    import lib.gen_libs as gen_libs                     # pylint:disable=R0402
    import lib.gen_class as gen_class                   # pylint:disable=R0402
    import elastic_lib.elastic_class as elastic_class   # pylint:disable=R0402
    import elastic_lib.elastic_libs as elastic_libs     # pylint:disable=R0402
    import version

__version__ = version.__version__

# Global variables


def help_message():

    """Function:  help_message

    Description:  Displays the program's docstring which is the help and usage
        message when -h option is selected.

    Arguments:

    """

    print(__doc__)


def create_header(dtg, name=None):

    """Function:  create_header

    Description:  Create standard dictionary header and add Check entry to
        header if needed.

    Arguments:
        (input) dtg -> TimeFormat instance
        (input) name -> Name of check
        (output) header -> Dictionary header

    """

    header = {
        "Application": "Elastic_DB_Admin",
        "AsOf": dtg.get_time("zulu")}

    if name:
        header["Check"] = name

    return header


def list_nodes(els, **kwargs):                          # pylint:disable=W0613

    """Function:  list_nodes

    Description:  Lists the current nodes in the Elasticsearch cluster.

    Arguments:
        (input) els -> Elasticsearch class instance
        (input) **kwargs:
            args -> ArgParser class instance
            status_call -> Contains class method names for the '-D' option
            check_call -> Contains class method names for the '-C' option
            cfg -> Configuration variables from configuration file
            dtg -> TimeFormat instance

    """

    data = create_header(kwargs.get("dtg"), name="ListNodes")
    data["Nodes"] = els.nodes

#    print(f'\n{"List of Nodes":25}')
#    for item in els.nodes:
#        print(f"{item:25}")

    data_out(data, kwargs.get("args"))


def list_repos(els, **kwargs):                          # pylint:disable=W0613

    """Function:  list_repos

    Description:  Lists the current repositories in the Elasticsearch database.

    Arguments:
        (input) els -> Elasticsearch class instance
        (input) **kwargs:
            args -> ArgParser class instance
            status_call -> Contains class method names for the '-D' option
            check_call -> Contains class method names for the '-C' option
            cfg -> Configuration variables from configuration file
            dtg -> TimeFormat instance

    """

    data = create_header(kwargs.get("dtg"), name="ListRepositories")
    data["Repositories"] = []

    for repo in els.repo_dict:
        tdata = {
            "Repo": repo,
            "Location": els.repo_dict[repo]["settings"]["location"]}
        data["Repositories"].append(tdata)

#    print(f'\n{"List of Repositories":25}')
#    elastic_libs.list_repos2(els.repo_dict)

    data_out(data, kwargs.get("args"))


def list_master(els, **kwargs):                         # pylint:disable=W0613

    """Function:  list_master

    Description:  Displays the current master node name.

    Arguments:
        (input) els-> Elasticsearch class instance
        (input) **kwargs:
            args -> ArgParser class instance
            status_call -> Contains class method names for the '-D' option
            check_call -> Contains class method names for the '-C' option
            cfg -> Configuration variables from configuration file
            dtg -> TimeFormat instance

    """

    data = create_header(kwargs.get("dtg"), name="MasterNode")
    data["Master"] = els.master
#    print(f'\n{"Master Node":25}')
#    print(f"{els.master:25}")
    data_out(data, kwargs.get("args"))


#def print_failures(els, repo):

    """Function:  print_failures

    Description:  Print the failed dumps in the current repository.

    Arguments:
        (input) els -> Elasticsearch class instance
        (input) repo -> Repository name

    """

#    print(f"Repository: {repo:25}")

#    elastic_libs.list_dumps(
#        [dmp for dmp in elastic_class.get_dump_list(els.els, repo=repo)[0]
#         if dmp["state"] != "SUCCESS"])


def failed_dumps(els, **kwargs):

    """Function:  failed_dumps

    Description:  Lists dumps that failed for some reason under the current
        repository.

    Arguments:
        (input) els -> Elasticsearch class instance
        (input) **kwargs:
            args -> ArgParser class instance
            status_call -> Contains class method names for the '-D' option
            check_call -> Contains class method names for the '-C' option
            cfg -> Configuration variables from configuration file
            dtg -> TimeFormat instance

    """

    repo = kwargs.get("args").get_val("-F", def_val=None)
#    args = kwargs.get("args")
#    repo = args.get_val("-F", def_val=None)
    data = create_header(kwargs.get("dtg"), name="FailedDumps")
#    print(f'\n{"List of Failed Dumps:":25}')

    if repo and repo not in els.repo_dict:
        data["Repos"] = []
        print(f"Warning:  Repository {repo} does not exist.")

    elif repo:
        data["Repos"] = [get_dumps(els, repo, get_failed=True)]
#    if repo:
#        print_failures(els, repo)

    else:
        data["Repos"] = []

        for repo in els.get_repo_list():
            data["Repos"].append(get_dumps(els, repo, get_failed=True))

#        for repo in elastic_class.get_repo_list(els.els):
#            print_failures(els, repo)

    data_out(data, kwargs.get("args"))


#def print_dumps(els, repo):

    """Function:  print_dumps

    Description:  Print the dumps in the current repository.

    Arguments:
        (input) els -> Elasticsearch class instance
        (input) repo -> Repository name

    """

#    print(f"Repository: {repo:25}")
#    elastic_libs.list_dumps(elastic_class.get_dump_list(els.els, repo=repo)[0])


def get_dumps(els, repo, **kwargs): 

    """Function:  get_dumps

    Description:  Retrieve dumps from the Elasticsearch cluster and return the
        dumps in a dictionary format.

    Arguments:
        (input) els -> Elasticsearch class instance
        (input) repo -> Repository name
        (input) **kwargs:
            get_failed -> True|False - Return failed dumps
        (output) data -> Dictionary of repository dumps

    """

    get_failed = auto_delete=kwargs.get("get_failed", False)

    data = {repo: []}

    for dump in els.get_dump_list(repo=repo)[0]:
        tdata = None

        if get_failed and dump["state"] != "SUCCESS":
            tdata = {
                "Status": dump["state"], "StartTime": dump["start_time"],
                "ShardSuccess": dump["shards"]["successful"],
                "ShardFail": dump["shards"]["failed"],
                "ShardTotal": dump["shards"]["total"],
                "DumpName": dump["snapshot"]}


        elif not get_failed:
            tdata = {
                "Status": dump["state"], "StartTime": dump["start_time"],
                "ShardSuccess": dump["shards"]["successful"],
                "ShardFail": dump["shards"]["failed"],
                "ShardTotal": dump["shards"]["total"],
                "DumpName": dump["snapshot"]}

        if tdata:
            data[repo].append(tdata)

    return data


def list_dumps(els, **kwargs):

    """Function:  list_dumps

    Description:  Lists the dumps under the current repository or list all
        dumps in all repositories.

    Arguments:
        (input) els -> Elasticsearch class instance
        (input) **kwargs:
            args -> ArgParser class instance
            status_call -> Contains class method names for the '-D' option
            check_call -> Contains class method names for the '-C' option
            cfg -> Configuration variables from configuration file
            dtg -> TimeFormat instance

    """

    repo = kwargs.get("args").get_val("-L", def_val=None)
#    args = kwargs.get("args")
#    repo = args.get_val("-L", def_val=None)
    data = create_header(kwargs.get("dtg"), name="ListDumps")

    if repo and repo not in els.repo_dict:
        data["Repos"] = []
        print(f"Warning:  Repository {repo} does not exist.")

    elif repo:
        data["Repos"] = [get_dumps(els, repo)]

#        print(f'\n{"List of Dumps:":25}')
#        print_dumps(els, repo)

    else:
        data["Repos"] = []

        for repo in els.get_repo_list():
            data["Repos"].append(get_dumps(els, repo))

#        print(f'\n{"List of Dumps:":25}')
#
#        for repo in elastic_class.get_repo_list(els.els):
#            print_dumps(els, repo)

    data_out(data, kwargs.get("args"))


def data_out(data, args):

    """Function:  data_out

    Description:  Determine where the data will be sent to such as email, file,
        standard out and in the type of format it will be displayed.

    Arguments:
        (input) data -> Data to be sent out
        (input) args -> ArgParser class instance

    """

    if not isinstance(data, dict):
        print(f"Error: Is not a dictionary: {data}")
        return

    data = dict(data)
    mode = "a" if args.arg_exist("-a") else "w"
#    indent = 4 if args.arg_exist("-j") else None
    indent = {"indent": 4} if args.arg_exist("-j") else {}

    if args.arg_exist("-t"):
        subj = args.get_val("-s", def_val="Elasticsearch_DB_Admin")
        mail = gen_class.setup_mail(args.get_val("-t"), subj=subj)
#        mail.add_2_msg(json.dumps(data, indent=indent))
        mail.add_2_msg(json.dumps(data, **indent))
        mail.send_mail(use_mailx=args.arg_exist("-x"))

    if args.arg_exist("-o") and indent:
        with open(args.get_val("-o"), mode, encoding="UTF-8") as outfile:
            pprint.pprint(data, stream=outfile, **indent)

    elif args.arg_exist("-o"):
        gen_libs.write_file(
            args.get_val("-o"), mode, json.dumps(data, **indent))

    if not args.arg_exist("-z") and indent:
        pprint.pprint(data, **indent)

    elif not args.arg_exist("-z"):
        print(data)

#    mail = gen_class.setup_mail(
#        args.get_val("-t"),
#        subj=args.get_val("-s", def_val="Elasticsearch_DB_Admin")) \
#        if args.arg_exist("-t") else None
#    ofile = args.get_val("-o") if args.get_val("-o") else None
#
#    if mail:
#        mail.add_2_msg(json.dumps(data, indent=indent))
#        mail.send_mail()
#
#    if ofile:
#        gen_libs.write_file(ofile, mode, json.dumps(data, indent=indent))
#
#    if not args.get_val("-z", def_val=False):
#        print(json.dumps(data, indent=indent))


def get_status(els, **kwargs):

    """Function:  get_status

    Description:  Display status on a number of different options in an
        Elasticsearch database cluster.

    Arguments:
        (input) els -> Elasticsearch class instance
        (input) **kwargs:
            args -> ArgParser class instance
            status_call -> Contains class method names for the '-D' option
            check_call -> Contains class method names for the '-C' option
            cfg -> Configuration variables from configuration file
            dtg -> TimeFormat instance

    """

    args = kwargs.get("args")
    display_list = args.get_val("-D", def_val=[])

    if not display_list or "all" in display_list:
        data = els.get_all()

    else:
        data, _, _ = gen_libs.merge_two_dicts(
            els.get_cluster(), els.get_nodes())

        for opt in display_list:
            data = get_data(data, els, opt, **kwargs)

    data["AsOf"] = datetime.datetime.strftime(
        datetime.datetime.now(), "%Y-%m-%d %H:%M:%S")
    data["HostName"] = socket.gethostname()
    data_out(data, args)


def get_data(data, els, opt, **kwargs):

    """Function:  get_data

    Description:  Get data from Elasticsearch database.

    Arguments:
        (input) data -> Data results
        (input) els -> Elasticsearch status class instance
        (input) opt -> Method to run in class instance
        (input) **kwargs:
            status_call -> Contains class method names for the '-D' option
            args -> ArgParser class instance
            check_call -> Contains class method names for the '-C' option
            cfg -> Configuration variables from configuration file
            dtg -> TimeFormat instance
        (output) data -> Modified data results

    """

    func_call = dict(kwargs.get("status_call"))
    data = dict(data)

    if opt in func_call:
        data, _, _ = gen_libs.merge_two_dicts(
            data, getattr(els, func_call[opt])())

    else:
        print(f"Warning:  Option {opt} is not supported")

    return data


def check_status(els, **kwargs):

    """Function:  check_status

    Description:  Check status on a number of different options in an
        Elasticsearch database cluster.

    Arguments:
        (input) els -> Elasticsearch class instance
        (input) **kwargs:
            args -> ArgParser class instance
            check_call -> Contains class method names for the '-C' option
            status_call -> Contains class method names for the '-D' option
            cfg -> Configuration variables from configuration file
            dtg -> TimeFormat instance

    """

    args = kwargs.get("args")
    check_list = args.get_val("-C", def_val=[])
    cfg = kwargs.get("cfg")
    cutoff_mem = args.get_val("-m", def_val=None)
    cutoff_cpu = args.get_val("-u", def_val=None)
    cutoff_disk = args.get_val("-p", def_val=None)

    els.cutoff_mem = \
        int(cutoff_mem) if cutoff_mem else cfg.cutoff_mem if hasattr(
            cfg, "cutoff_mem") else els.cutoff_mem

    els.cutoff_cpu = \
        int(cutoff_cpu) if cutoff_cpu else cfg.cutoff_cpu if hasattr(
            cfg, "cutoff_cpu") else els.cutoff_cpu

    els.cutoff_disk = \
        int(cutoff_disk) if cutoff_disk else cfg.cutoff_disk if hasattr(
            cfg, "cutoff_disk") else els.cutoff_disk

    if not check_list or "all" in check_list:
        data = els.chk_all(
            cutoff_cpu=els.cutoff_cpu, cutoff_mem=els.cutoff_mem,
            cutoff_disk=els.cutoff_disk)

    else:
        data = process_data(
            check_list, els, cutoff_cpu=els.cutoff_cpu,
            cutoff_mem=els.cutoff_mem, cutoff_disk=els.cutoff_disk, **kwargs)

        if data:
            data["HostName"] = socket.gethostname()
            data, _, _ = gen_libs.merge_two_dicts(data, els.get_cluster())

    if data:
        data["AsOf"] = datetime.datetime.strftime(
            datetime.datetime.now(), "%Y-%m-%d %H:%M:%S")
        data, _, _ = gen_libs.merge_two_dicts(data, els.get_nodes())
        data_out(data, args)


def process_data(check_list, esc, **kwargs):

    """Function:  process_data

    Description:  Process data from Elasticsearch database.

    Arguments:
        (input) check_list -> Contains class method names for the '-C' option
        (input) esc -> Elasticsearch status class instance
        (input) **kwargs:
            check_call -> Contains class method names for the '-C' option
            cutoff_cpu -> Cutoff value for CPU usage
            cutoff_mem -> Cutoff value for Memory usage
            cutoff_disk -> Cutoff value for Disk usage
            args -> ArgParser class instance
            status_call -> Contains class method names for the '-D' option
            cfg -> Configuration variables from configuration file
            dtg -> TimeFormat instance
        (output) err_flag -> True|False - Status of results
        (output) err_msg -> Error message(s)

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
            print(f"Warning:  Option {opt} is not supported")

    return data


def run_program(args, func_dict, **kwargs):

    """Function:  run_program

    Description:  Creates class instance and controls flow of the program.
        Create a program lock to prevent other instantiations from running.

    Arguments:
        (input) args -> ArgParser class instance
        (input) func_dict -> Dictionary list of functions and options
        (input) **kwargs:
            status_call -> Contains class method names for the '-D' option
            check_call -> Contains class method names for the '-C' option

    """

    func_dict = dict(func_dict)
    cfg = gen_libs.load_module(args.get_val("-c"), args.get_val("-d"))
    user = cfg.user if hasattr(cfg, "user") else None
    japd = cfg.japd if hasattr(cfg, "japd") else None
    ca_cert = cfg.ssl_client_ca if hasattr(cfg, "ssl_client_ca") else None
    flavorid = "elasticadmin"
    dtg = gen_class.TimeFormat()
    dtg.create_time()

    try:
        prog_lock = gen_class.ProgramLock(sys.argv, flavor_id=flavorid)

        # Intersect args_array & func_dict to find which functions to call.
        for opt in set(args.get_args_keys()) & set(func_dict.keys()):
            els = elastic_class.ElasticSearchStatus(
                cfg.host, user=user, japd=japd, ca_cert=ca_cert)
            els.connect()

            if els.is_connected:
                func_dict[opt](els, args=args, cfg=cfg, dtg=dtg, **kwargs)

            else:
                print("ERROR:  Failed to connect to Elasticsearch")

        del prog_lock

    except gen_class.SingleInstanceException:
        print(f"Warning:  elastic_db_admin lock in place for: {flavorid}")


def main():

    """Function:  main

    Description:  Initializes program-wide used variables and processes command
        line arguments and values.

    Variables:
        dir_perms_chk -> contains options which will be directories and the
            octal permission settings
        func_dict -> dictionary list for the function calls or other options
        opt_con_req_list -> contains the options that require other options
        opt_def_dict -> contains options with their default values
        opt_multi_list -> contains the options that will have multiple values
        opt_req_list -> contains options that are required for the program
        opt_val_bin -> List of options that allow 0 or 1 value for option
        opt_val -> contains options which require values
        status_call -> contains '-D' option values and associated
            ElasticSearchStatus class method names
        check_call -> contains '-C' option values and associated
            ElasticSearchStatus class method names

    Arguments:
        (input) argv -> Arguments from the command line.

    """

    dir_perms_chk = {"-d": 5}
    func_dict = {
        "-F": failed_dumps, "-L": list_dumps, "-M": list_master,
        "-R": list_repos, "-N": list_nodes, "-D": get_status,
        "-C": check_status}
    opt_con_req_list = {"-s": ["-t"]}
    opt_def_dict = {"-D": [], "-C": []}
    opt_multi_list = ["-D", "-C", "-t", "-s"]
    opt_req_list = ["-c", "-d"]
    opt_val_bin = ["-F", "-L"]
    opt_val = ["-c", "-d", "-m", "-u", "-p", "-o"]
    status_call = {
        "node": "get_node_status", "server": "get_svr_status",
        "memory": "get_mem_status", "shard": "get_shrd_status",
        "general": "get_gen_status", "disk": "get_disk_status"}
    check_call = {
        "node": "chk_nodes", "server": "chk_server", "memory": "chk_mem",
        "shard": "chk_shards", "general": "chk_status", "disk": "chk_disk"}

    # Process argument list from command line
    args = gen_class.ArgParser(
        sys.argv, opt_val=opt_val, opt_val_bin=opt_val_bin,
        multi_val=opt_multi_list, opt_def=opt_def_dict)

    if args.arg_parse2()                                            \
       and not gen_libs.help_func(args, __version__, help_message)  \
       and args.arg_require(opt_req=opt_req_list)                   \
       and args.arg_dir_chk(dir_perms_chk=dir_perms_chk)            \
       and args.arg_cond_req(opt_con_req=opt_con_req_list):
        run_program(
            args, func_dict, status_call=status_call, check_call=check_call)


if __name__ == "__main__":
    sys.exit(main())
