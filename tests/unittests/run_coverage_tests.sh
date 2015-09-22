#!/bin/bash
#
# Project Kimchi
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
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301USA

#mkdir -p venv

# Verify if the required commands exists on the system
#command -v virtualenv >/dev/null 2>&1 || { echo >&2 "virtualenv must be installed for your distribution.  Aborting."; exit 1; }
#command -v pip >/dev/null 2>&1 || { echo >&2 "pip must be installed for your distribution.  Aborting."; exit 1; }

# Start the virtual environment
#virtualenv venv --no-site-packages


# Actiate the virtual environment
#source venv/bin/activate

while read line; do
  case "$line" in
    \#*)
    continue ;; # skip comments
    "")
    continue ;; # skip empty lines
    *)
    venv/bin/python2.7 -c "import $line" > /dev/null 2>&1
    status=$?
    if [ $status -ne 0 ]; then
        pip install -r requirements.txt # Install the required modules to run tests
        break
    fi
  esac
done < requirements.txt

export PYTHONPATH="${PYTHONPATH}:../../:/usr/lib/python2.7/site-packages/"
# Execute the test suite
coverage run -m unittest test_cioignore
coverage html

# Deativate the virtual environment
#deactivate
