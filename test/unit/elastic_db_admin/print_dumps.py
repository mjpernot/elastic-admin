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
import unittest
import mock

# Local
sys.path.append(os.getcwd())
import elastic_db_admin                         # pylint:disable=E0401,C0413
import elastic_lib.elastic_class as elcs    # pylint:disable=E0401,C0413,R0402
import lib.gen_libs as gen_libs             # pylint:disable=E0401,C0413,R0402
import version                                  # pylint:disable=E0401,C0413

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
        self.els = elcs.ElasticSearchStatus(
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
