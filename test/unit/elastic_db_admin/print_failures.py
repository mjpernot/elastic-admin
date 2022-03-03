#!/usr/bin/python
# Classification (U)

"""Program:  print_failures.py

    Description:  Unit testing of print_failures in elastic_db_admin.py.

    Usage:
        test/unit/elastic_db_admin/print_failures.py

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


class ElasticSearchDump(object):

    """Class:  ElasticSearchDump

    Description:  Class representation of the ElasticSearchDump class.

    Methods:
        __init__

    """

    def __init__(self, hosts, repo, port):

        """Method:  __init__

        Description:  Initialization instance of the class.

        Arguments:

        """

        self.hosts = hosts
        self.port = port
        self.repo_name = repo


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

        self.hosts = ["nodename1", "nodename2"]
        self.port = 9200


class UnitTest(unittest.TestCase):

    """Class:  UnitTest

    Description:  Class which is a representation of a unit testing.

    Methods:
        setUp
        test_other_failures
        test_all_failures
        test_no_failures
        test_print_failures

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        self.els = ElasticSearch()
        self.reponame = "reponame"
        self.dump_list = (
            [{"snapshot": "dump1", "state": "SUCCESS"},
             {"snapshot": "dump2", "state": "FAILED"}], True, None)
        self.dump_list2 = (
            [{"snapshot": "dump1", "state": "SUCCESS"},
             {"snapshot": "dump2", "state": "SUCCESS"}], True, None)
        self.dump_list3 = (
            [{"snapshot": "dump1", "state": "FAILED"},
             {"snapshot": "dump2", "state": "FAILED"}], True, None)
        self.dump_list4 = (
            [{"snapshot": "dump1", "state": "INCOMPATIBLE"},
             {"snapshot": "dump2", "state": "SUCCESS"}], True, None)

    @mock.patch("elastic_db_admin.elastic_class.get_dump_list")
    @mock.patch("elastic_db_admin.elastic_libs.list_dumps")
    def test_other_failures(self, mock_list, mock_dumps):

        """Function:  test_other_failures

        Description:  Test with other types of states.

        Arguments:

        """

        mock_list.return_value = True
        mock_dumps.return_value = self.dump_list4

        with gen_libs.no_std_out():
            self.assertFalse(
                elastic_db_admin.print_failures(self.els, self.reponame))

    @mock.patch("elastic_db_admin.elastic_class.get_dump_list")
    @mock.patch("elastic_db_admin.elastic_libs.list_dumps")
    def test_all_failures(self, mock_list, mock_dumps):

        """Function:  test_all_failures

        Description:  Test with all failed dumps.

        Arguments:

        """

        mock_list.return_value = True
        mock_dumps.return_value = self.dump_list3

        with gen_libs.no_std_out():
            self.assertFalse(
                elastic_db_admin.print_failures(self.els, self.reponame))

    @mock.patch("elastic_db_admin.elastic_class.get_dump_list")
    @mock.patch("elastic_db_admin.elastic_libs.list_dumps")
    def test_no_failures(self, mock_list, mock_dumps):

        """Function:  test_no_failures

        Description:  Test with no failed dumps.

        Arguments:

        """

        mock_list.return_value = True
        mock_dumps.return_value = self.dump_list2

        with gen_libs.no_std_out():
            self.assertFalse(
                elastic_db_admin.print_failures(self.els, self.reponame))

    @mock.patch("elastic_db_admin.elastic_class.get_dump_list")
    @mock.patch("elastic_db_admin.elastic_libs.list_dumps")
    def test_print_failures(self, mock_list, mock_dumps):

        """Function:  test_print_failures

        Description:  Test print_failures function.

        Arguments:

        """

        mock_list.return_value = True
        mock_dumps.return_value = self.dump_list

        with gen_libs.no_std_out():
            self.assertFalse(
                elastic_db_admin.print_failures(self.els, self.reponame))


if __name__ == "__main__":
    unittest.main()
