#!/usr/bin/env python
# -*- coding: utf-8 -*-

# .py
#
# Copyright (c) 2012 Rodrigo Moreira Araujo
#
# Author: Rodrigo Moreira Araujo <alf.rodrigo@gmail.com>
#
# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU Lesser General Public License
# as published by the Free Software Foundation; either version 2 of
# the License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public
# License along with this program; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA 02111-1307
# USA

from context import series
import unittest

class DateTests(unittest.TestCase):

    def setUp(self):
        self.data = series.Data()

    def testSetCorrectTypeName(self):
        self.data.name = 'data_name'
        self.assertEqual(self.data.name, 'data_name')

    def testSetWrongTypeName(self):
        self.assertRaises(TypeError, setattr, self.data, 'name', 123)

    def testNumberContent(self):
        self.data.content = 25
        self.assertEqual(self.data.content, 25)

    def testTupleContent(self):
        self.data.content = (1,2,3)
        self.assertEqual(self.data.content, (1,2,3))

    def testWrongContent(self):
        self.assertRaises(TypeError, setattr, self.data, 'content', 'wrong')

    def testClear(self):
        self.data.clear()
        self.assertEqual(self.data, series.Data())

    def testWrongClear(self):
        self.data.clear()
        self.assertNotEqual(self.data, series.Data(25))

    def testCopy(self):
        self.data = series.Data(25, '5 data_name')
        other_data = self.data.copy()
        self.assertEqual(self.data, other_data)

def main():
    unittest.main()

if __name__ == "__main__":
    main()

