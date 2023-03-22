# Classification (U)

"""Program:  list_nodes.py

    Description:  Unit testing of list_nodes in elastic_db_admin.py.

    Usage:
        test/unit/elastic_db_admin/list_nodes.py

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


class ElasticSearch(object):

    """Class:  ElasticSearch

    Description:  Class representation of the ElasticSearch class.

    Methods:
        __init__

    """

    def __init__(self):

        """Method:  __init__

        Description:  Initialization instance of the class.

        Arguments:

        """

        self.nodes = ["Node1", "Node2"]


class UnitTest(unittest.TestCase):

    """Class:  UnitTest

    Description:  Class which is a representation of a unit testing.

    Methods:
        setUp
        test_empty_list_nodes
        test_list_nodes

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        self.els = ElasticSearch()

    def test_empty_list_nodes(self):

        """Function:  test_empty_list_nodes

        Description:  Test with empty list for nodes.

        Arguments:

        """

        self.els.nodes = []

        with gen_libs.no_std_out():
            self.assertFalse(elastic_db_admin.list_nodes(self.els))

    def test_list_nodes(self):

        """Function:  test_list_nodes

        Description:  Test list_nodes function.

        Arguments:

        """

        with gen_libs.no_std_out():
            self.assertFalse(elastic_db_admin.list_nodes(self.els))


if __name__ == "__main__":
    unittest.main()
