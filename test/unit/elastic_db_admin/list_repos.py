# Classification (U)

"""Program:  list_repos.py

    Description:  Unit testing of list_repos in elastic_db_admin.py.

    Usage:
        test/unit/elastic_db_admin/list_repos.py

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

        self.repo_dict = {"node": True}


class UnitTest(unittest.TestCase):

    """Class:  UnitTest

    Description:  Class which is a representation of a unit testing.

    Methods:
        setUp
        test_list_repos

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        self.els = ElasticSearch()

    @mock.patch("elastic_db_admin.elastic_libs.list_repos2")
    def test_list_repos(self, mock_lib):

        """Function:  test_list_repos

        Description:  Test list_repos function.

        Arguments:

        """

        mock_lib.return_value = True

        with gen_libs.no_std_out():
            self.assertFalse(elastic_db_admin.list_repos(self.els))


if __name__ == "__main__":
    unittest.main()
