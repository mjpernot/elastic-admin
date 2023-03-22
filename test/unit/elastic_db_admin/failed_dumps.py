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

        self.els = "Elasticsearch class instance"
        self.hosts = ["nodename1", "nodename2"]
        self.port = 9200
        self.dump_list = None


class UnitTest(unittest.TestCase):

    """Class:  UnitTest

    Description:  Class which is a representation of a unit testing.

    Methods:
        setUp
        test_no_repo
        test_repo

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        self.els = ElasticSearch()
        self.args_array = {"-F": "reponame"}

    @mock.patch("elastic_db_admin.elastic_class.get_repo_list")
    @mock.patch("elastic_db_admin.print_failures")
    def test_no_repo(self, mock_print, mock_repo):

        """Function:  test_no_repo

        Description:  Test with no repo name set.

        Arguments:

        """

        mock_print.return_value = True
        mock_repo.return_value = ["repo1", "repo2"]

        with gen_libs.no_std_out():
            self.assertFalse(
                elastic_db_admin.failed_dumps(self.els, args_array={}))

    @mock.patch("elastic_db_admin.print_failures")
    def test_repo(self, mock_print):

        """Function:  test_repo

        Description:  Test with repo name set.

        Arguments:

        """

        mock_print.return_value = True

        with gen_libs.no_std_out():
            self.assertFalse(
                elastic_db_admin.failed_dumps(self.els,
                                              args_array=self.args_array))


if __name__ == "__main__":
    unittest.main()
