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


class ElasticStatus(object):

    """Class:  ElasticStatus

    Description:  Class representation of the ElasticStatus class.

    Super-Class:  object

    Sub-Classes:

    Methods:
        __init__ -> Initialize configuration environment.
        get_mem_status -> Stub holder for ElasticStatus.get_mem_status method.
        get_nodes -> Stub holder for ElasticStatus.get_nodes method.
        get_cluster -> Stub holder for ElasticStatus.get_cluster method.
        get_all -> Stub holder for ElasticStatus.get_all method.

    """

    def __init__(self, node, port):

        """Method:  __init__

        Description:  Initialization instance of the class.

        Arguments:
            (input) node -> Node name.
            (input) port -> Port number.

        """

        self.node = node
        self.port = port

    def get_mem_status(self, json=False):

        """Method:  get_mem_status

        Description:  Stub holder for ElasticStatus.get_mem_status method.

        Arguments:
            (input) json -> True|False - JSON format.

        """

        if json:
            return {"memory":  "memory_status"}

        else:
            return "memory:  memory_status"

    def get_nodes(self, json=False):

        """Method:  get_nodes

        Description:  Stub holder for ElasticStatus.get_nodes method.

        Arguments:
            (input) json -> True|False - JSON format.

        """

        if json:
            return {"node":  "node_name"}

        else:
            return "node:  node_name"

    def get_cluster(self, json=False):

        """Method:  get_cluster

        Description:  Stub holder for ElasticStatus.get_cluster method.

        Arguments:
            (input) json -> True|False - JSON format.

        """

        if json:
            return {"cluster":  "cluster_name"}

        else:
            return "cluster:  cluster_name"

    def get_all(self, json=False):

        """Method:  get_all

        Description:  Stub holder for ElasticStatus.get_all method.

        Arguments:
            (input) json -> True|False - JSON format.

        """

        return True


class ElasticCluster(object):

    """Class:  ElasticCluster

    Description:  Class representation of the ElasticCluster class.

    Super-Class:  object

    Sub-Classes:

    Methods:
        __init__ -> Initialize configuration environment.

    """

    def __init__(self):

        """Method:  __init__

        Description:  Initialization instance of the class.

        Arguments:

        """

        self.node = "nodename"
        self.port = 1234


class UnitTest(unittest.TestCase):

    """Class:  UnitTest

    Description:  Class which is a representation of a unit testing.

    Super-Class:  unittest.TestCase

    Sub-Classes:

    Methods:
        setUp -> Initialization for unit testing.
        test_incorrect_option -> Test with incorrect option.
        test_json_one_option -> Test with JSON format with one option.
        test_json_all -> Test with JSON format with all option.
        test_json -> Test with JSON format with no options.
        test_std_out_no_options -> Test with standard out with no options.
        test_std_out_one_option -> Test with standard out with one option.
        test_display_all -> Test with display all option.
        test_display_default -> Test with display default option.

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        self.es = ElasticCluster()
        self.args_array = {"-D": ["all"]}
        self.args_array2 = {"-D": ["memory"]}
        self.args_array3 = {"-D": []}
        self.args_array4 = {"-D": [], "-j": True}
        self.args_array5 = {"-D": ["all"], "-j": True}
        self.args_array6 = {"-D": ["memory"], "-j": True}
        self.args_array7 = {"-D": ["incorrect"], "-j": True}
        self.status_call = {"memory": "get_mem_status"}

    @mock.patch("elastic_db_admin.elastic_class.ElasticStatus")
    def test_incorrect_option(self, mock_class):

        """Function:  test_incorrect_option

        Description:  Test with incorrect option.

        Arguments:

        """

        mock_class.return_value = ElasticStatus(self.es.node, self.es.port)

        with gen_libs.no_std_out():
            self.assertFalse(elastic_db_admin.get_status(self.es,
                status_call=self.status_call, args_array=self.args_array7))

    @mock.patch("elastic_db_admin.elastic_class.ElasticStatus")
    def test_json_one_option(self, mock_class):

        """Function:  test_json_one_option

        Description:  Test with JSON format with one option.

        Arguments:

        """

        mock_class.return_value = ElasticStatus(self.es.node, self.es.port)

        with gen_libs.no_std_out():
            self.assertFalse(elastic_db_admin.get_status(self.es,
                status_call=self.status_call, args_array=self.args_array6))

    @mock.patch("elastic_db_admin.elastic_class.ElasticStatus")
    def test_json_all(self, mock_class):

        """Function:  test_json_all

        Description:  Test with JSON format with all option.

        Arguments:

        """

        mock_class.return_value = ElasticStatus(self.es.node, self.es.port)

        with gen_libs.no_std_out():
            self.assertFalse(elastic_db_admin.get_status(self.es,
                status_call=self.status_call, args_array=self.args_array5))

    @mock.patch("elastic_db_admin.elastic_class.ElasticStatus")
    def test_json(self, mock_class):

        """Function:  test_json

        Description:  Test with JSON format with no options.

        Arguments:

        """

        mock_class.return_value = ElasticStatus(self.es.node, self.es.port)

        with gen_libs.no_std_out():
            self.assertFalse(elastic_db_admin.get_status(self.es,
                status_call=self.status_call, args_array=self.args_array4))

    @mock.patch("elastic_db_admin.elastic_class.ElasticStatus")
    def test_std_out_no_options(self, mock_class):

        """Function:  test_std_out_no_options

        Description:  Test with standard out with no options.

        Arguments:

        """

        mock_class.return_value = ElasticStatus(self.es.node, self.es.port)

        with gen_libs.no_std_out():
            self.assertFalse(elastic_db_admin.get_status(self.es,
                status_call=self.status_call, args_array=self.args_array3))

    @mock.patch("elastic_db_admin.elastic_class.ElasticStatus")
    def test_std_out_one_option(self, mock_class):

        """Function:  test_std_out_one_option

        Description:  Test with standard out with one option.

        Arguments:

        """

        mock_class.return_value = ElasticStatus(self.es.node, self.es.port)

        with gen_libs.no_std_out():
            self.assertFalse(elastic_db_admin.get_status(self.es,
                status_call=self.status_call, args_array=self.args_array2))

    @mock.patch("elastic_db_admin.elastic_class.ElasticStatus")
    def test_display_all(self, mock_class):

        """Function:  test_display_all

        Description:  Test with display all option.

        Arguments:

        """

        mock_class.return_value = ElasticStatus(self.es.node, self.es.port)

        with gen_libs.no_std_out():
            self.assertFalse(elastic_db_admin.get_status(self.es,
                status_call=self.status_call, args_array=self.args_array))

    @mock.patch("elastic_db_admin.elastic_class.ElasticStatus")
    def test_display_default(self, mock_class):

        """Function:  test_display_default

        Description:  Test with display default option.

        Arguments:

        """

        mock_class.return_value = ElasticStatus(self.es.node, self.es.port)

        with gen_libs.no_std_out():
            self.assertFalse(elastic_db_admin.get_status(self.es,
                status_call=self.status_call, args_array={}))


if __name__ == "__main__":
    unittest.main()
