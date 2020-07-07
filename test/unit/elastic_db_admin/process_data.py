#!/usr/bin/python
# Classification (U)

"""Program:  process_data.py

    Description:  Unit testing of _process_data in elastic_db_admin.py.

    Usage:
        test/unit/elastic_db_admin/process_data.py

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


class UnitTest(unittest.TestCase):

    """Class:  UnitTest

    Description:  Class which is a representation of a unit testing.

    Methods:
        setUp -> Initialization for unit testing.
        test_one_option_error -> Test with one option with error.
        test_incorrect_option -> Test with incorrect option.
        test_one_option -> Test with one option.

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        self.cutoff_cpu = 90
        self.cutoff_mem = 95
        self.cutoff_disk = 80
        self.els = ElasticSearchStatus("nodename", 1234, self.cutoff_cpu,
                                       self.cutoff_mem, self.cutoff_disk)
        self.check_call = {"memory": "chk_mem"}
        self.check_list = ["memory"]
        self.check_list2 = ["incorrect"]
        self.err_flag = False
        self.err_msg = {}
        self.err_msg2 = ""
        self.err_msg3 = {"Error": True}

    def test_one_option_error(self):

        """Function:  test_one_option_error

        Description:  Test with one option with error.

        Arguments:

        """

        self.els.mem_err_msg = {"Err": "Error Message"}
        self.els.cluster_err_msg = {}

        self.assertEqual(
            elastic_db_admin._process_data(
                self.check_list, self.err_flag, self.err_msg3, self.els,
                check_call=self.check_call, cutoff_cpu=self.cutoff_cpu,
                cutoff_mem=self.cutoff_mem, cutoff_disk=self.cutoff_disk),
            (True, {"Err": "Error Message", "Error": True}))

    def test_incorrect_option(self):

        """Function:  test_incorrect_option

        Description:  Test with incorrect option.

        Arguments:

        """

        with gen_libs.no_std_out():
            self.assertEqual(
                elastic_db_admin._process_data(
                    self.check_list2, self.err_flag, self.err_msg, self.els,
                    check_call=self.check_call, cutoff_cpu=self.cutoff_cpu,
                    cutoff_mem=self.cutoff_mem, cutoff_disk=self.cutoff_disk),
                (False, {}))

    def test_one_option(self):

        """Function:  test_one_option

        Description:  Test with one option.

        Arguments:

        """

        self.assertEqual(
            elastic_db_admin._process_data(
                self.check_list, self.err_flag, self.err_msg, self.els,
                check_call=self.check_call, cutoff_cpu=self.cutoff_cpu,
                cutoff_mem=self.cutoff_mem, cutoff_disk=self.cutoff_disk),
            (False, {}))


if __name__ == "__main__":
    unittest.main()
