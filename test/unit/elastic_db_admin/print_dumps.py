#!/usr/bin/python
# Classification (U)

"""Program:  print_dumps.py

    Description:  Unit testing of print_dumps in elastic_db_admin.py.

    Usage:
        test/unit/elastic_db_admin/print_dumps.py

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
import elastic_lib.elastic_class as elastic_class
import lib.gen_libs as gen_libs
import version

__version__ = version.__version__


class UnitTest(unittest.TestCase):

    """Class:  UnitTest

    Description:  Class which is a representation of a unit testing.

    Methods:
        setUp
        test_print_dumps

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
            [{"snapshot": "Test_Dump_Name_1"},
             {"snapshot": "Test_Dump_Name_2"}], True, None)

    @mock.patch("elastic_db_admin.elastic_class.get_dump_list")
    @mock.patch("elastic_db_admin.elastic_libs.list_dumps")
    def test_print_dumps(self, mock_list, mock_dumps):

        """Function:  test_print_dumps

        Description:  Test print_dumps function.

        Arguments:

        """

        mock_list.return_value = True
        mock_dumps.return_value = self.dump_list

        with gen_libs.no_std_out():
            self.assertFalse(
                elastic_db_admin.print_dumps(self.els, self.reponame))


if __name__ == "__main__":
    unittest.main()
