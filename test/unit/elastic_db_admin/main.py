# Classification (U)

"""Program:  main.py

    Description:  Unit testing of main in elastic_db_admin.py.

    Usage:
        test/unit/elastic_db_admin/main.py

    Arguments:
        None

"""

# Libraries and Global Variables

# Standard
import sys
import os
import unittest
import mock

# Local
sys.path.append(os.getcwd())
import elastic_db_admin
import version

# Version
__version__ = version.__version__


class ArgParser(object):

    """Class:  ArgParser

    Description:  Class stub holder for gen_class.ArgParser class.

    Methods:
        __init__
        arg_cond_req
        arg_dir_chk
        arg_require

    """

    def __init__(self):

        """Method:  __init__

        Description:  Class initialization.

        Arguments:

        """

        self.cmdline = None
        self.args_array = dict()
        self.opt_con_req = None
        self.opt_con_req2 = True
        self.opt_req = None
        self.opt_req2 = True
        self.dir_perms_chk = None
        self.dir_perms_chk2 = True

    def arg_cond_req(self, opt_con_req):

        """Method:  arg_cond_req

        Description:  Method stub holder for gen_class.ArgParser.arg_cond_req.

        Arguments:

        """

        self.opt_con_req = opt_con_req

        return self.opt_con_req2

    def arg_dir_chk(self, dir_perms_chk):

        """Method:  arg_dir_chk

        Description:  Method stub holder for gen_class.ArgParser.arg_dir_chk.

        Arguments:

        """

        self.dir_perms_chk = dir_perms_chk

        return self.dir_perms_chk2

    def arg_require(self, opt_req):

        """Method:  arg_require

        Description:  Method stub holder for gen_class.ArgParser.arg_require.

        Arguments:

        """

        self.opt_req = opt_req

        return self.opt_req2


class ProgramLock(object):

    """Class:  ProgramLock

    Description:  Class stub holder for gen_class.ProgramLock class.

    Methods:
        __init__

    """

    def __init__(self, cmdline, flavor):

        """Method:  __init__

        Description:  Class initialization.

        Arguments:

        """

        self.cmdline = cmdline
        self.flavor = flavor


class UnitTest(unittest.TestCase):

    """Class:  UnitTest

    Description:  Class which is a representation of a unit testing.

    Methods:
        setUp
        test_help_true
        test_help_false
        test_require_true
        test_require_false
        test_dir_chk_crt_true
        test_dir_chk_crt_false
        test_arg_cond_req_false
        test_arg_cond_req_true
        test_run_program
#STOPPED HERE
    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        self.args = ArgParser()
        self.args.args_array = {
            "-c": "config_file", "-d": "config_dir", "-R": True}
        self.proglock = ProgramLock(["cmdline"], "Hostname")

    @mock.patch("elastic_db_admin.gen_libs.help_func")
    @mock.patch("elastic_db_admin.gen_class.ArgParser")
    def test_help_true(self, mock_arg, mock_help):

        """Function:  test_help_true

        Description:  Test with help_func returns True.

        Arguments:

        """

        mock_arg.return_value = self.args
        mock_help.return_value = True

        self.assertFalse(elastic_db_admin.main())

    @mock.patch("elastic_db_admin.gen_libs.help_func")
    @mock.patch("elastic_db_admin.gen_class.ArgParser")
    def test_help_false(self, mock_arg, mock_help):

        """Function:  test_help_false

        Description:  Test with help_func returns False.

        Arguments:

        """

        mock_arg.arg_parse2.return_value = self.args
        mock_help.return_value = False
        mock_arg.arg_require.return_value = True

        self.assertFalse(elastic_db_admin.main())

    @mock.patch("elastic_db_admin.gen_libs.help_func")
    @mock.patch("elastic_db_admin.gen_class.ArgParser")
    def test_require_true(self, mock_arg, mock_help):

        """Function:  test_require_true

        Description:  Test with arg_require returns True.

        Arguments:

        """

        mock_arg.arg_parse2.return_value = self.args
        mock_help.return_value = False
        mock_arg.arg_require.return_value = True

        self.assertFalse(elastic_db_admin.main())

    @mock.patch("elastic_db_admin.gen_libs.help_func")
    @mock.patch("elastic_db_admin.gen_class.ArgParser")
    def test_require_false(self, mock_arg, mock_help):

        """Function:  test_require_false

        Description:  Test with arg_require returns False.

        Arguments:

        """

        mock_arg.arg_parse2.return_value = self.args
        mock_help.return_value = False
        mock_arg.arg_require.return_value = False
        mock_arg.arg_dir_chk_crt.return_value = True

        self.assertFalse(elastic_db_admin.main())

    @mock.patch("elastic_db_admin.gen_libs.help_func")
    @mock.patch("elastic_db_admin.gen_class.ArgParser")
    def test_dir_chk_crt_true(self, mock_arg, mock_help):

        """Function:  test_dir_chk_crt_true

        Description:  Test with arg_dir_chk_crt returns True.

        Arguments:

        """

        mock_arg.arg_parse2.return_value = self.args
        mock_help.return_value = False
        mock_arg.arg_require.return_value = False
        mock_arg.arg_dir_chk_crt.return_value = True

        self.assertFalse(elastic_db_admin.main())

    @mock.patch("elastic_db_admin.gen_libs.help_func")
    @mock.patch("elastic_db_admin.gen_class.ArgParser")
    def test_dir_chk_crt_false(self, mock_arg, mock_help):

        """Function:  test_dir_chk_crt_false

        Description:  Test with arg_dir_chk_crt returns False.

        Arguments:

        """

        mock_arg.arg_parse2.return_value = self.args
        mock_help.return_value = False
        mock_arg.arg_require.return_value = False
        mock_arg.arg_dir_chk_crt.return_value = False
        mock_arg.arg_cond_req.return_value = False

        self.assertFalse(elastic_db_admin.main())

    @mock.patch("elastic_db_admin.gen_libs.help_func")
    @mock.patch("elastic_db_admin.gen_class.ArgParser")
    def test_arg_cond_req_false(self, mock_arg, mock_help):

        """Function:  test_arg_cond_req_false

        Description:  Test with arg_cond_req returns False.

        Arguments:

        """

        mock_arg.arg_parse2.return_value = self.args
        mock_help.return_value = False
        mock_arg.arg_require.return_value = False
        mock_arg.arg_dir_chk_crt.return_value = False
        mock_arg.arg_cond_req.return_value = False

        self.assertFalse(elastic_db_admin.main())

    @mock.patch("elastic_db_admin.run_program", mock.Mock(return_value=True))
    @mock.patch("elastic_db_admin.gen_class.ProgramLock")
    @mock.patch("elastic_db_admin.gen_libs.help_func")
    @mock.patch("elastic_db_admin.gen_class.ArgParser")
    def test_arg_cond_req_true(self, mock_arg, mock_help, mock_lock):

        """Function:  test_arg_cond_req_true

        Description:  Test with arg_cond_req returns True.

        Arguments:

        """

        mock_arg.arg_parse2.return_value = self.args
        mock_help.return_value = False
        mock_arg.arg_require.return_value = False
        mock_arg.arg_dir_chk_crt.return_value = False
        mock_arg.arg_cond_req.return_value = True
        mock_lock.return_value = self.proglock

        self.assertFalse(elastic_db_admin.main())

    @mock.patch("elastic_db_admin.run_program", mock.Mock(return_value=True))
    @mock.patch("elastic_db_admin.gen_class.ProgramLock")
    @mock.patch("elastic_db_admin.gen_libs.help_func")
    @mock.patch("elastic_db_admin.gen_class.ArgParser")
    def test_run_program(self, mock_arg, mock_help, mock_lock):

        """Function:  test_run_program

        Description:  Test run_program function.

        Arguments:

        """

        mock_arg.arg_parse2.return_value = self.args
        mock_help.return_value = False
        mock_arg.arg_require.return_value = False
        mock_arg.arg_dir_chk_crt.return_value = False
        mock_arg.arg_cond_req.return_value = True
        mock_lock.return_value = self.proglock

        self.assertFalse(elastic_db_admin.main())


if __name__ == "__main__":
    unittest.main()
