# Classification (U)

"""Program:  list_master.py

    Description:  Unit testing of list_master in elastic_db_admin.py.

    Usage:
        test/unit/elastic_db_admin/list_master.py

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
import elastic_db_admin                         # pylint:disable=E0401,C0413
import lib.gen_libs as gen_libs             # pylint:disable=E0401,C0413,R0402
import version                                  # pylint:disable=E0401,C0413

__version__ = version.__version__


class ElasticSearch():                                  # pylint:disable=R0903

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

        self.master = "nodename"


class UnitTest(unittest.TestCase):

    """Class:  UnitTest

    Description:  Class which is a representation of a unit testing.

    Methods:
        setUp
        test_list_master

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        self.els = ElasticSearch()

    @mock.patch("elastic_db_admin.elastic_libs.list_repos2")
    def test_list_master(self, mock_lib):

        """Function:  test_list_master

        Description:  Test list_master function.

        Arguments:

        """

        mock_lib.return_value = True

        with gen_libs.no_std_out():
            self.assertFalse(elastic_db_admin.list_master(self.els))


if __name__ == "__main__":
    unittest.main()
