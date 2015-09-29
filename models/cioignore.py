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
import cherrypy
import platform
import wok.utils as utils
from wok.exception import OperationFailed, InvalidParameter

wok_log = cherrypy.log.error_log
cio_ignore = "cio_ignore"


class CIOIgnoreModel(object):

    # def lookup(self, params):
    #     return {'dummy': "dummy"}
# 
#     def adddummy(selfself,params):
#         return {'dummy': "dummytest"}


    def add(self, name, devices):
        """
        Add one or more device IDs to the blacklist.
        DEVID can be a single device ID. or it can be a range of device IDs, or  a comma-separated list of device IDs
        or ranges.Ranges may not cross SSID boundaries.

        devices : List of device IDs. List can contain range of device IDs
                device ID format: "<CSSID>.<SSID>.<DEVNO>". For example: "0.0.0190"
                Devices for which CSSID and SSID are 0 can alternatively be specified by using only the device number,
                either with or without leading "0x" and zeros.  For example: "190", "0x190" or "0190".
        """
        # Check the instance of devices.
        if not (isinstance(devices, list)):
            raise InvalidParameter('GS390INVPARAM', {'reason': 'input must be of type list'})
        # Convert the list to String with comma seperated value
        devices = ','.join(str(device) for device in devices)
        # command to add devices into cio_ignore list
        command = [cio_ignore, '-a', devices]
        output, err, rc = utils.run_command(command)
	err = err.replace("cio_ignore: Error: ",'').strip()
        if rc:
            wok_log.error(err)
            raise OperationFailed('GS390ADDIGRE', {'rc': rc, 'reason': err})

        wok_log.info('Devices: %s  Added sucessfully, rc: %d' % (devices, rc))


    def remove(self, name, devices):
        """
        Remove one or more device IDs from the blacklist.
        DEVID can be a single device ID. or it can be a range of device IDs, or  a comma-separated list of device IDs
        or ranges.Ranges may not cross SSID boundaries.

        devices : List of device IDs. List can contain range of device IDs
                device ID format: "<CSSID>.<SSID>.<DEVNO>". For example: "0.0.0190"
                Devices for which CSSID and SSID are 0 can alternatively be specified by using only the device number,
                either with or without leading "0x" and zeros.  For example: "190", "0x190" or "0190".
        """
        # Check the instance of devices.
        if not (isinstance(devices, list)):
            raise InvalidParameter('GS390INVPARAM', {'rc': '', 'reason': 'input must be of type list'})
        # Convert the list to String with comma seperated value
        devices = ','.join(str(device) for device in devices)
        # command to add devices into cio_ignore list
        command = [cio_ignore, '-r', devices]
        output, err, rc = utils.run_command(command)
	err = err.replace("cio_ignore: Error: ",'').strip()
        if rc:
            wok_log.error(err)
            raise OperationFailed('GS390RMVIGRE', {'rc': rc, 'reason': err})

        wok_log.info('Devices: %s  Removed sucessfully, rc: %d' % (devices, rc))
        
    def purge(self, name):
        """
        purge all offline devices in blacklist
        """
        # command to purge cioignore blacklist offlined devices
        command = [cio_ignore, '-p']
        output, err, rc = utils.run_command(command)
	err = err.replace("cio_ignore: Error: ",'').strip()
        if rc:
            wok_log.error(err)
            raise OperationFailed('GS390PGEIGRE', {'rc': rc, 'reason': err})

        wok_log.info('Sucessfully purge cioignore blacklist offlined devices, rc: %d' % (rc))

    def is_feature_available(self):
        return platform.machine().startswith('s390x')
