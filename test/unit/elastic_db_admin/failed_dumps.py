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
import elastic_db_admin                         # pylint:disable=E0401,C0413
import lib.gen_libs as gen_libs             # pylint:disable=E0401,C0413,R0402
import version                                  # pylint:disable=E0401,C0413

__version__ = version.__version__


class ArgParser():                                      # pylint:disable=R0903

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

        self.args_array = {}

    def get_val(self, skey, def_val=None):

        """Method:  get_val

        Description:  Method stub holder for gen_class.ArgParser.get_val.

        Arguments:

        """

        return self.args_array.get(skey, def_val)


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
        self.args = ArgParser()
        self.args2 = ArgParser()
        self.args2.args_array = {"-F": "reponame"}

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
                elastic_db_admin.failed_dumps(self.els, args=self.args))

    @mock.patch("elastic_db_admin.print_failures")
    def test_repo(self, mock_print):

        """Function:  test_repo

        Description:  Test with repo name set.

        Arguments:

        """

        mock_print.return_value = True

        with gen_libs.no_std_out():
            self.assertFalse(
                elastic_db_admin.failed_dumps(self.els, args=self.args2))


if __name__ == "__main__":
    unittest.main()
