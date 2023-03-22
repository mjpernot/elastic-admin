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
import unittest
import mock

# Local
sys.path.append(os.getcwd())
import elastic_db_admin
import elastic_lib.elastic_class as elastic_class
import lib.gen_libs as gen_libs
import version

__version__ = version.__version__


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

        self.host = "localhost"
        self.user = "UserName"
        self.japd = "japd"
        self.els = elastic_class.ElasticSearchStatus(
            self.host, user=self.user, japd=self.japd)
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
