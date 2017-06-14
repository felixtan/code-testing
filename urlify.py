#! /usr/bin/env python3

# # Cracking the Coding Interview Ch9 Ex1.3

import sys
import unittest
from time import perf_counter

# O(n^2)
def method1(string):
    spaces = []
    for i, char in enumerate(string):
        if char == ' ':
            spaces.append(i)

    changes = 0
    out = string
    for space in spaces:
        space += changes * 2       # len("%20") - len(" ") = 2
        out = out[0:space] + "%20" + out[space+1:]
        changes += 1

    return out

def method2(string):
    changes = 0
    out = string

    for i, char in enumerate(string):
        if char == ' ':
            space = i + changes * 2
            out = out[0:space] + '%20' + out[space+1:]
            changes += 1

    return out

# Don't use slicing
def method3(string):
    out = ''

    for i, char in enumerate(string):
        if char == ' ':
            out += '%20'
        else:
            out += char

    return out

# Because string concatentatino using ''.join() is faster than + or +=
def method4(string):
    out = []

    for i, char in enumerate(string):
        if char == ' ':
            out.append('%20')
        else:
            out.append(char)

    return ''.join(out)

# Don't use enumerate
def method5(string):
    out = []

    for char in string:
        if char == ' ':
            out.append('%20')
        else:
            out.append(char)

    return ''.join(out)

# for x in X vs for i in range(len(X))?
def method6(string):
    out = []

    for i in range(len(string)):
        char = string[i]
        if char == ' ':
            out.append('%20')
        else:
            out.append(char)

    return ''.join(out)

class TestUrlEncodeSpaces(unittest.TestCase):

    def setUp(self):
        self.functions = [
            method1,
            method2,
            method3,
            method4,
            method5,
            method6
        ]

    def test_encodes_spaces(self):
        for fn in self.functions:
            self.assertEqual(fn('Mr John Smith'), 'Mr%20John%20Smith')
            self.assertEqual(fn('   abc  '), '%20%20%20abc%20%20')
            self.assertEqual(fn('   a b c  '), '%20%20%20a%20b%20c%20%20')

    def test_handles_all_space(self):
        for fn in self.functions:
            self.assertEqual(fn('     '), '%20%20%20%20%20')

    def test_handles_no_space(self):
        for fn in self.functions:
            self.assertEqual(fn('abcdefg'), 'abcdefg')

    def test_performance(self):
        for fn in self.functions:
            for i in range(7):
                test = ''
                spaces = pow(10, i)

                for j in range(spaces):
                    test += ' '

                start = perf_counter()
                res = fn(test)
                elapsed = perf_counter() - start
                print('{}, n={}, {}'.format(fn.__name__, spaces, elapsed))

if __name__ == "__main__":
    unittest.main()
