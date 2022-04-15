#!/usr/bin/python
# Classification (U)

"""Program:  list_dumps.py

    Description:  Integration testing of list_dumps in elastic_db_admin.py.

    Usage:
        test/integration/elastic_db_admin/list_dumps.py

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
        test_repo_incorrect
        test_no_repo
        test_repo

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

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
        self.args_array = {"-L": "WhatNameToUse"}
        self.args_array2 = {"-L": "WhatNameToUse3"}

    def test_repo_incorrect(self):

        """Function:  test_repo_incorrect

        Description:  Test with incorrect repo name.

        Arguments:

        """

        with gen_libs.no_std_out():
            self.assertFalse(
                elastic_db_admin.list_dumps(
                    self.els, args_array=self.args_array2))

    def test_no_repo(self):

        """Function:  test_no_repo

        Description:  Test with no repo name passed.

        Arguments:

        """

        with gen_libs.no_std_out():
            self.assertFalse(
                elastic_db_admin.list_dumps(self.els, args_array={}))

    def test_repo(self):

        """Function:  test_repo

        Description:  Test with repo name passed.

        Arguments:

        """

        with gen_libs.no_std_out():
            self.assertFalse(
                elastic_db_admin.list_dumps(
                    self.els, args_array=self.args_array))


if __name__ == "__main__":
    unittest.main()
