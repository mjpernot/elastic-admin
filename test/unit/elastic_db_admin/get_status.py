# Classification (U)

"""Program:  get_status.py

    Description:  Unit testing of get_status in elastic_db_admin.py.

    Usage:
        test/unit/elastic_db_admin/get_status.py

    Arguments:

"""

# Libraries and Global Variables

# Standard
import sys
import os
import unittest
import mock

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


class ElasticSearchStatus(object):

    """Class:  ElasticSearchStatus

    Description:  Class representation of the ElasticSearchStatus class.

    Methods:
        __init__
        get_mem_status
        get_nodes
        get_cluster
        get_all

    """

    def __init__(self):

        """Method:  __init__

        Description:  Initialization instance of the class.

        Arguments:

        """

        self.hosts = ["hosts"]
        self.port = 9200

    def get_mem_status(self):

        """Method:  get_mem_status

        Description:  Holder for ElasticSearchStatus.get_mem_status method.

        Arguments:

        """

        return {"memory": "memory_status"}

    def get_nodes(self):

        """Method:  get_nodes

        Description:  Stub holder for ElasticSearchStatus.get_nodes method.

        Arguments:

        """

        return {"node": "node_name"}

    def get_cluster(self):

        """Method:  get_cluster

        Description:  Stub holder for ElasticSearchStatus.get_cluster method.

        Arguments:

        """

        return {"cluster": "cluster_name"}

    def get_all(self):

        """Method:  get_all

        Description:  Stub holder for ElasticSearchStatus.get_all method.

        Arguments:

        """

        return {}


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

        self.els = ElasticSearchStatus()
        self.args = ArgParser()
        self.args2 = ArgParser()
        self.args3 = ArgParser()
        self.args4 = ArgParser()
        self.args5 = ArgParser()
        self.args6 = ArgParser()
        self.args7 = ArgParser()
        self.args8 = ArgParser()
        self.args9 = ArgParser()
        self.args.args_array = {"-D": ["all"]}
        self.args2.args_array = {"-D": ["memory"]}
        self.args3.args_array = {"-D": list()}
        self.args4.args_array = {"-D": list(), "-j": True}
        self.args5.args_array = {"-D": ["all"], "-j": True}
        self.args6.args_array = {"-D": ["memory"], "-j": True}
        self.args7.args_array = {"-D": ["incorrect"], "-j": True}
        self.args8.args_array = {"-D": list()}
        self.args9.args_array = dict()
        self.status_call = {"memory": "get_mem_status"}

    @mock.patch("elastic_db_admin.data_out", mock.Mock(return_value=True))
    def test_empty_display_list(self):

        """Function:  test_empty_display_list

        Description:  Test with empty display list.

        Arguments:

        """

        self.assertFalse(
            elastic_db_admin.get_status(
                self.els, status_call=self.status_call,
                args=self.args8))

    @mock.patch("elastic_db_admin.data_out", mock.Mock(return_value=True))
    def test_incorrect_option(self):

        """Function:  test_incorrect_option

        Description:  Test with incorrect option.

        Arguments:

        """

        with gen_libs.no_std_out():
            self.assertFalse(
                elastic_db_admin.get_status(
                    self.els, status_call=self.status_call,
                    args=self.args7))

    @mock.patch("elastic_db_admin.data_out", mock.Mock(return_value=True))
    def test_one_option(self):

        """Function:  test_one_option

        Description:  Test with one option.

        Arguments:

        """

        self.assertFalse(
            elastic_db_admin.get_status(
                self.els, status_call=self.status_call,
                args=self.args6))

    @mock.patch("elastic_db_admin.data_out", mock.Mock(return_value=True))
    def test_all(self):

        """Function:  test_all

        Description:  Test with all option.

        Arguments:

        """

        self.assertFalse(
            elastic_db_admin.get_status(
                self.els, status_call=self.status_call,
                args=self.args5))

    @mock.patch("elastic_db_admin.data_out", mock.Mock(return_value=True))
    def test_no_options(self):

        """Function:  test_no_options

        Description:  Test with no options.

        Arguments:

        """

        self.assertFalse(
            elastic_db_admin.get_status(
                self.els, status_call=self.status_call,
                args=self.args4))

    @mock.patch("elastic_db_admin.data_out", mock.Mock(return_value=True))
    def test_display_all(self):

        """Function:  test_display_all

        Description:  Test with display all option.

        Arguments:

        """

        self.assertFalse(
            elastic_db_admin.get_status(
                self.els, status_call=self.status_call,
                args=self.args))

    @mock.patch("elastic_db_admin.data_out", mock.Mock(return_value=True))
    def test_display_default(self):

        """Function:  test_display_default

        Description:  Test with display default option.

        Arguments:

        """

        self.assertFalse(
            elastic_db_admin.get_status(
                self.els, status_call=self.status_call, args=self.args9))


if __name__ == "__main__":
    unittest.main()
