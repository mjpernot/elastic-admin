# Classification (U)

"""Program:  get_data.py

    Description:  Unit testing of get_data in elastic_db_admin.py.

    Usage:
        test/unit/elastic_db_admin/get_data.py

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
import lib.gen_libs as gen_libs             # pylint:disable=E0401,C0413,R0402
import version                                  # pylint:disable=E0401,C0413

__version__ = version.__version__


class ElasticSearchStatus():

    """Class:  ElasticSearchStatus

    Description:  Class representation of the ElasticSearchStatus class.

    Methods:
        __init__
        get_mem_status
        get_nodes
        get_cluster
        get_all

    """

    def __init__(self, node, port):

        """Method:  __init__

        Description:  Initialization instance of the class.

        Arguments:

        """

        self.node = node
        self.port = port

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

        return True


class UnitTest(unittest.TestCase):

    """Class:  UnitTest

    Description:  Class which is a representation of a unit testing.

    Methods:
        setUp
        test_incorrect_option
        test_one_option
        test_no_option

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        self.els = ElasticSearchStatus("nodename", 1234)
        self.status_call = {"memory": "get_mem_status"}
        self.data = {}
        self.opt = "memory"
        self.opt2 = "incorrect"

    def test_incorrect_option(self):

        """Function:  test_incorrect_option

        Description:  Test with incorrect option.

        Arguments:

        """

        with gen_libs.no_std_out():
            self.assertEqual(
                elastic_db_admin.get_data(
                    self.data, self.els, self.opt2,
                    status_call=self.status_call), ({}))

    def test_one_option(self):

        """Function:  test_one_option

        Description:  Test with one option.

        Arguments:

        """

        self.assertEqual(
            elastic_db_admin.get_data(
                self.data, self.els, self.opt, status_call=self.status_call),
            ({"memory": "memory_status"}))

    def test_no_option(self):

        """Function:  test_no_option

        Description:  Test with no options.

        Arguments:

        """

        self.assertEqual(
            elastic_db_admin.get_data(
                self.data, self.els, self.opt, status_call=self.status_call),
            ({"memory": "memory_status"}))


if __name__ == "__main__":
    unittest.main()
