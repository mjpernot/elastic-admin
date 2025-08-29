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
import elastic_db_admin                         # pylint:disable=E0401,C0413
import elastic_lib.elastic_class as elcs    # pylint:disable=E0401,C0413,R0402
import lib.gen_libs as gen_libs             # pylint:disable=E0401,C0413,R0402
import lib.gen_class as gen_class           # pylint:disable=E0401,C0413,R0402
import version                                  # pylint:disable=E0401,C0413

__version__ = version.__version__


class ArgParser():

    """Class:  ArgParser

    Description:  Class stub holder for gen_class.ArgParser class.

    Methods:
        __init__
        arg_exist
        get_val

    """

    def __init__(self):

        """Method:  __init__

        Description:  Class initialization.

        Arguments:

        """

        self.args_array = {"-c": "elastic", "-d": "config"}

    def arg_exist(self, arg):

        """Method:  arg_exist

        Description:  Method stub holder for gen_class.ArgParser.arg_exist.

        Arguments:

        """

        return arg in self.args_array

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
        test_incorrect_option
        test_one_option
        test_no_options
        test_file
        test_display_suppress
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
        self.els = elcs.ElasticSearchStatus(
            self.cfg.host, user=self.user, japd=self.japd,
            ca_cert=self.ca_cert, scheme=self.scheme)
        self.els.connect()
        self.args = ArgParser()
        self.dtg = gen_class.TimeFormat()
        self.dtg.create_time()

    def test_incorrect_option(self):

        """Function:  test_incorrect_option

        Description:  Test with incorrect option.

        Arguments:

        """

        self.args.args_array = {"-D": ["incorrect"]}

        with gen_libs.no_std_out():
            self.assertFalse(elastic_db_admin.get_status(
                self.els, args=self.args, dtg=self.dtg))

    def test_one_option(self):

        """Function:  test_one_option

        Description:  Test with one option.

        Arguments:

        """

        self.args.args_array = {"-D": ["memory"], "-z": True}

        self.assertFalse(
            elastic_db_admin.get_status(
                self.els, args=self.args, dtg=self.dtg))

    def test_no_options(self):

        """Function:  test_no_options

        Description:  Test with no options.

        Arguments:

        """

        self.args.args_array = {"-D": [], "-z": True}

        self.assertFalse(
            elastic_db_admin.get_status(
                self.els, args=self.args, dtg=self.dtg))

    def test_file(self):

        """Function:  test_file

        Description:  Test with file option.

        Arguments:

        """

        self.args.args_array = {"-D": ["all"], "-o": self.t_file, "-z": True}

        elastic_db_admin.get_status(self.els, args=self.args, dtg=self.dtg)

        self.assertTrue(os.path.isfile(self.t_file))

    def test_display_suppress(self):

        """Function:  test_display_suppress

        Description:  Test with display default option.

        Arguments:

        """

        self.args.args_array = {"-D": ["all"], "-z": True}

        self.assertFalse(
            elastic_db_admin.get_status(
                self.els, args=self.args, dtg=self.dtg))

    def test_display_default(self):

        """Function:  test_display_default

        Description:  Test with display default option.

        Arguments:

        """

        self.args.args_array = {"-D": ["all"]}

        with gen_libs.no_std_out():
            self.assertFalse(
                elastic_db_admin.get_status(
                    self.els, args=self.args, dtg=self.dtg))

    def tearDown(self):

        """Function:  tearDown

        Description:  Clean up of unit testing.

        Arguments:

        """

        if os.path.isfile(self.t_file):
            os.remove(self.t_file)


if __name__ == "__main__":
    unittest.main()
