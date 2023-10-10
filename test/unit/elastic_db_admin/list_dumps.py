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
import unittest
import mock

# Local
sys.path.append(os.getcwd())
import elastic_db_admin
import lib.gen_libs as gen_libs
import version

__version__ = version.__version__


class ArgParser(object):

    """Class:  ArgParser

    Description:  Class stub holder for gen_class.ArgParser class.

    Methods:
        __init__
        get_val

    """

    def __init__(self):

        """Method:  __init__

        Description:  Class initialization.

        Arguments:

        """

        self.args_array = dict()

    def get_val(self, skey, def_val=None):

        """Method:  get_val

        Description:  Method stub holder for gen_class.ArgParser.get_val.

        Arguments:

        """

        return self.args_array.get(skey, def_val)


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
        self.repo_dict = {"reponame": "Repo", "reponame2": "Repo"}


class UnitTest(unittest.TestCase):

    """Class:  UnitTest

    Description:  Class which is a representation of a unit testing.

    Methods:
        setUp
        test_repo_incorrect
        test_no_repo
        test_repo

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        self.els = ElasticSearch()
        self.args = ArgParser()
        self.args2 = ArgParser()
        self.args3 = ArgParser()
        self.args.args_array = {"-L": "reponame"}
        self.args2.args_array = {"-L": "reponame3"}

    def test_repo_incorrect(self):

        """Function:  test_repo_incorrect

        Description:  Test with incorrect repo name.

        Arguments:

        """

        with gen_libs.no_std_out():
            self.assertFalse(
                elastic_db_admin.list_dumps(self.els, args=self.args2))

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
            self.assertFalse(
                elastic_db_admin.list_dumps(self.els, args=self.args3))

    @mock.patch("elastic_db_admin.print_dumps")
    def test_repo(self, mock_print):

        """Function:  test_repo

        Description:  Test with repo name passed.

        Arguments:

        """

        mock_print.return_value = True

        with gen_libs.no_std_out():
            self.assertFalse(
                elastic_db_admin.list_dumps(self.els, args=self.args))


if __name__ == "__main__":
    unittest.main()
