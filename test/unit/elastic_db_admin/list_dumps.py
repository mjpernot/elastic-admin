#!/usr/bin/python
# Classification (U)

"""Program:  list_dumps.py

    Description:  Unit testing of list_dumps in elastic_db_admin.py.

    Usage:
        test/unit/elastic_db_admin/list_dumps.py

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


class ElasticSearch(object):

    """Class:  ElasticSearch

    Description:  Class representation of the ElasticSearch class.

    Methods:
        __init__ -> Initialize configuration environment.

    """

    def __init__(self):

        """Method:  __init__

        Description:  Initialization instance of the class.

        Arguments:

        """

        self.es = "Elasticsearch class instance"
        self.hosts = ["nodename1", "nodename2"]
        self.port = 1234


class UnitTest(unittest.TestCase):

    """Class:  UnitTest

    Description:  Class which is a representation of a unit testing.

    Methods:
        setUp -> Initialization for unit testing.
        test_no_repo -> Test with no repo name passed.
        test_repo -> Test with repo name passed.

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        self.es = ElasticSearch()
        self.args_array = {"-L": "reponame"}

    @mock.patch("elastic_db_admin.elastic_class.get_repo_list")
    @mock.patch("elastic_db_admin.print_dumps")
    def test_no_repo(self, mock_print, mock_repo):

        """Function:  test_no_repo

        Description:  Test with no repo name passed.

        Arguments:

        """

        mock_print.return_value = True
        mock_repo.return_value = {"repo1": True, "repo2": True}

        with gen_libs.no_std_out():
            self.assertFalse(elastic_db_admin.list_dumps(self.es,
                                                         args_array={}))

    @mock.patch("elastic_db_admin.print_dumps")
    def test_repo(self, mock_print):

        """Function:  test_repo

        Description:  Test with repo name passed.

        Arguments:

        """

        mock_print.return_value = True

        with gen_libs.no_std_out():
            self.assertFalse(
                elastic_db_admin.list_dumps(self.es,
                                            args_array=self.args_array))


if __name__ == "__main__":
    unittest.main()
