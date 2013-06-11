#! /usr/bin/python
#! -*- coding: utf-8 -*-

"""
Copyright (C) 2012 Yigit Genc

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation
files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy,
modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software
is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES
OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE
LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR
IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
"""

import os
import argparse
import random

class KeyGenerator(object):
    prefix      = None
    length      = None
    count       = None
    keys        = None
    alphabet    = None
    digits      = None
    alnumlib    = None
    filename    = None

    def __init__(self, prefix, length, count, filename):
        self.prefix     = str(prefix)
        self.length     = int(length)
        self.count      = int(count)
        self.keys       = set()
        self.alphabet   = list()
        self.digits     = list()
        self.filename   = str(filename)

    def __generateKey(self):
        self.alphabet   = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
        self.digits     = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        self.alnumlib   = self.alphabet + self.digits

        random.shuffle(self.alnumlib)

        return (self.prefix + ''.join(self.alnumlib[0:self.length]))

    def __checkAndRegenerate(self, key):
        if self.keys.__contains__(key):
            self.__checkAndRegenerate(self.__generateKey())
        else:
            self.keys.add(key)

    def __writeKeysInFile(self):
        FILE = open(os.path.join(os.path.abspath('.'), self.filename), 'w')

        i = 1
        for key in self.keys:
            if i != self.count:
                FILE.write(key + '\n')
            else:
                FILE.write(key)
            i += 1

        FILE.close()
        del self.keys

    def generate(self):
        for i in range(0, self.count):
            self.__checkAndRegenerate(self.__generateKey())
        self.__writeKeysInFile()

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='KeyGenerator')
    parser.add_argument('-p', action='store', type=str, dest='prefix', default='F', help='String value for key prefix.')
    parser.add_argument('-l', action='store', type=int, dest='length', default=6, help='Integer value for generated string excluding prefix.')
    parser.add_argument('-c', action='store', type=int, dest='count', default=10, help='Integer value for number of generated strings.')
    parser.add_argument('-f', action='store', type=str, dest='filename', default='keygenerator-output.txt', help='String value for output filename.')

    #print parser.parse_args(['-p', 'F', '-l', '6', '-c', '10', '-f', 'keygenerator-output.txt'])
    result = parser.parse_args()

    keyGenerator = KeyGenerator(result.prefix, result.length, result.count, result.filename)
    keyGenerator.generate()