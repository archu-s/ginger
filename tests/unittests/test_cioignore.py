#
# Project Gingers390
#
# Copyright IBM, Corp. 2015
#
# This library is free software; you can redistribute it and/or
# modify it under the terms of the GNU Lesser General Public
# License as published by the Free Software Foundation; either
# version 2.1 of the License, or (at your option) any later version.
#
# This library is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public
# License along with this library; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301 USA

import unittest
import mock
import wok.exception as exception
from models.cioignore import CIOIgnoreModel

class CIOIgnoreUnitTests(unittest.TestCase):
    """
    Unit tests for CIO Ignore Model using mock.patch
    """

    @mock.patch('models.cioignore.utils')
    @mock.patch('models.cioignore.wok_log')
    def test_add_devicesto_ignorelist(self, mock_log, mock_utils):
        """
        unittest to add valid list of devices into ignorelist
        mock_log: mock of wok_log present in models.cioignore
        mock_utils: mock of wok.utils imported in models.cioignore
        """
        cioignore = CIOIgnoreModel()
        devices = ["0000", "0002-0018"]
        devicestr = "0000,0002-0018"
        mock_utils.run_command.return_value = ["", "", 0]
        returns = cioignore.add(devices)

        #verify if run_command get called with the command
        command = ['cio_ignore', '-a', devicestr]
        mock_utils.run_command.assert_called_with(command)

        #verify if log get called
        mock_log.info.assert_called_with('Devices: %s  Added sucessfully, rc: %d' % (devicestr, 0))

        #verify return value
        assert returns == {'rc': 0, 'reason': 'Devices: 0000,0002-0018  Added sucessfully'}


    def test_add_invalidparameter(self):
        """
        unittest call add with invalid parameter
        """
        cioignore = CIOIgnoreModel()
        devicestr = "0000,0002-0018"
        self.assertRaises(exception.InvalidParameter, cioignore.add,devicestr)


    @mock.patch('models.cioignore.utils')
    @mock.patch('models.cioignore.wok_log')
    def test_add_valid_invalid_devicesto_ignorelist(self, mock_log, mock_utils):
        """
        unittest to remove valid and invalid devices list from ignorelist
        mock_log: mock of wok_log present in models.cioignore
        mock_utils: mock of wok.utils imported in models.cioignore
        """
        cioignore = CIOIgnoreModel()
        devices = ["0000", "0002-0018","kjhfg","0020"]
        devicestr = "0000,0002-0018,kjhfg,0020"
        mock_utils.run_command.return_value = ["", "cio_ignore: Error: device ID 'kjhfg': device number is not valid", 1]
        #returns = cioignore.add(devices)

        # add method should throw exception
        self.assertRaises(exception.OperationFailed, cioignore.add,devices)

        #verify if run_command get called with the command
        command = ['cio_ignore', '-a', devicestr]
        mock_utils.run_command.assert_called_with(command)

        #verify if log get called
        mock_log.error.assert_called_with('cio_ignore: Error: device ID \'kjhfg\': device number is not valid')

    @mock.patch('models.cioignore.utils')
    @mock.patch('models.cioignore.wok_log')
    def test_remove_devicesfrom_ignorelist(self,mock_log,mock_utils):
        """
        unittest to remove valid list of devices from ignorelist
        mock_log: mock of wok_log present in models.cioignore
        mock_utils: mock of wok.utils imported in models.cioignore
        """
        cioignore = CIOIgnoreModel()
        devices = ["0000", "0002-0018"]
        devicestr = "0000,0002-0018"
        mock_utils.run_command.return_value = ["", "", 0]
        returns = cioignore.remove(devices)

        #verify if run_command get called with the command
        command = ['cio_ignore', '-r', devicestr]
        mock_utils.run_command.assert_called_with(command)

        #verify if log get called
        mock_log.info.assert_called_with('Devices: %s  Removed sucessfully, rc: %d' % (devicestr, 0))

        #verify return value
        assert returns == {'rc': 0, 'reason': 'Devices: 0000,0002-0018  Removed sucessfully'}

    def test_remove_invalidparameter(self):
        """
        unittest call remove with invalid parameter
        """
        cioignore = CIOIgnoreModel()
        devicestr = "0000,0002-0018"
        self.assertRaises(exception.InvalidParameter, cioignore.remove,devicestr)

    @mock.patch('models.cioignore.utils')
    @mock.patch('models.cioignore.wok_log')
    def test_add_valid_invalid_devicefrom_ignorelist(self,mock_log,mock_utils):
        """
        unittest to remove valid and invalid devices into list of devices to add in ignorelist
        mock_log: mock of wok_log present in models.cioignore
        mock_utils: mock of wok.utils imported in models.cioignore
        """
        cioignore = CIOIgnoreModel()
        devices = ["0000", "0002-0018","kjhfg","0020"]
        devicestr = "0000,0002-0018,kjhfg,0020"
        mock_utils.run_command.return_value = ["", "cio_ignore: Error: device ID 'kjhfg': device number is not valid", 1]

        # remove method should throw exception
        self.assertRaises(exception.OperationFailed, cioignore.remove,devices)

        #verify if run_command get called with the command
        command = ['cio_ignore', '-r', devicestr]
        mock_utils.run_command.assert_called_with(command)

        #verify if log get called
        mock_log.error.assert_called_with('cio_ignore: Error: device ID \'kjhfg\': device number is not valid')
