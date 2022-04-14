#!/usr/bin/python
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
        self.args_array = {}
        self.args_array2 = {"-o": self.t_file, "-z": True}
        self.args_array3 = {"-o": self.t_file, "-a": True, "-z": True}
        self.args_array4 = {"-o": self.t_file, "-j": True, "-z": True}
        self.args_array5 = {"-z": True}
        self.args_array6 = {"-j": True}

    def test_std_out_json(self):

        """Function:  test_std_out_json

        Description:  Test with standard out with json mode.

        Arguments:

        """

        with gen_libs.no_std_out():
            self.assertFalse(
                elastic_db_admin.data_out(self.data, self.args_array6))

    def test_std_out_suppressed(self):

        """Function:  test_std_out_suppressed

        Description:  Test with standard out suppressed.

        Arguments:

        """

        self.assertFalse(
            elastic_db_admin.data_out(self.data, self.args_array5))

    def test_std_out(self):

        """Function:  test_std_out

        Description:  Test with standard out.

        Arguments:

        """

        with gen_libs.no_std_out():
            self.assertFalse(
                elastic_db_admin.data_out(self.data, self.args_array))

    def test_file_json(self):

        """Function:  test_file_json

        Description:  Test with file option with json option.

        Arguments:

        """

        elastic_db_admin.data_out(self.data, self.args_array4)

        self.assertTrue(os.path.isfile(self.t_file))

    def test_file_append(self):

        """Function:  test_file_append

        Description:  Test with file option with append option.

        Arguments:

        """

        elastic_db_admin.data_out(self.data, self.args_array3)

        self.assertTrue(os.path.isfile(self.t_file))

    def test_file(self):

        """Function:  test_file

        Description:  Test with file option.

        Arguments:

        """

        elastic_db_admin.data_out(self.data, self.args_array2)

        self.assertTrue(os.path.isfile(self.t_file))

    def test_no_data(self):

        """Function:  test_no_data

        Description:  Test with no data output.

        Arguments:

        """

        self.assertFalse(
            elastic_db_admin.data_out(self.data, self.args_array5))

    def tearDown(self):

        """Function:  tearDown

        Description:  Clean up of unit testing.

        Arguments:

        """

        if os.path.isfile(self.t_file):
            os.remove(self.t_file)


if __name__ == "__main__":
    unittest.main()
