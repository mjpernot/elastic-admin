# Classification (U)

"""Program:  list_master.py

    Description:  Integration testing of list_master in elastic_db_admin.py.

    Usage:
        test/integration/elastic_db_admin/list_master.py

    Arguments:

"""

# Libraries and Global Variables

# Standard
import sys
import os
import unittest

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
        test_list_master

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        self.base_dir = "test/integration/elastic_db_admin"
        self.test_path = os.path.join(os.getcwd(), self.base_dir)
        self.config_path = os.path.join(self.test_path, "config")
        self.cfg = gen_libs.load_module("elastic", self.config_path)
        self.user = self.cfg.user if hasattr(self.cfg, "user") else None
        self.japd = self.cfg.japd if hasattr(self.cfg, "japd") else None
        self.ca_cert = self.cfg.ssl_client_ca if hasattr(
            self.cfg, "ssl_client_ca") else None
        self.scheme = self.cfg.scheme if hasattr(
            self.cfg, "scheme") else "https"
        self.els = elcs.ElasticSearchStatus(
            self.cfg.host, port=self.cfg.port, user=self.user, japd=self.japd,
            ca_cert=self.ca_cert, scheme=self.scheme)
        self.els.connect()

    def test_list_master(self):

        """Function:  test_list_master

        Description:  Test list_master function.

        Arguments:

        """

        with gen_libs.no_std_out():
            self.assertFalse(elastic_db_admin.list_master(self.els))


if __name__ == "__main__":
    unittest.main()
