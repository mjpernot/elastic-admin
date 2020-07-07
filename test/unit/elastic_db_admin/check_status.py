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
        __init__ -> Initialize configuration environment.
        chk_mem -> Stub holder for ElasticSearchStatus.chk_mem method.
        get_cluster -> Stub holder for ElasticSearchStatus.get_cluster method.
        chk_all -> Stub holder for ElasticSearchStatus.chk_all method.

    """

    def __init__(self, hosts, port, mem, cpu, disk):

        """Method:  __init__

        Description:  Initialization instance of the class.

        Arguments:
            (input) hosts -> Hosts name.
            (input) port -> Port number.
            (input) mem -> Memory cutoff.
            (input) cpu -> Cpu cutoff.
            (input) disk -> Disk cutoff.

        """

        self.hosts = hosts
        self.port = port
        self.all_err_msg = None
        self.cluster_err_msg = None
        self.mem_err_msg = None
        self.cutoff_cpu = cpu
        self.cutoff_mem = mem
        self.cutoff_disk = disk

    def chk_mem(self, cutoff_cpu, cutoff_mem, cutoff_disk):

        """Method:  chk_mem

        Description:  Stub holder for ElasticSearchStatus.chk_mem method.

        Arguments:
            (input) cutoff_cpu -> CPU cutoff value.
            (input) cutoff_mem -> Memory cutoff value.
            (input) cutoff_disk -> Disk cutoff value.

        """

        self.cutoff_cpu = cutoff_cpu
        self.cutoff_mem = cutoff_mem
        self.cutoff_disk = cutoff_disk

        return self.mem_err_msg

    def get_cluster(self):

        """Method:  get_cluster

        Description:  Stub holder for ElasticSearchStatus.get_cluster method.

        Arguments:

        """

        return self.cluster_err_msg

    def chk_all(self, cutoff_cpu, cutoff_mem, cutoff_disk):

        """Method:  chk_all

        Description:  Stub holder for ElasticSearchStatus.chk_all method.

        Arguments:
            (input) cutoff_cpu -> CPU cutoff value.
            (input) cutoff_mem -> Memory cutoff value.
            (input) cutoff_disk -> Disk cutoff value.

        """

        self.cutoff_cpu = cutoff_cpu
        self.cutoff_mem = cutoff_mem
        self.cutoff_disk = cutoff_disk

        return self.all_err_msg


class ElasticSearch(object):

    """Class:  ElasticSearch

    Description:  Class representation of the ElasticSearch class.

    Methods:
        __init__ -> Initialize configuration environment.

    """

    def __init__(self):

        """Method:  __init__

        Description:  Initialization instance of the class.

        Arguments:

        """

        self.hosts = ["nodename1", "nodename2"]
        self.port = 9200


class UnitTest(unittest.TestCase):

    """Class:  UnitTest

    Description:  Class which is a representation of a unit testing.

    Methods:
        setUp -> Initialization for unit testing.
        test_cutoff_args -> Test passing in cutoff arguments.
        test_one_option_cfg -> Test config settings.
        test_one_option_error -> Test one option with error.
        test_incorrect_option -> Test with incorrect option.
        test_one_option -> Test with one option.
        test_all -> Test with all option.
        test_no_options -> Test with no options.
        test_all_with_error -> Test with all option and with error.
        test_all_no_error -> Test with all option and no errors.
        test_default_no_error -> Test with default option and no errors.

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        self.mem = 90
        self.cpu = 95
        self.disk = 80
        self.els = ElasticSearch()
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

    @mock.patch("elastic_db_admin.elastic_class.ElasticSearchStatus")
    def test_cutoff_args(self, mock_class):

        """Function:  test_cutoff_args

        Description:  Test passing in cutoff arguments.

        Arguments:

        """

        mock_class.return_value = ElasticSearchStatus(
            self.els.hosts, self.els.port, self.mem, self.cpu, self.disk)

        self.assertFalse(
            elastic_db_admin.check_status(
                self.els, check_call=self.check_call,
                args_array=self.args_array8, cfg=self.cfg))

    @mock.patch("elastic_db_admin.elastic_class.ElasticSearchStatus")
    def test_one_option_cfg(self, mock_class):

        """Function:  test_one_option_cfg

        Description:  Test config settings.

        Arguments:

        """

        mock_class.return_value = ElasticSearchStatus(
            self.els.hosts, self.els.port, self.mem, self.cpu, self.disk)

        self.assertFalse(
            elastic_db_admin.check_status(
                self.els, check_call=self.check_call,
                args_array=self.args_array6, cfg=self.cfg))

    @mock.patch("elastic_db_admin.elastic_class.ElasticSearchStatus")
    def test_one_option_error(self, mock_class):

        """Function:  test_one_option_error

        Description:  Test with one option with error.

        Arguments:

        """

        els = ElasticSearchStatus(self.els.hosts, self.els.port, self.mem,
                                  self.cpu, self.disk)
        els.mem_err_msg = {"Err": "Error Message"}
        els.cluster_err_msg = {}
        mock_class.return_value = els

        with gen_libs.no_std_out():
            self.assertFalse(
                elastic_db_admin.check_status(
                    self.els, check_call=self.check_call,
                    args_array=self.args_array6, cfg=self.cfg2))

    @mock.patch("elastic_db_admin.elastic_class.ElasticSearchStatus")
    def test_incorrect_option(self, mock_class):

        """Function:  test_incorrect_option

        Description:  Test with incorrect option.

        Arguments:

        """

        mock_class.return_value = ElasticSearchStatus(
            self.els.hosts, self.els.port, self.mem, self.cpu, self.disk)

        with gen_libs.no_std_out():
            self.assertFalse(
                elastic_db_admin.check_status(
                    self.els, check_call=self.check_call,
                    args_array=self.args_array7, cfg=self.cfg2))

    @mock.patch("elastic_db_admin.elastic_class.ElasticSearchStatus")
    def test_one_option(self, mock_class):

        """Function:  test_one_option

        Description:  Test with one option.

        Arguments:

        """

        mock_class.return_value = ElasticSearchStatus(
            self.els.hosts, self.els.port, self.mem, self.cpu, self.disk)

        self.assertFalse(
            elastic_db_admin.check_status(
                self.els, check_call=self.check_call,
                args_array=self.args_array6, cfg=self.cfg2))

    @mock.patch("elastic_db_admin.elastic_class.ElasticSearchStatus")
    def test_all(self, mock_class):

        """Function:  test_all

        Description:  Test with all option.

        Arguments:

        """

        mock_class.return_value = ElasticSearchStatus(
            self.els.hosts, self.els.port, self.mem, self.cpu, self.disk)

        self.assertFalse(
            elastic_db_admin.check_status(
                self.els, check_call=self.check_call,
                args_array=self.args_array5, cfg=self.cfg2))

    @mock.patch("elastic_db_admin.elastic_class.ElasticSearchStatus")
    def test_no_options(self, mock_class):

        """Function:  test_no_options

        Description:  Test with no options.

        Arguments:

        """

        mock_class.return_value = ElasticSearchStatus(
            self.els.hosts, self.els.port, self.mem, self.cpu, self.disk)

        self.assertFalse(
            elastic_db_admin.check_status(
                self.els, check_call=self.check_call,
                args_array=self.args_array4, cfg=self.cfg2))

    @mock.patch("elastic_db_admin.elastic_class.ElasticSearchStatus")
    def test_all_with_error(self, mock_class):

        """Function:  test_all_with_error

        Description:  Test with all option and with error.

        Arguments:

        """
        els = ElasticSearchStatus(self.els.hosts, self.els.port, self.mem,
                                  self.cpu, self.disk)
        els.all_err_msg = "Error Message"
        mock_class.return_value = els

        with gen_libs.no_std_out():
            self.assertFalse(
                elastic_db_admin.check_status(
                    self.els, check_call=self.check_call,
                    args_array=self.args_array, cfg=self.cfg2))

    @mock.patch("elastic_db_admin.elastic_class.ElasticSearchStatus")
    def test_all_no_error(self, mock_class):

        """Function:  test_all_no_error

        Description:  Test with display all option.

        Arguments:

        """

        mock_class.return_value = ElasticSearchStatus(
            self.els.hosts, self.els.port, self.mem, self.cpu, self.disk)

        self.assertFalse(
            elastic_db_admin.check_status(
                self.els, check_call=self.check_call,
                args_array=self.args_array, cfg=self.cfg2))

    @mock.patch("elastic_db_admin.elastic_class.ElasticSearchStatus")
    def test_default_no_error(self, mock_class):

        """Function:  test_default_no_error

        Description:  Test with default option and no errors.

        Arguments:

        """

        mock_class.return_value = ElasticSearchStatus(
            self.els.hosts, self.els.port, self.mem, self.cpu, self.disk)

        self.assertFalse(
            elastic_db_admin.check_status(
                self.els, check_call=self.check_call, args_array={},
                cfg=self.cfg2))


if __name__ == "__main__":
    unittest.main()
