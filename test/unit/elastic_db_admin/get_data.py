#!/usr/bin/python
# Classification (U)

"""Program:  get_data.py

    Description:  Unit testing of _get_data in elastic_db_admin.py.

    Usage:
        test/unit/elastic_db_admin/get_data.py

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


class UnitTest(unittest.TestCase):

    """Class:  UnitTest

    Description:  Class which is a representation of a unit testing.

    Super-Class:  unittest.TestCase

    Sub-Classes:

    Methods:
        setUp -> Initialization for unit testing.
        test_incorrect_option -> Test with incorrect option.
        test_json_one_option -> Test with JSON format with one option.
        test_json -> Test with JSON format with no options.
        test_std_out_one_option -> Test with standard out with one option.

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        self.es = ElasticStatus("nodename", 1234)
        self.status_call = {"memory": "get_mem_status"}
        self.json = True
        self.json2 = False
        self.data = {}
        self.data2 = ""
        self.opt = "memory"
        self.opt2 = "incorrect"

    def test_incorrect_option(self):

        """Function:  test_incorrect_option

        Description:  Test with incorrect option.

        Arguments:

        """

        with gen_libs.no_std_out():
            self.assertFalse(elastic_db_admin._get_data(self.json, self.data,
                self.es, self.opt2, status_call=self.status_call))

    def test_json_one_option(self):

        """Function:  test_json_one_option

        Description:  Test with JSON format with one option.

        Arguments:

        """

        with gen_libs.no_std_out():
            self.assertFalse(elastic_db_admin._get_data(self.json, self.data,
                self.es, self.opt, status_call=self.status_call))

    def test_json(self):

        """Function:  test_json

        Description:  Test with JSON format with no options.

        Arguments:

        """

        with gen_libs.no_std_out():
            self.assertFalse(elastic_db_admin._get_data(self.json, self.data,
                self.es, self.opt, status_call=self.status_call))

    def test_std_out_one_option(self):

        """Function:  test_std_out_one_option

        Description:  Test with standard out with one option.

        Arguments:

        """

        with gen_libs.no_std_out():
            self.assertFalse(elastic_db_admin._get_data(self.json2, self.data2,
                self.es, self.opt, status_call=self.status_call))


if __name__ == "__main__":
    unittest.main()
