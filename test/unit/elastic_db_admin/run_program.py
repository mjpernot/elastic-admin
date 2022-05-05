#!/usr/bin/python
# Classification (U)

"""Program:  run_program.py

    Description:  Unit testing of run_program in elastic_db_admin.py.

    Usage:
        test/unit/elastic_db_admin/run_program.py

    Arguments:

"""

# Libraries and Global Variables

# Standard
import sys
import os

if sys.version_info < (2, 7):
    import unittest2 as unittest
else:
    import unittest

# Third-party
import mock

# Local
sys.path.append(os.getcwd())
import elastic_db_admin
import lib.gen_libs as gen_libs
import version

__version__ = version.__version__


def failed_dumps(els, **kwargs):

    """Function:  failed_dumps

    Description:  This is a function stub for elastic_db_admin.failed_dumps.

    Arguments:

    """

    status = True

    if els and dict(kwargs.get("args_array")):
        status = True

    return status


def list_dumps(els, **kwargs):

    """Function:  list_repos

    Description:  This is a function stub for elastic_db_admin.list_dumps.

    Arguments:

    """

    status = True

    if els and dict(kwargs.get("args_array")):
        status = True

    return status


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


class CfgTest(object):

    """Class:  CfgTest

    Description:  Class which is a representation of a cfg module.

    Methods:
        __init__

    """

    def __init__(self):

        """Method:  __init__

        Description:  Initialization instance of the CfgTest class.

        Arguments:

        """

        self.host = ["SERVER_NAME"]
        self.port = 9200
        self.user = None
        self.japd = None
        self.ssl_client_ca = None
        self.scheme = "https"


class ElasticSearchStatus(object):

    """Class:  ElasticSearchStatus

    Description:  Class stub holder for elastic_class.ElasticSearchStatus
        class.

    Methods:
        __init__
        connect

    """

    def __init__(self):

        """Method:  __init__

        Description:  Class initialization.

        Arguments:

        """

        self.host = "host"
        self.port = 9200
        self.user = None
        self.japd = None
        self.ca_cert = None
        self.scheme = "https"
        self.is_connected = True

    def connect(self):

        """Method:  __init__

        Description:  Class initialization.

        Arguments:

        """

        return True


class UnitTest(unittest.TestCase):

    """Class:  UnitTest

    Description:  Class which is a representation of a unit testing.

    Methods:
        setUp
        test_is_not_connected
        test_is_connected
        test_raise_exception
        test_func_call_multi
        test_func_call_one
        test_func_call_zero

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        self.cfg = CfgTest()
        self.els = ElasticSearchStatus()
        self.args = {"-c": "config_file", "-d": "config_dir", "-M": True}
        self.func_dict = {"-F": failed_dumps, "-L": list_dumps}
        self.proglock = ProgramLock(["cmdline"], "FlavorID")

    @mock.patch("elastic_db_admin.gen_libs.load_module")
    @mock.patch("elastic_db_admin.elastic_class.ElasticSearchStatus")
    @mock.patch("elastic_db_admin.gen_class")
    def test_is_not_connected(self, mock_lock, mock_class, mock_load):

        """Function:  test_is_not_connected

        Description:  Test with failed connection.

        Arguments:

        """

        self.args["-F"] = True
        self.els.is_connected = False

        mock_lock.return_value = self.proglock
        mock_class.return_value = self.els
        mock_load.return_value = self.cfg

        with gen_libs.no_std_out():
            self.assertFalse(
                elastic_db_admin.run_program(self.args, self.func_dict))

    @mock.patch("elastic_db_admin.gen_libs.load_module")
    @mock.patch("elastic_db_admin.elastic_class.ElasticSearchStatus")
    @mock.patch("elastic_db_admin.gen_class")
    def test_is_connected(self, mock_lock, mock_class, mock_load):

        """Function:  test_is_connected

        Description:  Test with successful connection.

        Arguments:

        """

        self.args["-F"] = True

        mock_lock.return_value = self.proglock
        mock_class.return_value = self.els
        mock_load.return_value = self.cfg

        self.assertFalse(
            elastic_db_admin.run_program(self.args, self.func_dict))

    @mock.patch("elastic_db_admin.gen_libs.load_module")
    @mock.patch("elastic_db_admin.elastic_class.ElasticSearchStatus")
    @mock.patch("elastic_db_admin.gen_class.ProgramLock")
    def test_raise_exception(self, mock_lock, mock_class, mock_load):

        """Function:  test_raise_exception

        Description:  Test with raising exception.

        Arguments:

        """

        self.args["-F"] = True

        mock_lock.side_effect = \
            elastic_db_admin.gen_class.SingleInstanceException
        mock_class.return_value = self.els
        mock_load.return_value = self.cfg

        with gen_libs.no_std_out():
            self.assertFalse(
                elastic_db_admin.run_program(self.args, self.func_dict))

    @mock.patch("elastic_db_admin.gen_libs.load_module")
    @mock.patch("elastic_db_admin.elastic_class.ElasticSearchStatus")
    @mock.patch("elastic_db_admin.gen_class")
    def test_func_call_multi(self, mock_lock, mock_class, mock_load):

        """Function:  test_func_call_multi

        Description:  Test run_program function with multiple calls to
            function.

        Arguments:

        """

        self.args["-F"] = True
        self.args["-L"] = True

        mock_lock.return_value = self.proglock
        mock_class.return_value = self.els
        mock_load.return_value = self.cfg

        self.assertFalse(
            elastic_db_admin.run_program(self.args, self.func_dict))

    @mock.patch("elastic_db_admin.gen_libs.load_module")
    @mock.patch("elastic_db_admin.elastic_class.ElasticSearchStatus")
    @mock.patch("elastic_db_admin.gen_class")
    def test_func_call_one(self, mock_lock, mock_class, mock_load):

        """Function:  test_func_call_one

        Description:  Test run_program function with one call to function.

        Arguments:

        """

        self.args["-F"] = True

        mock_lock.return_value = self.proglock
        mock_class.return_value = self.els
        mock_load.return_value = self.cfg

        self.assertFalse(
            elastic_db_admin.run_program(self.args, self.func_dict))

    @mock.patch("elastic_db_admin.gen_libs.load_module")
    @mock.patch("elastic_db_admin.elastic_class.ElasticSearchStatus")
    @mock.patch("elastic_db_admin.gen_class")
    def test_func_call_zero(self, mock_lock, mock_class, mock_load):

        """Function:  test_func_call_zero

        Description:  Test run_program function with zero calls to function.

        Arguments:

        """

        mock_lock.return_value = self.proglock
        mock_class.return_value = self.els
        mock_load.return_value = self.cfg

        self.assertFalse(
            elastic_db_admin.run_program(self.args, self.func_dict))


if __name__ == "__main__":
    unittest.main()
