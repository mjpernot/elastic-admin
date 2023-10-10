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
import unittest

# Local
sys.path.append(os.getcwd())
import elastic_db_admin
import lib.gen_libs as gen_libs
import elastic_lib.elastic_class as elastic_class
import version

__version__ = version.__version__


class ArgParser(object):

    """Class:  ArgParser

    Description:  Class stub holder for gen_class.ArgParser class.

    Methods:
        __init__
        get_val

    """

    def __init__(self):

        """Method:  __init__

        Description:  Class initialization.

        Arguments:

        """

        self.args_array = {"-c": "elastic", "-d": "config"}

    def get_val(self, skey, def_val=None):

        """Method:  get_val

        Description:  Method stub holder for gen_class.ArgParser.get_val.

        Arguments:

        """

        return self.args_array.get(skey, def_val)


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
        self.args = ArgParser()
        self.args2 = ArgParser()
        self.args3 = ArgParser()
        self.args4 = ArgParser()
        self.args5 = ArgParser()
        self.args6 = ArgParser()
        self.args7 = ArgParser()
        self.args8 = ArgParser()
        self.args9 = ArgParser()
        self.args.args_array = {"-D": ["all"], "-o": self.t_file, "-z": True}
        self.args2.args_array = {
            "-D": ["memory"], "-o": self.t_file, "-z": True}
        self.args3.args_array = {"-D": [], "-o": self.t_file, "-z": True}
        self.args4.args_array = {
            "-D": [], "-j": True, "-o": self.t_file, "-z": True}
        self.args5.args_array = {
            "-D": ["all"], "-j": True, "-o": self.t_file, "-z": True}
        self.args6.args_array = {
            "-D": ["memory"], "-j": True, "-o": self.t_file, "-z": True}
        self.args7.args_array = {
            "-D": ["incorrect"], "-j": True, "-o": self.t_file, "-z": True}
        self.args8.args_array8 = {"-D": [], "-o": self.t_file, "-z": True}
        self.args9.args_array = dict()
        self.status_call = {"memory": "get_mem_status"}

    def test_empty_display_list(self):

        """Function:  test_empty_display_list

        Description:  Test with empty display list.

        Arguments:

        """

        elastic_db_admin.get_status(
            self.els, status_call=self.status_call, args=self.args8)

        self.assertTrue(os.path.isfile(self.t_file))

    def test_incorrect_option(self):

        """Function:  test_incorrect_option

        Description:  Test with incorrect option.

        Arguments:

        """

        with gen_libs.no_std_out():
            elastic_db_admin.get_status(
                self.els, status_call=self.status_call, args=self.args7)

        self.assertTrue(os.path.isfile(self.t_file))

    def test_one_option(self):

        """Function:  test_one_option

        Description:  Test with one option.

        Arguments:

        """

        elastic_db_admin.get_status(
            self.els, status_call=self.status_call, args=self.args6)

        self.assertTrue(os.path.isfile(self.t_file))

    def test_all(self):

        """Function:  test_all

        Description:  Test with all option.

        Arguments:

        """

        elastic_db_admin.get_status(
            self.els, status_call=self.status_call, args=self.args5)

        self.assertTrue(os.path.isfile(self.t_file))

    def test_no_options(self):

        """Function:  test_no_options

        Description:  Test with no options.

        Arguments:

        """

        elastic_db_admin.get_status(
            self.els, status_call=self.status_call, args=self.args4)

        self.assertTrue(os.path.isfile(self.t_file))

    def test_display_all(self):

        """Function:  test_display_all

        Description:  Test with display all option.

        Arguments:

        """

        elastic_db_admin.get_status(
            self.els, status_call=self.status_call, args=self.args)

        self.assertTrue(os.path.isfile(self.t_file))

    def test_display_default(self):

        """Function:  test_display_default

        Description:  Test with display default option.

        Arguments:

        """

        with gen_libs.no_std_out():
            self.assertFalse(
                elastic_db_admin.get_status(
                    self.els, status_call=self.status_call, args=self.args))

    def tearDown(self):

        """Function:  tearDown

        Description:  Clean up of unit testing.

        Arguments:

        """

        if os.path.isfile(self.t_file):
            os.remove(self.t_file)


if __name__ == "__main__":
    unittest.main()
