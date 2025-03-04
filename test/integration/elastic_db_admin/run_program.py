# Classification (U)

"""Program:  run_program.py

    Description:  Integration testing of run_program in elastic_db_admin.py.

    Usage:
        test/integration/elastic_db_admin/run_program.py

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
import version                                  # pylint:disable=E0401,C0413

__version__ = version.__version__


def list_master(els, **kwargs):                         # pylint:disable=W0613

    """Function:  list_master

    Description:  This is a function stub for elastic_db_admin.list_master.

    Arguments:

    """


def failed_dumps(els, **kwargs):                        # pylint:disable=W0613

    """Function:  failed_dumps

    Description:  This is a function stub for elastic_db_admin.failed_dumps.

    Arguments:

    """


def list_dumps(els, **kwargs):                          # pylint:disable=W0613

    """Function:  list_repos

    Description:  This is a function stub for elastic_db_admin.list_dumps.

    Arguments:

    """


class UnitTest(unittest.TestCase):

    """Class:  UnitTest

    Description:  Class which is a representation of a unit testing.

    Methods:
        setUp
        test_is_connected
        test_func_call_multi
        test_func_call_one
        test_func_call_zero
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
        self.args = {
            "-c": "elastic", "-d": self.config_path, "-M": True,
            "-o": self.t_file, "-z": True}
        self.func_names = {
            "-F": failed_dumps, "-L": list_dumps, "-M": list_master}

    def test_is_connected(self):

        """Function:  test_is_connected

        Description:  Test with successful connection.

        Arguments:

        """

        self.args["-F"] = True
        elastic_db_admin.run_program(self.args, self.func_names)

        self.assertFalse(os.path.isfile(self.t_file))

    def test_func_call_multi(self):

        """Function:  test_func_call_multi

        Description:  Test run_program function with multiple calls to
            function.

        Arguments:

        """

        self.args["-F"] = True
        self.args["-L"] = True
        elastic_db_admin.run_program(self.args, self.func_names)

        self.assertFalse(os.path.isfile(self.t_file))

    def test_func_call_one(self):

        """Function:  test_func_call_one

        Description:  Test run_program function with one call to function.

        Arguments:

        """

        self.args["-F"] = True
        elastic_db_admin.run_program(self.args, self.func_names)

        self.assertFalse(os.path.isfile(self.t_file))

    def test_func_call_zero(self):

        """Function:  test_func_call_zero

        Description:  Test run_program function with zero calls to function.

        Arguments:

        """

        elastic_db_admin.run_program(self.args, self.func_names)

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
