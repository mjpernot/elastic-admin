#!/usr/bin/python
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

    Super-Class:  object

    Sub-Classes:

    Methods:
        __init__ -> Initialize configuration environment.

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

    Super-Class:  unittest.TestCase

    Sub-Classes:

    Methods:
        setUp -> Initialization for unit testing.
        test_list_master -> Test list_master function.

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        self.es = ElasticCluster()

    @mock.patch("elastic_db_admin.elastic_libs.list_repos2")
    def test_list_master(self, mock_lib):

        """Function:  test_list_master

        Description:  Test list_master function.

        Arguments:

        """

        mock_lib.return_value = True

        with gen_libs.no_std_out():
            self.assertFalse(elastic_db_admin.list_master(self.es))


if __name__ == "__main__":
    unittest.main()
