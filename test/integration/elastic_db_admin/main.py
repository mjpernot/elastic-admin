#!/usr/bin/python
# Classification (U)

"""Program:  main.py

    Description:  Integration testing of main in elastic_db_admin.py.

    Usage:
        test/integration/elastic_db_admin/main.py

    Arguments:
        None

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

# Version
__version__ = version.__version__


class UnitTest(unittest.TestCase):

    """Class:  UnitTest

    Description:  Class which is a representation of a unit testing.

    Methods:
        setUp
        test_help_func2
        test_help_func
        test_arg_require
        test_arg_dir_chk_crt
        test_arg_cond_req
        test_run_program
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
        self.config_path2 = os.path.join(self.test_path, "config2")

        self.argv_list = [
            "elastic_db_admin.py", "-c", "elastic", "-d", self.config_path,
            "-R"]
        self.argv_list2 = [
            "elastic_db_admin.py", "-c", "elastic", "-d", self.config_path,
            "-D", "-o", self.t_file, "-z"]

    def test_help_func2(self):

        """Function:  test_help_func2

        Description:  Test with help_func for -v option.

        Arguments:

        """

        cmdline = gen_libs.get_inst(sys)
        self.argv_list.append("-v")
        cmdline.argv = self.argv_list

        with gen_libs.no_std_out():
            self.assertFalse(elastic_db_admin.main())

    def test_help_func(self):

        """Function:  test_help_func

        Description:  Test with help_func for -h option.

        Arguments:

        """

        cmdline = gen_libs.get_inst(sys)
        self.argv_list.append("-h")
        cmdline.argv = self.argv_list

        with gen_libs.no_std_out():
            self.assertFalse(elastic_db_admin.main())

    def test_arg_require(self):

        """Function:  test_arg_require

        Description:  Test with arg_require missing option.

        Arguments:

        """

        cmdline = gen_libs.get_inst(sys)
        self.argv_list.remove("-c")
        self.argv_list.remove("elastic")
        cmdline.argv = self.argv_list

        with gen_libs.no_std_out():
            self.assertFalse(elastic_db_admin.main())

    def test_arg_dir_chk_crt(self):

        """Function:  test_arg_dir_chk_crt

        Description:  Test with arg_dir_chk_crt with missing directory.

        Arguments:

        """

        cmdline = gen_libs.get_inst(sys)
        self.argv_list.remove("-d")
        self.argv_list.remove(self.config_path)
        self.argv_list.append("-d")
        self.argv_list.append(self.config_path2)
        cmdline.argv = self.argv_list

        with gen_libs.no_std_out():
            self.assertFalse(elastic_db_admin.main())

    def test_arg_cond_req(self):

        """Function:  test_arg_cond_req

        Description:  Test with arg_cond_req missing conditional argument.

        Arguments:

        """

        cmdline = gen_libs.get_inst(sys)
        self.argv_list.append("-s")
        self.argv_list.append("subject_line")
        cmdline.argv = self.argv_list

        with gen_libs.no_std_out():
            self.assertFalse(elastic_db_admin.main())

    def test_run_program(self):

        """Function:  test_run_program

        Description:  Test run_program function.

        Arguments:

        """

        cmdline = gen_libs.get_inst(sys)
        cmdline.argv = self.argv_list2
        elastic_db_admin.main()

        self.assertTrue(os.path.isfile(self.t_file))

    def tearDown(self):

        """Function:  tearDown

        Description:  Clean up of unit testing.

        Arguments:

        """

        if os.path.isfile(self.t_file):
            os.remove(self.t_file)


if __name__ == "__main__":
    unittest.main()
