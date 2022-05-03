#!/usr/bin/python
# Classification (U)

"""Program:  check_status.py

    Description:  Integration testing of check_status in elastic_db_admin.py.

    Usage:
        test/integration/elastic_db_admin/check_status.py

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
        test_cutoff_args
        test_one_option_cfg
        test_incorrect_option
        test_one_option
        test_all
        test_no_options
        test_default_no_error
        tearDown

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

        self.mem = 100
        self.mem2 = 1
        self.cpu = 100
        self.disk = 100
        self.args_array = {
            "-C": ["all"], "-o": self.t_file, "-z": True,  "-m": self.mem,
            "-u": self.cpu, "-p": self.disk}
        self.args_array2 = {"-C": ["memory"], "-o": self.t_file, "-z": True}
        self.args_array3 = {"-C": [], "-o": self.t_file, "-z": True}
        self.args_array4 = {
            "-C": [], "-j": True, "-o": self.t_file, "-z": True}
        self.args_array5 = {
            "-C": ["all"], "-j": True, "-o": self.t_file, "-z": True}
        self.args_array6 = {
            "-C": ["memory"], "-j": True, "-m": self.mem2, "-o": self.t_file,
            "-z": True}
        self.args_array7 = {
            "-C": ["incorrect"], "-j": True, "-o": self.t_file, "-z": True}
        self.args_array8 = {
            "-C": ["memory"], "-j": True, "-m": self.mem, "-u": self.cpu,
            "-p": self.disk, "-o": self.t_file, "-z": True}
        self.check_call = {"memory": "chk_mem"}

    def test_cutoff_args(self):

        """Function:  test_cutoff_args

        Description:  Test passing in cutoff arguments.

        Arguments:

        """

        elastic_db_admin.check_status(
            self.els, check_call=self.check_call, args_array=self.args_array8,
            cfg=self.cfg)

        self.assertFalse(os.path.isfile(self.t_file))

    def test_one_option_cfg(self):

        """Function:  test_one_option_cfg

        Description:  Test config settings.

        Arguments:

        """

        elastic_db_admin.check_status(
            self.els, check_call=self.check_call,
            args_array=self.args_array6, cfg=self.cfg)

        self.assertTrue(os.path.isfile(self.t_file))

    def test_incorrect_option(self):

        """Function:  test_incorrect_option

        Description:  Test with incorrect option.

        Arguments:

        """

        with gen_libs.no_std_out():
            elastic_db_admin.check_status(
                self.els, check_call=self.check_call,
                args_array=self.args_array7, cfg=self.cfg)

        self.assertFalse(os.path.isfile(self.t_file))

    def test_one_option(self):

        """Function:  test_one_option

        Description:  Test with one option.

        Arguments:

        """

        elastic_db_admin.check_status(
            self.els, check_call=self.check_call,
            args_array=self.args_array6, cfg=self.cfg)

        self.assertTrue(os.path.isfile(self.t_file))

    def test_all(self):

        """Function:  test_all

        Description:  Test with all option.

        Arguments:

        """

        elastic_db_admin.check_status(
            self.els, check_call=self.check_call, args_array=self.args_array5,
            cfg=self.cfg)

        if os.path.isfile(self.t_file):
            self.assertTrue(os.path.isfile(self.t_file))

        else:
            self.assertFalse(os.path.isfile(self.t_file))

    def test_no_options(self):

        """Function:  test_no_options

        Description:  Test with no options.

        Arguments:

        """

        elastic_db_admin.check_status(
            self.els, check_call=self.check_call, args_array=self.args_array4,
            cfg=self.cfg)

        if os.path.isfile(self.t_file):
            self.assertTrue(os.path.isfile(self.t_file))

        else:
            self.assertFalse(os.path.isfile(self.t_file))

    def test_all_error(self):

        """Function:  test_all_error

        Description:  Test with display all option.

        Arguments:

        """

        elastic_db_admin.check_status(
            self.els, check_call=self.check_call, args_array=self.args_array,
            cfg=self.cfg)

        if os.path.isfile(self.t_file):
            self.assertTrue(os.path.isfile(self.t_file))

        else:
            self.assertFalse(os.path.isfile(self.t_file))

    def tearDown(self):

        """Function:  tearDown

        Description:  Clean up of unit testing.

        Arguments:

        """

        if os.path.isfile(self.t_file):
            os.remove(self.t_file)


if __name__ == "__main__":
    unittest.main()
