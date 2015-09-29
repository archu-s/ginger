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

from wok.control.base import Resource


class CIOIgnore(Resource):
    def __init__(self, model):
        super(CIOIgnore, self).__init__(model)
        self.admin_methods = ['GET', 'POST']
        self.role_key = "administration"
        self.uri_fmt = "/cioignore/%s"
        self.params=['devices']
        self.add = self.generate_action_handler('add', self.params)
        self.remove = self.generate_action_handler('remove', self.params)
        self.purge = self.generate_action_handler('purge')

    @property
    def data(self):
        return self.info
