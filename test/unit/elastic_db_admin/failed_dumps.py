#!/usr/bin/python
# Classification (U)

"""Program:  failed_dumps.py

    Description:  Unit testing of failed_dumps in elastic_db_admin.py.

    Usage:
        test/unit/elastic_db_admin/failed_dumps.py

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


class ElasticDump(object):

    """Class:  ElasticDump

    Description:  Class representation of the ElasticDump class.

    Methods:
        __init__ -> Initialize configuration environment.

    """

    def __init__(self, node, repo, port):

        """Method:  __init__

        Description:  Initialization instance of the class.

        Arguments:
            (input) node -> Node name.
            (input) repo -> Repoistory name.
            (input) port -> Port number.

        """

        self.repo_name = repo


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

        self.node = "nodename"
        self.port = 1234
        self.dump_list = ["dump1", "dump2"]


class UnitTest(unittest.TestCase):

    """Class:  UnitTest

    Description:  Class which is a representation of a unit testing.

    Methods:
        setUp -> Initialization for unit testing.
        test_no_repo -> Test with no repo name set.
        test_failed_dumps -> Test failed_dumps function.

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        self.es = ElasticCluster()
        self.args_array = {"-F": "reponame"}

    @mock.patch("elastic_db_admin.elastic_class.ElasticDump")
    def test_no_repo(self, mock_class):

        """Function:  test_no_repo

        Description:  Test with no repo name set.

        Arguments:

        """

        mock_class.return_value = ElasticDump(self.es.node, None, self.es.port)

        with gen_libs.no_std_out():
            self.assertFalse(
                elastic_db_admin.failed_dumps(self.es, args_array={}))

    @mock.patch("elastic_db_admin.elastic_class.ElasticDump")
    @mock.patch("elastic_db_admin.elastic_libs.list_dumps")
    def test_failed_dumps(self, mock_list, mock_class):

        """Function:  test_failed_dumps

        Description:  Test failed_dumps function.

        Arguments:

        """

        mock_list.return_value = True
        mock_class.return_value = ElasticDump(self.es.node,
                                              self.args_array["-F"],
                                              self.es.port)

        with gen_libs.no_std_out():
            self.assertFalse(
                elastic_db_admin.failed_dumps(self.es,
                                              args_array=self.args_array))


if __name__ == "__main__":
    unittest.main()
