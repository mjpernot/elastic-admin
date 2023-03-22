# Classification (U)

"""Program:  check_status.py

    Description:  Unit testing of check_status in elastic_db_admin.py.

    Usage:
        test/unit/elastic_db_admin/check_status.py

    Arguments:

"""

# Libraries and Global Variables

# Standard
import sys
import os
import unittest
import collections
import mock

# Local
sys.path.append(os.getcwd())
import elastic_db_admin
import lib.gen_libs as gen_libs
import version

__version__ = version.__version__


class ElasticSearchStatus(object):

    """Class:  ElasticSearchStatus

    Description:  Class representation of the ElasticSearchStatus class.

    Methods:
        __init__
        chk_mem
        get_nodes
        get_cluster
        chk_all

    """

    def __init__(self):

        """Method:  __init__

        Description:  Initialization instance of the class.

        Arguments:

        """

        self.hosts = ["hosts"]
        self.port = 9200
        self.all_err_msg = None
        self.cluster_err_msg = None
        self.mem_err_msg = None
        self.cutoff_cpu = 95
        self.cutoff_mem = 90
        self.cutoff_disk = 75

    def chk_mem(self, cutoff_cpu, cutoff_mem, cutoff_disk):

        """Method:  chk_mem

        Description:  Stub holder for ElasticSearchStatus.chk_mem method.

        Arguments:

        """

        self.cutoff_cpu = cutoff_cpu
        self.cutoff_mem = cutoff_mem
        self.cutoff_disk = cutoff_disk

        return self.mem_err_msg

    def get_nodes(self):

        """Method:  get_nodes

        Description:  Stub holder for ElasticSearchStatus.get_nodes method.

        Arguments:

        """

        return {"node": "node_name"}

    def get_cluster(self):

        """Method:  get_cluster

        Description:  Stub holder for ElasticSearchStatus.get_cluster method.

        Arguments:

        """

        return {"Cluster": "cluster_name"}

    def chk_all(self, cutoff_cpu, cutoff_mem, cutoff_disk):

        """Method:  chk_all

        Description:  Stub holder for ElasticSearchStatus.chk_all method.

        Arguments:

        """

        self.cutoff_cpu = cutoff_cpu
        self.cutoff_mem = cutoff_mem
        self.cutoff_disk = cutoff_disk

        return self.all_err_msg


class UnitTest(unittest.TestCase):

    """Class:  UnitTest

    Description:  Class which is a representation of a unit testing.

    Methods:
        setUp
        test_cutoff_args
        test_one_option_cfg
        test_one_option_error
        test_incorrect_option
        test_one_option
        test_all
        test_no_options
        test_all_with_error
        test_all_no_error
        test_default_no_error

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        self.mem = 90
        self.cpu = 95
        self.disk = 80
        self.els = ElasticSearchStatus()
        self.args_array = {"-C": ["all"]}
        self.args_array2 = {"-C": ["memory"]}
        self.args_array3 = {"-C": []}
        self.args_array4 = {"-C": [], "-j": True}
        self.args_array5 = {"-C": ["all"], "-j": True}
        self.args_array6 = {"-C": ["memory"], "-j": True}
        self.args_array7 = {"-C": ["incorrect"], "-j": True}
        self.args_array8 = {"-C": ["memory"], "-j": True, "-m": self.mem,
                            "-u": self.cpu, "-p": self.disk}
        self.check_call = {"memory": "chk_mem"}
        cfg = collections.namedtuple("Cfg",
                                     "cutoff_mem cutoff_cpu cutoff_disk")
        self.cfg = cfg("75", "70", "65")
        cfg2 = collections.namedtuple("Cfg", "test")
        self.cfg2 = cfg2("test")

    def test_cutoff_args(self):

        """Function:  test_cutoff_args

        Description:  Test passing in cutoff arguments.

        Arguments:

        """

        self.assertFalse(
            elastic_db_admin.check_status(
                self.els, check_call=self.check_call,
                args_array=self.args_array8, cfg=self.cfg))

    def test_one_option_cfg(self):

        """Function:  test_one_option_cfg

        Description:  Test config settings.

        Arguments:

        """

        self.assertFalse(
            elastic_db_admin.check_status(
                self.els, check_call=self.check_call,
                args_array=self.args_array6, cfg=self.cfg))

    @mock.patch("elastic_db_admin.data_out", mock.Mock(return_value=True))
    def test_one_option_error(self):

        """Function:  test_one_option_error

        Description:  Test with one option with error.

        Arguments:

        """

        self.els.mem_err_msg = {"Err": "Error Message"}
        self.els.cluster_err_msg = {}

        self.assertFalse(
            elastic_db_admin.check_status(
                self.els, check_call=self.check_call,
                args_array=self.args_array6, cfg=self.cfg2))

    @mock.patch("elastic_db_admin.data_out", mock.Mock(return_value=True))
    def test_incorrect_option(self):

        """Function:  test_incorrect_option

        Description:  Test with incorrect option.

        Arguments:

        """

        with gen_libs.no_std_out():
            self.assertFalse(
                elastic_db_admin.check_status(
                    self.els, check_call=self.check_call,
                    args_array=self.args_array7, cfg=self.cfg2))

    def test_one_option(self):

        """Function:  test_one_option

        Description:  Test with one option.

        Arguments:

        """

        self.assertFalse(
            elastic_db_admin.check_status(
                self.els, check_call=self.check_call,
                args_array=self.args_array6, cfg=self.cfg2))

    def test_all(self):

        """Function:  test_all

        Description:  Test with all option.

        Arguments:

        """

        self.assertFalse(
            elastic_db_admin.check_status(
                self.els, check_call=self.check_call,
                args_array=self.args_array5, cfg=self.cfg2))

    def test_no_options(self):

        """Function:  test_no_options

        Description:  Test with no options.

        Arguments:

        """

        self.assertFalse(
            elastic_db_admin.check_status(
                self.els, check_call=self.check_call,
                args_array=self.args_array4, cfg=self.cfg2))

    @mock.patch("elastic_db_admin.data_out", mock.Mock(return_value=True))
    def test_all_with_error(self):

        """Function:  test_all_with_error

        Description:  Test with all option and with error.

        Arguments:

        """

        self.els.all_err_msg = {"Key": "Error Message"}

        self.assertFalse(
            elastic_db_admin.check_status(
                self.els, check_call=self.check_call,
                args_array=self.args_array, cfg=self.cfg2))

    def test_all_no_error(self):

        """Function:  test_all_no_error

        Description:  Test with display all option.

        Arguments:

        """

        self.assertFalse(
            elastic_db_admin.check_status(
                self.els, check_call=self.check_call,
                args_array=self.args_array, cfg=self.cfg2))

    def test_default_no_error(self):

        """Function:  test_default_no_error

        Description:  Test with default option and no errors.

        Arguments:

        """

        self.assertFalse(
            elastic_db_admin.check_status(
                self.els, check_call=self.check_call, args_array={},
                cfg=self.cfg2))


if __name__ == "__main__":
    unittest.main()
