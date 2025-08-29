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


class ArgParser():

    """Class:  ArgParser

    Description:  Class stub holder for gen_class.ArgParser class.

    Methods:
        __init__
        get_args_keys
        get_val

    """

    def __init__(self):

        """Method:  __init__

        Description:  Class initialization.

        Arguments:

        """

        self.args_array = {}

    def get_args_keys(self):

        """Method:  get_args_keys

        Description:  Method stub holder for gen_class.ArgParser.get_args_keys.

        Arguments:

        """

        return list(self.args_array.keys())

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
        self.func_names = {
            "-F": failed_dumps, "-L": list_dumps, "-M": list_master}
        self.args = ArgParser()

    def test_is_connected(self):

        """Function:  test_is_connected

        Description:  Test with successful connection.

        Arguments:

        """

        self.args.args_array = {
            "-c": "elastic", "-d": self.config_path, "-M": True,
            "-o": self.t_file, "-z": True, "-F": True}

        elastic_db_admin.run_program(self.args, self.func_names)

        self.assertFalse(os.path.isfile(self.t_file))

    def test_func_call_multi(self):

        """Function:  test_func_call_multi

        Description:  Test run_program function with multiple calls to
            function.

        Arguments:

        """

        self.args.args_array = {
            "-c": "elastic", "-d": self.config_path, "-M": True,
            "-o": self.t_file, "-z": True, "-F": True, "-L": True}

        elastic_db_admin.run_program(self.args, self.func_names)

        self.assertFalse(os.path.isfile(self.t_file))

    def test_func_call_one(self):

        """Function:  test_func_call_one

        Description:  Test run_program function with one call to function.

        Arguments:

        """

        self.args.args_array = {
            "-c": "elastic", "-d": self.config_path, "-M": True,
            "-o": self.t_file, "-z": True, "-F": True}

        elastic_db_admin.run_program(self.args, self.func_names)

        self.assertFalse(os.path.isfile(self.t_file))

    def test_func_call_zero(self):

        """Function:  test_func_call_zero

        Description:  Test run_program function with zero calls to function.

        Arguments:

        """

        self.args.args_array = {
            "-c": "elastic", "-d": self.config_path, "-M": True,
            "-o": self.t_file, "-z": True}

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
