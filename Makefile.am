#
# Kimchi
#
# Copyright IBM Corp, 2014
#
# Authors:
#  Mark Wu <wudxw@linux.vnet.ibm.com>
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

SUBDIRS=controls models

ginger_PYTHON = \
	__init__.py \
	ginger.py \
	i18n.py \
	$(NULL)

gingerdir = $(pythondir)/kimchi/plugins/ginger

confdir = $(sysconfdir)/kimchi/plugins.d/ginger
dist_conf_DATA = ginger.conf

EXTRA_DIST = \
	API.json

install-data-local:
	$(MKDIR_P) $(DESTDIR)$(gingerdir)
	$(INSTALL_DATA) API.json $(DESTDIR)$(gingerdir)/API.json