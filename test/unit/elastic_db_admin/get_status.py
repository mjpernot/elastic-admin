#!/usr/bin/python
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


class ElasticStatus(object):

    """Class:  ElasticStatus

    Description:  Class representation of the ElasticStatus class.

    Super-Class:  object

    Sub-Classes:

    Methods:
        __init__ -> Initialize configuration environment.
        get_all -> Stub holder for ElasticStatus.get_all method.

    """

    def __init__(self, node, port):

        """Method:  __init__

        Description:  Initialization instance of the class.

        Arguments:
            (input) node -> Node name.
            (input) port -> Port number.

        """

        self.repo_name = repo

    def get_all(self, json):

        """Method:  get_all

        Description:  Initialization instance of the class.

        Arguments:
            (input) json -> JSON format?

        """

        return True


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

        self.node = "nodename"
        self.port = 1234


class UnitTest(unittest.TestCase):

    """Class:  UnitTest

    Description:  Class which is a representation of a unit testing.

    Super-Class:  unittest.TestCase

    Sub-Classes:

    Methods:
        setUp -> Initialization for unit testing.
        test_json -> Test with JSON format.
        test_display_all -> Test with display all option.

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        self.es = ElasticCluster()
        self.args_array = {"-L": "reponame"}

    @mock.patch("elastic_db_admin.elastic_class.ElasticStatus")
    def test_json(self, mock_class):

        """Function:  test_json

        Description:  Test with JSON format.

        Arguments:

        """

        mock_class.return_value = ElasticStatus
STOPPED HERE
        with gen_libs.no_std_out():
            self.assertFalse(elastic_db_admin.get_status(self.es))

    @mock.patch("elastic_db_admin.elastic_class.ElasticStatus")
    def test_display_all(self, mock_class):

        """Function:  test_display_all

        Description:  Test with display all option.

        Arguments:

        """

        mock_class.return_value = ElasticStatus

        with gen_libs.no_std_out():
            self.assertFalse(elastic_db_admin.get_status(self.es))


if __name__ == "__main__":
    unittest.main()
