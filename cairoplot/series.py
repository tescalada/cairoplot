#!/usr/bin/env python
# -*- coding: utf-8 -*-

# series.py
#
# Copyright (c) 2012 Magnun Leno da Silva
#
# Author: Magnun Leno da Silva <magnun.leno@gmail.com>
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

# Contributor: Rodrigo Moreiro Araujo <alf.rodrigo@gmail.com>

NUM_TYPES = (int, float, long)
DATA_TYPES = (int, float, long, tuple)
STR_TYPES = (str, unicode)
FILLING_TYPES = ['solid', 'radial', 'horizontal', 'vertical']
DEFAULT_COLOR_FILLING = 'solid'
#TODO: Define default color list
DEFAULT_COLOR_LIST = None


class Data(object):
    '''
        Model the smallest data structure which might contain:

        - A number (int, float or long);
        - A tuple representing a point with 2 or 3 items (x,y,z).

        Common usage:
            >>> d = Data(name='simple value', 1); print d
            empty: 1
            >>> d = Data('point a', (1,1)); print d
            point a: (1, 1)
            >>> d = Data('point b', (1,2,3)); print d
            point b: (1, 2, 3)
    '''
    def __init__(self, name=None, content=None):
        '''Initiate the objects variables.'''
        self.content = content
        self.name = name

    @property
    def content(self):
        '''
        Property to validate the object's content.

            >>> d = Data(content = 13); print d
            13
            >>> d = Data(content = (1,2)); print d
            (1, 2)
            >>> d = Data(content = (1,2,3)); print d
            (1, 2, 3)

        :raises TypeError: If the input's type is not in :const:`DATA_TYPES`. Also, if the input's type is a tuple but its values' types are not in :const:`NUM_TYPES` or its length is not two or three.
        '''
        return self._content

    @content.setter
    def content(self, content):
        '''Ensure that content is a valid tuple or a number (int, float or long).'''
        # Type: None
        if content is None:
            self._content = None

        # Type: Int or Float
        elif type(content) in NUM_TYPES:
            self._content = content

        # Type: Tuple
        elif type(content) is tuple:
            # Ensures the correct size
            if len(content) not in (2, 3):
                raise TypeError("Content representing points must have two or three items.")

            # Ensures that all items in tuple are numbers
            is_num = lambda x: type(x) not in NUM_TYPES

            if max(map(is_num, content)):
                # An item's type isn't int, float or long
                raise TypeError("All content must be a number (int, float or long)")
            # Append a copy
            self._content = content[:]

        # Unknown type!
        else:
            self._content = 0
            raise TypeError("Content must be int, float, long or a tuple with two or three items")

    # Name property
    @property
    def name(self):
        '''
        Property to validate the object's name.

            >>> d = Data('data_name', 13); print d
            data_name: 13

        :raises TypeError: If the input's type is not in :const:`STR_TYPES`
        '''
        return self._name

    @name.setter
    def name(self, name):
        '''Sets the name of the Data'''
        if type(name) in STR_TYPES and len(name) > 0:
            self._name = name
        elif name is None:
            self._name = None
        else:
            self._name = None
            raise TypeError("Data name must be string or unicode.")

    def clear(self):
        '''Sets name to None and content to 0.'''
        self.name = None
        self.content = None

    def copy(self):
        '''Return a copy of the object'''
        new_data = Data()
        # If it has a name
        if self.name is not None:
            new_data.name = self.name

        # If content is a tuple
        if type(self.content) is tuple:
            new_data.content = self.content[:]
        # If content is a number
        else:
            new_data.content = self.content

        return new_data

    def __eq__(self, other_data):
        '''Compare Data variables'''
        return self.name == other_data.name and \
               self.content == other_data.content

    def __len__(self):
        '''
            Return the length of the content.

            :return: **1**, if content is a number or **length** if a tuple.
        '''
        if type(self.content) in NUM_TYPES:
            return 1
        return len(self.content)

    def __str__(self):
        '''Return a string representation of the Data object'''
        if self.name is None:
            return str(self.content)
        else:
            return self.name + ": " + str(self.content)


class Series(object):
    '''
        Model a list of values that must be either:

        - Numbers (int, float or long);
        - Tuples representing points with 2 or 3 items (x,y,z).

        Common usage:
            >>> s = Series("number_series", [1,2,3,4,5]); print s
            number_series ['1', '2', '3', '4', '5']
            >>> s = Series("point_series", [(1,1,1), (2,2,2), (3,3,3)]); print s
            point_series ['(1, 1, 1)', '(2, 2, 2)', '(3, 3, 3)']
    '''

    def __init__(self, name=None, content=None):
        '''Initiate the objects variables.'''
        self.name = name
        self.content = content

    @property
    def content(self):
        '''
        Property to validate the series.

            >>> s = Series(content = [1,2,3,4,5]); print s
            ['1', '2', '3', '4', '5']
            >>> s = Series(content = [(1,1,1), (2,2,2), (3,3,3)]); print s
            ['(1, 1, 1)', '(2, 2, 2)', '(3, 3, 3)']

        :raises TypeError: If the input's is not a list or if the list contains tuples and numbers (int, float or long) mixed.
        '''
        return self._content

    @content.setter
    def content(self, content):
        '''Ensure that content is a list of numbers (int, float or long) or tuples. Lists containing Data objects along the primitive types are also accepted if they have the same length.'''
        is_num = lambda x: type(x) in NUM_TYPES
        is_tuple = lambda x: type(x) is tuple

        # If content is None
        if content is None:
            self._content = []
        # If content is not a List
        elif type(content) is not list:
            self._content = []
            raise TypeError("Series must be a list containing numbers (int, float or long) or 2 or 3 dimensions tuples.")
        # If content is an empty list
        elif len(content) == 0:
            self._content = []
        # If content contains numbers and tuples
        elif max(map(is_num, content)) and max(map(is_tuple, content)):
            # Content contains numbers and tuples
            raise TypeError("Series must contain either a list of numbers (int, float or long) or 2 or 3 dimensions tuples. Not both types.")
        #Content is either a list of points or a list of numbers
        else:
            self._content = []
            for item in content:
                if type(item) is Data:
                    self._content.append(item.copy())
                else:
                    self._content.append(Data(content=item))

    # Name property
    @property
    def name(self):
        '''
        Property to validate the object's name.
            >>> s = Series("number_series", [1,2,3,4,5]); print s
            number_series ['1', '2', '3', '4', '5']

        :raises TypeError: If the input's type is not in :const:`STR_TYPES`
        '''
        return self._name

    @name.setter
    def name(self, name):
        '''Sets the name of the Data'''
        if type(name) in STR_TYPES and len(name) > 0:
            self._name = name
        elif name is None:
            self._name = None
        else:
            self._name = None
            raise TypeError("Data name must be string or unicode.")

    def clear(self):
        '''Set name to None and content to [].'''
        self.name = None
        self.content = []

    def __eq__(self, other_series):
        '''Compare Series objects'''
        return self.name == other_series.name and \
               self.content == other_series.content

    def __len__(self):
        '''Return the length of the content.'''
        return len(self.content)

    def __str__(self):
        '''Return a string that represents the object'''
        ret = ""
        if self.name is not None:
            ret += self.name + " "
        if len(self.content) > 0:
            list_str = [str(item) for item in self.content]
            ret += str(list_str)
        else:
            ret += "[]"
        return ret
