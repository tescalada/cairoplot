#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# series_tests.py
#
# Copyright (c) 2012 Rodrigo Moreira Araujo
#
# Author: Rodrigo Moreira Araujo <alf [dot] rodrigo [at] gmail [dot] com>
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

    def testOneDimesionContent(self):
        self.data.content = 25
        self.assertEqual(self.data.content, (25, 0, 0))

    def testTwoDimensionContent(self):
        self.data.content = (1, 2)
        self.assertEqual(self.data.content, (1, 2, 0))

    def testThreeDimensionContent(self):
        self.data.content = (1, 2, 3)
        self.assertEqual(self.data.content, (1, 2, 3))

    def testWrongContent(self):
        self.assertRaises(TypeError, setattr, self.data, 'content', 'wrong')

    def testWrongTupleContent(self):
        self.assertRaises(TypeError, setattr, self.data, 'content', (1, 2, 'wrong'))

    def testSetCorrectTypeName(self):
        self.data.name = 'data_name'
        self.assertEqual(self.data.name, 'data_name')

    def testSetWrongTypeName(self):
        self.assertRaises(TypeError, setattr, self.data, 'name', 123)

    def testClear(self):
        self.data.clear()
        self.assertEqual(self.data, series.Data())

    def testWrongClear(self):
        self.data.clear()
        self.assertNotEqual(self.data, series.Data(content=25))

    def testCopy(self):
        self.data = series.Data('data_name', 25)
        other_data = self.data.copy()
        self.assertEqual(self.data, other_data)


class SeriesTests(unittest.TestCase):

    def setUp(self):
        pass

    def testNumberInput(self):
        #testing a list containing numbers
        list_input = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        desired_input = [series.Data(content=item) for item in list_input]
        self.series = series.Series(content=list_input)
        self.assertEqual(self.series.content, desired_input)

    def testPointInput(self):
        #testing a list containing tuples representing points
        list_input = [(1, 1, 1), (2, 2, 2), (3, 3, 3), (4, 4, 4)]
        desired_input = [series.Data(content=item) for item in list_input]
        self.series = series.Series(content=list_input)
        self.assertEqual(self.series.content, desired_input)

    def testDataInput(self):
        #testing a list containing Data objects
        list_input = [(1, 1, 1), (2, 2, 2), (3, 3, 3), (4, 4, 4)]
        data_input = [series.Data('point', item) for item in list_input]
        desired_input = [series.Data('point', (1, 1, 1)), series.Data('point', (2, 2, 2)),
                         series.Data('point', (3, 3, 3)), series.Data('point', (4, 4, 4))]
        self.series = series.Series(content=data_input)
        self.assertEqual(self.series.content, desired_input)

    def testDataNumberInput(self):
        #testing a list containing both Numbers and Data
        list_input = [1, 2, series.Data('point', 3)]
        desired_input = [series.Data(content=1), series.Data(content=2), series.Data('point', 3)]
        self.series = series.Series(content=list_input)
        self.assertEqual(self.series.content, desired_input)

    def testDataPointInput(self):
        #testing a list containing both Points and Data
        list_input = [(1, 1, 1), (2, 2, 2), series.Data('point', (3, 3, 3))]
        desired_input = [series.Data(content=(1, 1, 1)), series.Data(content=(2, 2, 2)), series.Data('point', (3, 3, 3))]
        self.series = series.Series(content=list_input)
        self.assertEqual(self.series.content, desired_input)

    def testWrongTypeContentSeries(self):
        #testing the input of a dictionary instead of a list
        dummy_input = [1, 2, 3, 4]
        dict_input = {'aaa': (1, 1, 1), 'bbb': (2, 2, 2), 'ccc': (3, 3, 3)}
        self.series = series.Series(content=dummy_input)
        self.assertRaises(TypeError, setattr, self.series, 'content', dict_input)

    def testMixedListSeries(self):
        #testing a list containing both tuples and numbers
        dummy_input = [1, 2, 3, 4]
        list_input = [(1, 1, 1), 2, 3, (4, 4, 4)]
        self.series = series.Series(content=dummy_input)
        self.assertRaises(TypeError, setattr, self.series, 'content', list_input)

    def testClear(self):
        list_input = [(1, 1, 1), (2, 2, 2), (3, 3, 3), (4, 4, 4)]
        self.series = series.Series('a_series', list_input)
        self.series.clear()
        self.assertEqual(self.series, series.Series())

    def testWrongClear(self):
        list_input = [(1, 1, 1), (2, 2, 2), (3, 3, 3), (4, 4, 4)]
        self.series = series.Series('a_series', list_input)
        self.series.clear()
        self.assertNotEqual(self.series, series.Series(content=[1, 2, 3, 4]))


def main():
    unittest.main()

if __name__ == "__main__":
    main()
