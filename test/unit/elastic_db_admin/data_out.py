# Classification (U)

"""Program:  data_out.py

    Description:  Unit testing of data_out in elastic_db_admin.py.

    Usage:
        test/unit/elastic_db_admin/data_out.py

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


class Mail(object):

    """Class:  Mail

    Description:  Class stub holder for gen_class.Mail class.

    Methods:
        __init__
        add_2_msg
        send_mail

    """

    def __init__(self):

        """Method:  __init__

        Description:  Class initialization.

        Arguments:

        """

        self.data = None

    def add_2_msg(self, data):

        """Method:  add_2_msg

        Description:  Stub method holder for Mail.add_2_msg.

        Arguments:

        """

        self.data = data

        return True

    def send_mail(self, use_mailx=False):

        """Method:  send_mail

        Description:  Stub method holder for Mail.send_mail.

        Arguments:
            (input) use_mailx -> True|False - To use mailx command.

        """

        status = True

        if use_mailx:
            status = True

        return status


class UnitTest(unittest.TestCase):

    """Class:  UnitTest

    Description:  Class which is a representation of a unit testing.

    Methods:
        setUp
        test_std_out_json
        test_std_out_suppressed
        test_std_out
        test_mail_json
        test_mail
        test_file_json
        test_file_append
        test_file
        test_no_data

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        dir_file = "dir/file"
        self.data = {"key1": "value1", "key2": "value2"}
        self.mail = Mail()
        self.args_array = {}
        self.args_array2 = {"-o": dir_file, "-z": True}
        self.args_array3 = {"-o": dir_file, "-a": True, "-z": True}
        self.args_array4 = {"-o": dir_file, "-j": True, "-z": True}
        self.args_array5 = {"-t": "to_address", "-z": True}
        self.args_array6 = {"-t": "to_address", "-j": True, "-z": True}
        self.args_array7 = {"-z": True}
        self.args_array8 = {"-j": True}

    def test_std_out_json(self):

        """Function:  test_std_out_json

        Description:  Test with standard out with json mode.

        Arguments:

        """

        with gen_libs.no_std_out():
            self.assertFalse(
                elastic_db_admin.data_out(self.data, self.args_array8))

    def test_std_out_suppressed(self):

        """Function:  test_std_out_suppressed

        Description:  Test with standard out suppressed.

        Arguments:

        """

        self.assertFalse(
            elastic_db_admin.data_out(self.data, self.args_array7))

    def test_std_out(self):

        """Function:  test_std_out

        Description:  Test with standard out.

        Arguments:

        """

        with gen_libs.no_std_out():
            self.assertFalse(
                elastic_db_admin.data_out(self.data, self.args_array))

    @mock.patch("elastic_db_admin.gen_class.setup_mail")
    def test_mail_json(self, mock_mail):

        """Function:  test_mail_json

        Description:  Test with mail option with json option.

        Arguments:

        """

        mock_mail.return_value = self.mail

        self.assertFalse(
            elastic_db_admin.data_out(self.data, self.args_array6))

    @mock.patch("elastic_db_admin.gen_class.setup_mail")
    def test_mail(self, mock_mail):

        """Function:  test_mail

        Description:  Test with mail option.

        Arguments:

        """

        mock_mail.return_value = self.mail

        self.assertFalse(
            elastic_db_admin.data_out(self.data, self.args_array5))

    @mock.patch("elastic_db_admin.gen_libs.write_file",
                mock.Mock(return_value=True))
    def test_file_json(self):

        """Function:  test_file_json

        Description:  Test with file option with json option.

        Arguments:

        """

        self.assertFalse(
            elastic_db_admin.data_out(self.data, self.args_array4))

    @mock.patch("elastic_db_admin.gen_libs.write_file",
                mock.Mock(return_value=True))
    def test_file_append(self):

        """Function:  test_file_append

        Description:  Test with file option with append option.

        Arguments:

        """

        self.assertFalse(
            elastic_db_admin.data_out(self.data, self.args_array3))

    @mock.patch("elastic_db_admin.gen_libs.write_file",
                mock.Mock(return_value=True))
    def test_file(self):

        """Function:  test_file

        Description:  Test with file option.

        Arguments:

        """

        self.assertFalse(
            elastic_db_admin.data_out(self.data, self.args_array2))

    def test_no_data(self):

        """Function:  test_no_data

        Description:  Test with no data output.

        Arguments:

        """

        self.assertFalse(
            elastic_db_admin.data_out(self.data, self.args_array7))


if __name__ == "__main__":
    unittest.main()
