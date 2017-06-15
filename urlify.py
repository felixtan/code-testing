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

functions = [
    method1,
    method2,
    method3,
    method4,
    method5,
    method6
]

class TestUrlEncodeSpaces(unittest.TestCase):

    def setUp(self):
        self.functions = functions

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
    for fn in functions:
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

# n = length of string containing only spaces
#
# Round 1
# method1, n=1, 2.3700000042481406e-06
# method1, n=10, 6.957999971746176e-06
# method1, n=100, 0.0006272440000429924
# method1, n=1000, 0.000975948000018434
# method1, n=10000, 0.04000915200003874
# method1, n=100000, 2.9512804709999614
# method1, n=1000000, 703.1200730909999
# method2, n=1, 9.318000138591742e-06
# method2, n=10, 6.8819999796687625e-06
# method2, n=100, 5.608800006484671e-05
# method2, n=1000, 0.0009302290000050562
# method2, n=10000, 0.023191182000118715
# method2, n=100000, 2.389140050000151
# method2, n=1000000, 467.5713609070001
# method3, n=1, 3.8619998576905346e-06
# method3, n=10, 2.4020000637392513e-06
# method3, n=100, 1.6729999970266363e-05
# method3, n=1000, 0.00042645400003493705
# method3, n=10000, 0.002171464999946693
# method3, n=100000, 0.01831272300000819
# method3, n=1000000, 0.1858654090001437
# method4, n=1, 6.3019999743119115e-06
# method4, n=10, 5.2519999371725135e-06
# method4, n=100, 1.471799987484701e-05
# method4, n=1000, 0.0001346510000530543
# method4, n=10000, 0.0017829010000696144
# method4, n=100000, 0.017693536000024324
# method4, n=1000000, 0.1633743949998916
# method5, n=1, 5.073000011179829e-06
# method5, n=10, 4.515000000537839e-06
# method5, n=100, 1.2294000043766573e-05
# method5, n=1000, 9.129199997914839e-05
# method5, n=10000, 0.0012461489998258912
# method5, n=100000, 0.012448151000171492
# method5, n=1000000, 0.11584482700004628
# method6, n=1, 6.264000148803461e-06
# method6, n=10, 5.031999990023905e-06
# method6, n=100, 1.6010000081223552e-05
# method6, n=1000, 0.00015952800004015444
# method6, n=10000, 0.002017044000012902
# method6, n=100000, 0.02022766999994019
# method6, n=1000000, 0.17055876600011288

# Round 2
# method1, n=1, 3.493999884085497e-06
# method1, n=10, 8.15700013845344e-06
# method1, n=100, 5.5762000101822196e-05
# method1, n=1000, 0.0009930500000336906
# method1, n=10000, 0.02397788300004322
# method1, n=100000, 3.6161008740000398
# method1, n=1000000, 762.3297565340004
# method2, n=1, 9.342000339529477e-06
# method2, n=10, 6.785000550735276e-06
# method2, n=100, 0.00016235900056926766
# method2, n=1000, 0.0010060099994007032
# method2, n=10000, 0.02250664199982566
# method2, n=100000, 2.5681504149997636
# method2, n=1000000, 449.6530795589997
# method3, n=1, 4.737000381282996e-06
# method3, n=10, 2.4820001272019e-06
# method3, n=100, 1.7344999832857866e-05
# method3, n=1000, 0.00011528699997143121
# method3, n=10000, 0.0014766129997951793
# method3, n=100000, 0.024522328999410092
# method3, n=1000000, 0.1532788279992019
# method4, n=1, 6.281999958446249e-06
# method4, n=10, 5.5930004236870445e-06
# method4, n=100, 1.5994999557733536e-05
# method4, n=1000, 0.00013015100012125913
# method4, n=10000, 0.0016715330002625706
# method4, n=100000, 0.017873914999654517
# method4, n=1000000, 0.15236026999991736
# method5, n=1, 5.120999958307948e-06
# method5, n=10, 3.684000148496125e-06
# method5, n=100, 1.244000031874748e-05
# method5, n=1000, 0.00021755300076620188
# method5, n=10000, 0.001049186000273039
# method5, n=100000, 0.014547851000315859
# method5, n=1000000, 0.11692489699998987
# method6, n=1, 6.486000529548619e-06
# method6, n=10, 5.2879995564580895e-06
# method6, n=100, 1.5577000340272207e-05
# method6, n=1000, 0.00014449500031332718
# method6, n=10000, 0.001479687000028207
# method6, n=100000, 0.016534772999875713
# method6, n=1000000, 0.16264299300019047
