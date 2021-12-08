#!/usr/bin/python
# Classification (U)

"""Program:  get_status.py

    Description:  Unit testing of get_status in elastic_db_admin.py.

    Usage:
        test/unit/elastic_db_admin/get_status.py

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


class ElasticSearchStatus(object):

    """Class:  ElasticSearchStatus

    Description:  Class representation of the ElasticSearchStatus class.

    Methods:
        __init__
        get_mem_status
        get_nodes
        get_cluster
        get_all

    """

    def __init__(self, hosts, port):

        """Method:  __init__

        Description:  Initialization instance of the class.

        Arguments:

        """

        self.hosts = hosts
        self.port = port

    def get_mem_status(self):

        """Method:  get_mem_status

        Description:  Holder for ElasticSearchStatus.get_mem_status method.

        Arguments:

        """

        return {"memory": "memory_status"}

    def get_nodes(self):

        """Method:  get_nodes

        Description:  Stub holder for ElasticSearchStatus.get_nodes method.

        Arguments:

        """

        return {"node": "node_name"}

    def get_cluster(self):

        """Method:  get_cluster

        Description:  Stub holder for ElasticSearchStatus.get_cluster method.

        Arguments:

        """

        return {"cluster": "cluster_name"}

    def get_all(self):

        """Method:  get_all

        Description:  Stub holder for ElasticSearchStatus.get_all method.

        Arguments:

        """

        return True


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
        test_empty_display_list
        test_incorrect_option
        test_one_option
        test_all
        test_no_options
        test_display_all
        test_display_default

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        self.els = ElasticSearch()
        self.args_array = {"-D": ["all"]}
        self.args_array2 = {"-D": ["memory"]}
        self.args_array3 = {"-D": []}
        self.args_array4 = {"-D": [], "-j": True}
        self.args_array5 = {"-D": ["all"], "-j": True}
        self.args_array6 = {"-D": ["memory"], "-j": True}
        self.args_array7 = {"-D": ["incorrect"], "-j": True}
        self.args_array8 = {"-D": []}
        self.status_call = {"memory": "get_mem_status"}

    @mock.patch("elastic_db_admin.elastic_class.ElasticSearchStatus")
    def test_empty_display_list(self, mock_class):

        """Function:  test_empty_display_list

        Description:  Test with empty display list.

        Arguments:

        """

        mock_class.return_value = ElasticSearchStatus(self.els.hosts,
                                                      self.els.port)

        with gen_libs.no_std_out():
            self.assertFalse(
                elastic_db_admin.get_status(
                    self.els, status_call=self.status_call,
                    args_array=self.args_array8))

    @mock.patch("elastic_db_admin.elastic_class.ElasticSearchStatus")
    def test_incorrect_option(self, mock_class):

        """Function:  test_incorrect_option

        Description:  Test with incorrect option.

        Arguments:

        """

        mock_class.return_value = ElasticSearchStatus(self.els.hosts,
                                                      self.els.port)

        with gen_libs.no_std_out():
            self.assertFalse(
                elastic_db_admin.get_status(
                    self.els, status_call=self.status_call,
                    args_array=self.args_array7))

    @mock.patch("elastic_db_admin.elastic_class.ElasticSearchStatus")
    def test_one_option(self, mock_class):

        """Function:  test_one_option

        Description:  Test with one option.

        Arguments:

        """

        mock_class.return_value = ElasticSearchStatus(self.els.hosts,
                                                      self.els.port)

        with gen_libs.no_std_out():
            self.assertFalse(
                elastic_db_admin.get_status(
                    self.els, status_call=self.status_call,
                    args_array=self.args_array6))

    @mock.patch("elastic_db_admin.elastic_class.ElasticSearchStatus")
    def test_all(self, mock_class):

        """Function:  test_all

        Description:  Test with all option.

        Arguments:

        """

        mock_class.return_value = ElasticSearchStatus(self.els.hosts,
                                                      self.els.port)

        with gen_libs.no_std_out():
            self.assertFalse(
                elastic_db_admin.get_status(
                    self.els, status_call=self.status_call,
                    args_array=self.args_array5))

    @mock.patch("elastic_db_admin.elastic_class.ElasticSearchStatus")
    def test_no_options(self, mock_class):

        """Function:  test_no_options

        Description:  Test with no options.

        Arguments:

        """

        mock_class.return_value = ElasticSearchStatus(self.els.hosts,
                                                      self.els.port)

        with gen_libs.no_std_out():
            self.assertFalse(
                elastic_db_admin.get_status(
                    self.els, status_call=self.status_call,
                    args_array=self.args_array4))

    @mock.patch("elastic_db_admin.elastic_class.ElasticSearchStatus")
    def test_display_all(self, mock_class):

        """Function:  test_display_all

        Description:  Test with display all option.

        Arguments:

        """

        mock_class.return_value = ElasticSearchStatus(self.els.hosts,
                                                      self.els.port)

        with gen_libs.no_std_out():
            self.assertFalse(
                elastic_db_admin.get_status(
                    self.els, status_call=self.status_call,
                    args_array=self.args_array))

    @mock.patch("elastic_db_admin.elastic_class.ElasticSearchStatus")
    def test_display_default(self, mock_class):

        """Function:  test_display_default

        Description:  Test with display default option.

        Arguments:

        """

        mock_class.return_value = ElasticSearchStatus(self.els.hosts,
                                                      self.els.port)

        with gen_libs.no_std_out():
            self.assertFalse(
                elastic_db_admin.get_status(
                    self.els, status_call=self.status_call, args_array={}))


if __name__ == "__main__":
    unittest.main()
