#!/usr/bin/python
# Classification (U)

"""Program:  process_data.py

    Description:  Integration testing of _process_data in elastic_db_admin.py.

    Usage:
        test/integration/elastic_db_admin/process_data.py

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
import elastic_lib.elastic_class as elastic_class
import version

__version__ = version.__version__


class UnitTest(unittest.TestCase):

    """Class:  UnitTest

    Description:  Class which is a representation of a unit testing.

    Methods:
        setUp
        test_incorrect_option
        test_one_option

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        self.cutoff_cpu = 100
        self.cutoff_mem = 100
        self.cutoff_disk = 100

        self.base_dir = "test/integration/elastic_db_admin"
        self.test_path = os.path.join(os.getcwd(), self.base_dir)
        self.config_path = os.path.join(self.test_path, "config")
        self.cfg = gen_libs.load_module("elastic", self.config_path)
        self.user = self.cfg.user if hasattr(self.cfg, "user") else None
        self.japd = self.cfg.japd if hasattr(self.cfg, "japd") else None
        self.ca_cert = self.cfg.ssl_client_ca if hasattr(
            self.cfg, "ssl_client_ca") else None
        self.scheme = self.cfg.scheme if hasattr(
            self.cfg, "scheme") else "https"
        self.els = elastic_class.ElasticSearchStatus(
            self.cfg.host, port=self.cfg.port, user=self.user, japd=self.japd,
            ca_cert=self.ca_cert, scheme=self.scheme)
        self.els.connect()

        self.check_call = {"memory": "chk_mem"}
        self.check_list = ["memory"]
        self.check_list2 = ["incorrect"]

    def test_incorrect_option(self):

        """Function:  test_incorrect_option

        Description:  Test with incorrect option.

        Arguments:

        """

        with gen_libs.no_std_out():
            self.assertEqual(
                elastic_db_admin._process_data(
                    self.check_list2, self.els, check_call=self.check_call,
                    cutoff_cpu=self.cutoff_cpu, cutoff_mem=self.cutoff_mem,
                    cutoff_disk=self.cutoff_disk), {})

    def test_one_option(self):

        """Function:  test_one_option

        Description:  Test with one option.

        Arguments:

        """

        self.assertEqual(
            elastic_db_admin._process_data(
                self.check_list, self.els, check_call=self.check_call,
                cutoff_cpu=self.cutoff_cpu, cutoff_mem=self.cutoff_mem,
                cutoff_disk=self.cutoff_disk), {})


if __name__ == "__main__":
    unittest.main()
