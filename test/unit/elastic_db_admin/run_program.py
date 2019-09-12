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


def failed_dumps(es, **kwargs):

    """Function:  failed_dumps

    Description:  This is a function stub for elastic_db_admin.failed_dumps.

    Arguments:
        es -> Stub argument holder.

    """

    pass


def list_dumps(es, **kwargs):

    """Function:  list_repos

    Description:  This is a function stub for elastic_db_admin.list_dumps.

    Arguments:
        es -> Stub argument holder.

    """

    pass


class UnitTest(unittest.TestCase):

    """Class:  UnitTest

    Description:  Class which is a representation of a unit testing.

    Methods:
        setUp -> Unit testing initilization.
        test_func_call_multi -> Test run_program with multiple calls.
        test_func_call_one -> Test run_program with one call to function.
        test_func_call_zero -> Test run_program with zero calls to function.

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        class CfgTest(object):

            """Class:  CfgTest

            Description:  Class which is a representation of a cfg module.

            Methods:
                __init__ -> Initialize configuration environment.

            """

            def __init__(self):

                """Method:  __init__

                Description:  Initialization instance of the CfgTest class.

                Arguments:

                """

                self.host = ["SERVER_NAME"]
                self.port = 9200

        self.ct = CfgTest()

        self.args = {"-c": "config_file", "-d": "config_dir", "-M": True}
        self.func_dict = {"-F": failed_dumps, "-L": list_dumps}

    @mock.patch("elastic_db_admin.gen_libs.load_module")
    @mock.patch("elastic_db_admin.elastic_class.ElasticCluster")
    @mock.patch("elastic_db_admin.gen_class.ProgramLock")
    def test_raise_exception(self, mock_lock, mock_class, mock_load):

        """Function:  test_raise_exception

        Description:  Test with raising exception.

        Arguments:

        """

        self.args["-F"] = True

        mock_lock.side_effect = \
            elastic_db_admin.gen_class.SingleInstanceException
        mock_class.return_value = "ElasticCluster"
        mock_load.return_value = self.ct

        with gen_libs.no_std_out():
            self.assertFalse(elastic_db_admin.run_program(self.args,
                                                          self.func_dict))

    @mock.patch("elastic_db_admin.gen_libs.load_module")
    @mock.patch("elastic_db_admin.elastic_class.ElasticCluster")
    @mock.patch("elastic_db_admin.gen_class")
    def test_func_call_multi(self, mock_lock, mock_class, mock_load):

        """Function:  test_func_call_multi

        Description:  Test run_program function with multiple calls to
            function.

        Arguments:

        """

        self.args["-F"] = True
        self.args["-L"] = True

        mock_lock.ProgramLock = elastic_db_admin.gen_class.ProgramLock
        mock_class.return_value = "ElasticCluster"
        mock_load.return_value = self.ct

        self.assertFalse(elastic_db_admin.run_program(self.args,
                                                      self.func_dict))

    @mock.patch("elastic_db_admin.gen_libs.load_module")
    @mock.patch("elastic_db_admin.elastic_class.ElasticCluster")
    @mock.patch("elastic_db_admin.gen_class")
    def test_func_call_one(self, mock_lock, mock_class, mock_load):

        """Function:  test_func_call_one

        Description:  Test run_program function with one call to function.

        Arguments:

        """

        self.args["-F"] = True

        mock_lock.ProgramLock = elastic_db_admin.gen_class.ProgramLock
        mock_class.return_value = "ElasticCluster"
        mock_load.return_value = self.ct

        self.assertFalse(elastic_db_admin.run_program(self.args,
                                                      self.func_dict))

    @mock.patch("elastic_db_admin.gen_libs.load_module")
    @mock.patch("elastic_db_admin.elastic_class.ElasticCluster")
    @mock.patch("elastic_db_admin.gen_class")
    def test_func_call_zero(self, mock_lock, mock_class, mock_load):

        """Function:  test_func_call_zero

        Description:  Test run_program function with zero calls to function.

        Arguments:

        """

        mock_lock.ProgramLock = elastic_db_admin.gen_class.ProgramLock
        mock_class.return_value = "ElasticCluster"
        mock_load.return_value = self.ct

        self.assertFalse(elastic_db_admin.run_program(self.args,
                                                      self.func_dict))


if __name__ == "__main__":
    unittest.main()
