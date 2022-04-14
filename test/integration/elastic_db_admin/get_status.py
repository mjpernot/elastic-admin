#!/usr/bin/python
# Classification (U)

"""Program:  get_status.py

    Description:  Integration testing of get_status in elastic_db_admin.py.

    Usage:
        test/integration/elastic_db_admin/get_status.py

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
import elastic_lib.elastic_class as elastic_class
import version

__version__ = version.__version__


class UnitTest(unittest.TestCase):

    """Class:  UnitTest

    Description:  Class which is a representation of a unit testing.

    Methods:
        setUp
        test_empty_display_list
        test_incorrect_option
        test_one_option
        test_all
        test_no_options
        test_display_all
        test_display_default

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        self.base_dir = "test/integration/elastic_db_admin"
        self.test_path = os.path.join(os.getcwd(), self.base_dir)
        self.tmp_path = os.path.join(self.base_dir, "tmp")
        self.t_file = os.path.join(self.tmp_path, "data_out.txt")
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

# Set the memory threshold to 1

        self.args_array = {"-D": ["all"], "-o": self.t_file, "-z": True}
        self.args_array2 = {"-D": ["memory"], "-o": self.t_file, "-z": True}
        self.args_array3 = {"-D": [], "-o": self.t_file, "-z": True}
        self.args_array4 = {
            "-D": [], "-j": True, "-o": self.t_file, "-z": True}
        self.args_array5 = {
            "-D": ["all"], "-j": True, "-o": self.t_file, "-z": True}
        self.args_array6 = {
            "-D": ["memory"], "-j": True, "-o": self.t_file, "-z": True}
        self.args_array7 = {
            "-D": ["incorrect"], "-j": True, "-o": self.t_file, "-z": True}
        self.args_array8 = {"-D": [], "-o": self.t_file, "-z": True}
        self.status_call = {"memory": "get_mem_status"}

# STOPPED HERE
    @mock.patch("elastic_db_admin.data_out", mock.Mock(return_value=True))
    def test_empty_display_list(self):

        """Function:  test_empty_display_list

        Description:  Test with empty display list.

        Arguments:

        """

        self.assertFalse(
            elastic_db_admin.get_status(
                self.els, status_call=self.status_call,
                args_array=self.args_array8))

    def test_incorrect_option(self):

        """Function:  test_incorrect_option

        Description:  Test with incorrect option.

        Arguments:

        """

        with gen_libs.no_std_out():
            self.assertFalse(
                elastic_db_admin.get_status(
                    self.els, status_call=self.status_call,
                    args_array=self.args_array7))

    @mock.patch("elastic_db_admin.data_out", mock.Mock(return_value=True))
    def test_one_option(self):

        """Function:  test_one_option

        Description:  Test with one option.

        Arguments:

        """

        self.assertFalse(
            elastic_db_admin.get_status(
                self.els, status_call=self.status_call,
                args_array=self.args_array6))

    @mock.patch("elastic_db_admin.data_out", mock.Mock(return_value=True))
    def test_all(self):

        """Function:  test_all

        Description:  Test with all option.

        Arguments:

        """

        self.assertFalse(
            elastic_db_admin.get_status(
                self.els, status_call=self.status_call,
                args_array=self.args_array5))

    @mock.patch("elastic_db_admin.data_out", mock.Mock(return_value=True))
    def test_no_options(self):

        """Function:  test_no_options

        Description:  Test with no options.

        Arguments:

        """

        self.assertFalse(
            elastic_db_admin.get_status(
                self.els, status_call=self.status_call,
                args_array=self.args_array4))

    @mock.patch("elastic_db_admin.data_out", mock.Mock(return_value=True))
    def test_display_all(self):

        """Function:  test_display_all

        Description:  Test with display all option.

        Arguments:

        """

        self.assertFalse(
            elastic_db_admin.get_status(
                self.els, status_call=self.status_call,
                args_array=self.args_array))

    def test_display_default(self):

        """Function:  test_display_default

        Description:  Test with display default option.

        Arguments:

        """

        self.assertFalse(
            elastic_db_admin.get_status(
                self.els, status_call=self.status_call, args_array={}))

    def tearDown(self):

        """Function:  tearDown

        Description:  Clean up of unit testing.

        Arguments:

        """

        if os.path.isfile(self.t_file):
            os.remove(self.t_file)


if __name__ == "__main__":
    unittest.main()
