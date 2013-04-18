### This program is free software; you can redistribute it and/or modify
## it under the terms of the GNU General Public License as published by
## the Free Software Foundation; either version 2 of the License, or
## (at your option) any later version.

## This program is distributed in the hope that it will be useful,
## but WITHOUT ANY WARRANTY; without even the implied warranty of
## MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
## GNU General Public License for more details.

## You should have received a copy of the GNU General Public License
## along with this program; if not, write to the Free Software
## Foundation, Inc., 675 Mass Ave, Cambridge, MA 02139, USA.


from sos.plugins import Plugin, RedHatPlugin

class lsbrelease(Plugin, RedHatPlugin):
    """Linux Standard Base information
    """

    def setup(self):
        self.add_cmd_output("lsb_release -a")
        self.add_cmd_output("lsb_release -d", suggest_filename = "lsb_release", root_symlink = "lsb-release")
        self.add_copy_spec("/etc/lsb-release*")
