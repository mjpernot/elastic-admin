# Classification (U)

"""Program:  data_out.py

    Description:  Integration testing of data_out in elastic_db_admin.py.

    Usage:
        test/integration/elastic_db_admin/data_out.py

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
import version

__version__ = version.__version__


class ArgParser(object):

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

        return True if arg in self.args_array else False

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
        test_std_out_json
        test_std_out_suppressed
        test_std_out
        test_file_json
        test_file_append
        test_file
        test_no_data
        tearDown

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        self.base_dir = "test/integration/elastic_db_admin/tmp"
        self.tmp_path = os.path.join(os.getcwd(), self.base_dir)
        self.t_file = os.path.join(self.tmp_path, "data_out.txt")
        self.data = {"key1": "value1", "key2": "value2"}
        self.args = ArgParser()
        self.args2 = ArgParser()
        self.args3 = ArgParser()
        self.args4 = ArgParser()
        self.args5 = ArgParser()
        self.args6 = ArgParser()
        self.args.args_array = dict()
        self.args2.args_array = {"-o": self.t_file, "-z": True}
        self.args3.args_array = {"-o": self.t_file, "-a": True, "-z": True}
        self.args4.args_array = {"-o": self.t_file, "-j": True, "-z": True}
        self.args5.args_array = {"-z": True}
        self.args6.args_array = {"-j": True}

    def test_std_out_json(self):

        """Function:  test_std_out_json

        Description:  Test with standard out with json mode.

        Arguments:

        """

        with gen_libs.no_std_out():
            self.assertFalse(elastic_db_admin.data_out(self.data, self.args6))

    def test_std_out_suppressed(self):

        """Function:  test_std_out_suppressed

        Description:  Test with standard out suppressed.

        Arguments:

        """

        self.assertFalse(elastic_db_admin.data_out(self.data, self.args5))

    def test_std_out(self):

        """Function:  test_std_out

        Description:  Test with standard out.

        Arguments:

        """

        with gen_libs.no_std_out():
            self.assertFalse(elastic_db_admin.data_out(self.data, self.args))

    def test_file_json(self):

        """Function:  test_file_json

        Description:  Test with file option with json option.

        Arguments:

        """

        elastic_db_admin.data_out(self.data, self.args4)

        self.assertTrue(os.path.isfile(self.t_file))

    def test_file_append(self):

        """Function:  test_file_append

        Description:  Test with file option with append option.

        Arguments:

        """

        elastic_db_admin.data_out(self.data, self.args3)

        self.assertTrue(os.path.isfile(self.t_file))

    def test_file(self):

        """Function:  test_file

        Description:  Test with file option.

        Arguments:

        """

        elastic_db_admin.data_out(self.data, self.args2)

        self.assertTrue(os.path.isfile(self.t_file))

    def test_no_data(self):

        """Function:  test_no_data

        Description:  Test with no data output.

        Arguments:

        """

        self.assertFalse(elastic_db_admin.data_out(self.data, self.args5))

    def tearDown(self):

        """Function:  tearDown

        Description:  Clean up of unit testing.

        Arguments:

        """

        if os.path.isfile(self.t_file):
            os.remove(self.t_file)


if __name__ == "__main__":
    unittest.main()
