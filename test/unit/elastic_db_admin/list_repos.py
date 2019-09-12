#!/usr/bin/python
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
import version

__version__ = version.__version__


class ElasticCluster(object):

    """Class:  ElasticCluster

    Description:  Class representation of the ElasticCluster class.

    Methods:
        __init__ -> Initialize configuration environment.

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
        setUp -> Initialization for unit testing.
        test_list_repos -> Test list_repos function.

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        self.es = ElasticCluster()

    @mock.patch("elastic_db_admin.elastic_libs.list_repos2")
    def test_list_repos(self, mock_lib):

        """Function:  test_list_repos

        Description:  Test list_repos function.

        Arguments:

        """

        mock_lib.return_value = True

        with gen_libs.no_std_out():
            self.assertFalse(elastic_db_admin.list_repos(self.es))


if __name__ == "__main__":
    unittest.main()
