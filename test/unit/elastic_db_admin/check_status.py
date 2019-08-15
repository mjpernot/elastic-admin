#!/usr/bin/python
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

if sys.version_info < (2, 7):
    import unittest2 as unittest
else:
    import unittest

# Third-party
import mock
import collections

# Local
sys.path.append(os.getcwd())
import elastic_db_admin
import lib.gen_libs as gen_libs
import version

__version__ = version.__version__


class ElasticStatus(object):

    """Class:  ElasticStatus

    Description:  Class representation of the ElasticStatus class.

    Super-Class:  object

    Sub-Classes:

    Methods:
        __init__ -> Initialize configuration environment.
        chk_mem -> Stub holder for ElasticStatus.chk_mem method.
        get_cluster -> Stub holder for ElasticStatus.get_cluster method.
        chk_all -> Stub holder for ElasticStatus.chk_all method.

    """

    def __init__(self, node, port, mem, cpu, disk):

        """Method:  __init__

        Description:  Initialization instance of the class.

        Arguments:
            (input) node -> Node name.
            (input) port -> Port number.
            (input) mem -> Memory cutoff.
            (input) cpu -> Cpu cutoff.
            (input) disk -> Disk cutoff.

        """

        self.node = node
        self.port = port
        self.all_err_msg = None
        self.cluster_err_msg = None
        self.mem_err_msg = None

    def chk_mem(self, json, cutoff_cpu, cutoff_mem, cutoff_disk):

        """Method:  chk_mem

        Description:  Stub holder for ElasticStatus.chk_mem method.

        Arguments:
            (input) json -> True|False - JSON format.
            (input) cutoff_cpu -> CPU cutoff value.
            (input) cutoff_mem -> Memory cutoff value.
            (input) cutoff_disk -> Disk cutoff value.

        """

        return self.mem_err_msg

    def get_cluster(self, json=True):

        """Method:  get_cluster

        Description:  Stub holder for ElasticStatus.get_cluster method.

        Arguments:
            (input) json -> True|False - JSON format.

        """

        return self.cluster_err_msg

    def chk_all(self, json, cutoff_cpu, cutoff_mem, cutoff_disk):

        """Method:  chk_all

        Description:  Stub holder for ElasticStatus.chk_all method.

        Arguments:
            (input) json -> True|False - JSON format.
            (input) cutoff_cpu -> CPU cutoff value.
            (input) cutoff_mem -> Memory cutoff value.
            (input) cutoff_disk -> Disk cutoff value.

        """

        return self.all_err_msg


class ElasticCluster(object):

    """Class:  ElasticCluster

    Description:  Class representation of the ElasticCluster class.

    Super-Class:  object

    Sub-Classes:

    Methods:
        __init__ -> Initialize configuration environment.

    """

    def __init__(self):

        """Method:  __init__

        Description:  Initialization instance of the class.

        Arguments:

        """

        self.node = "nodename"
        self.port = 1234


class UnitTest(unittest.TestCase):

    """Class:  UnitTest

    Description:  Class which is a representation of a unit testing.

    Super-Class:  unittest.TestCase

    Sub-Classes:

    Methods:
        setUp -> Initialization for unit testing.
        test_std_out_option_cfg -> Test std out one option & config settings.
        test_json_one_option_cfg -> Test JSON format option & config settings.
        test_json_one_option_error -> Test JSON format one option with error.
        test_incorrect_option -> Test with incorrect option.
        test_json_one_option -> Test with JSON format with one option.
        test_json_all -> Test with JSON format with all option.
        test_json -> Test with JSON format with no options.
        test_std_out_no_options -> Test with standard out with no options.
        test_std_out_one_option -> Test with standard out with one option.
        test_all_with_error -> Test with all option and with error.
        test_all_no_error -> Test with all option and no errors.
        test_default_no_error -> Test with default option and no errors.

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        self.es = ElasticCluster()
        self.args_array = {"-C": ["all"]}
        self.args_array2 = {"-C": ["memory"]}
        self.args_array3 = {"-C": []}
        self.args_array4 = {"-C": [], "-j": True}
        self.args_array5 = {"-C": ["all"], "-j": True}
        self.args_array6 = {"-C": ["memory"], "-j": True}
        self.args_array7 = {"-C": ["incorrect"], "-j": True}
        self.check_call = {"memory": "chk_mem"}
        self.mem = 90
        self.cpu = 95
        self.disk = 80
        cfg = collections.namedtuple("Cfg",
                                     "cutoff_mem cutoff_cpu cutoff_disk")
        self.cfg = cfg("75", "70", "65")
        cfg2 = collections.namedtuple("Cfg", "test")
        self.cfg2 = cfg2("test")

    @mock.patch("elastic_db_admin.elastic_class.ElasticStatus")
    def test_std_out_option_cfg(self, mock_class):

        """Function:  test_std_out_option_cfg

        Description:  Test with standard out with one option & config settings.

        Arguments:

        """

        mock_class.return_value = ElasticStatus(self.es.node, self.es.port,
                                                self.mem, self.cpu, self.disk)

        self.assertFalse(elastic_db_admin.check_status(self.es,
            check_call=self.check_call, args_array=self.args_array2,
            cfg=self.cfg2))

    @mock.patch("elastic_db_admin.elastic_class.ElasticStatus")
    def test_json_one_option_cfg(self, mock_class):

        """Function:  test_json_one_option_cfg

        Description:  Test with JSON format with option and config settings.

        Arguments:

        """

        mock_class.return_value = ElasticStatus(self.es.node, self.es.port,
                                                self.mem, self.cpu, self.disk)

        self.assertFalse(elastic_db_admin.check_status(self.es,
            check_call=self.check_call, args_array=self.args_array6,
            cfg=self.cfg))

    @mock.patch("elastic_db_admin.elastic_class.ElasticStatus")
    def test_json_one_option_error(self, mock_class):

        """Function:  test_json_one_option_error

        Description:  Test with JSON format with one option with error.

        Arguments:

        """

        es = ElasticStatus(self.es.node, self.es.port, self.mem, self.cpu,
                           self.disk)
        es.mem_err_msg = {"Err": "Error Message"}
        es.cluster_err_msg = {}
        mock_class.return_value = es

        with gen_libs.no_std_out():
            self.assertFalse(elastic_db_admin.check_status(self.es,
                check_call=self.check_call, args_array=self.args_array6,
                cfg=self.cfg2))

    @mock.patch("elastic_db_admin.elastic_class.ElasticStatus")
    def test_incorrect_option(self, mock_class):

        """Function:  test_incorrect_option

        Description:  Test with incorrect option.

        Arguments:

        """

        mock_class.return_value = ElasticStatus(self.es.node, self.es.port,
                                                self.mem, self.cpu, self.disk)

        with gen_libs.no_std_out():
            self.assertFalse(elastic_db_admin.check_status(self.es,
                check_call=self.check_call, args_array=self.args_array7,
                cfg=self.cfg2))

    @mock.patch("elastic_db_admin.elastic_class.ElasticStatus")
    def test_json_one_option(self, mock_class):

        """Function:  test_json_one_option

        Description:  Test with JSON format with one option.

        Arguments:

        """

        mock_class.return_value = ElasticStatus(self.es.node, self.es.port,
                                                self.mem, self.cpu, self.disk)

        self.assertFalse(elastic_db_admin.check_status(self.es,
            check_call=self.check_call, args_array=self.args_array6,
            cfg=self.cfg2))

    @mock.patch("elastic_db_admin.elastic_class.ElasticStatus")
    def test_json_all(self, mock_class):

        """Function:  test_json_all

        Description:  Test with JSON format with all option.

        Arguments:

        """

        mock_class.return_value = ElasticStatus(self.es.node, self.es.port,
                                                self.mem, self.cpu, self.disk)

        self.assertFalse(elastic_db_admin.check_status(self.es,
            check_call=self.check_call, args_array=self.args_array5,
            cfg=self.cfg2))

    @mock.patch("elastic_db_admin.elastic_class.ElasticStatus")
    def test_json(self, mock_class):

        """Function:  test_json

        Description:  Test with JSON format with no options.

        Arguments:

        """

        mock_class.return_value = ElasticStatus(self.es.node, self.es.port,
                                                self.mem, self.cpu, self.disk)

        self.assertFalse(elastic_db_admin.check_status(self.es,
            check_call=self.check_call, args_array=self.args_array4,
            cfg=self.cfg2))

    @mock.patch("elastic_db_admin.elastic_class.ElasticStatus")
    def test_std_out_no_options(self, mock_class):

        """Function:  test_std_out_no_options

        Description:  Test with standard out with no options.

        Arguments:

        """

        mock_class.return_value = ElasticStatus(self.es.node, self.es.port,
                                                self.mem, self.cpu, self.disk)

        self.assertFalse(elastic_db_admin.check_status(self.es,
            check_call=self.check_call, args_array=self.args_array3,
            cfg=self.cfg2))

    @mock.patch("elastic_db_admin.elastic_class.ElasticStatus")
    def test_std_out_one_option(self, mock_class):

        """Function:  test_std_out_one_option

        Description:  Test with standard out with one option.

        Arguments:

        """

        mock_class.return_value = ElasticStatus(self.es.node, self.es.port,
                                                self.mem, self.cpu, self.disk)

        self.assertFalse(elastic_db_admin.check_status(self.es,
            check_call=self.check_call, args_array=self.args_array2,
            cfg=self.cfg2))

    @mock.patch("elastic_db_admin.elastic_class.ElasticStatus")
    def test_all_with_error(self, mock_class):

        """Function:  test_all_with_error

        Description:  Test with all option and with error.

        Arguments:

        """
        es = ElasticStatus(self.es.node, self.es.port, self.mem, self.cpu,
                           self.disk)
        es.all_err_msg = "Error Message"
        mock_class.return_value = es

        with gen_libs.no_std_out():
            self.assertFalse(elastic_db_admin.check_status(self.es,
                check_call=self.check_call, args_array=self.args_array,
                cfg=self.cfg2))

    @mock.patch("elastic_db_admin.elastic_class.ElasticStatus")
    def test_all_no_error(self, mock_class):

        """Function:  test_all_no_error

        Description:  Test with display all option.

        Arguments:

        """

        mock_class.return_value = ElasticStatus(self.es.node, self.es.port,
                                                self.mem, self.cpu, self.disk)

        self.assertFalse(elastic_db_admin.check_status(self.es,
            check_call=self.check_call, args_array=self.args_array,
            cfg=self.cfg2))

    @mock.patch("elastic_db_admin.elastic_class.ElasticStatus")
    def test_default_no_error(self, mock_class):

        """Function:  test_default_no_error

        Description:  Test with default option and no errors.

        Arguments:

        """

        mock_class.return_value = ElasticStatus(self.es.node, self.es.port,
                                                self.mem, self.cpu, self.disk)

        self.assertFalse(elastic_db_admin.check_status(self.es,
            check_call=self.check_call, args_array={}, cfg=self.cfg2))


if __name__ == "__main__":
    unittest.main()
