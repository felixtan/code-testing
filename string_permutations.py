#! /usr/bin/env python3

# Cracking the Coding Interview Ch9 Ex 1.2

import sys

def is_permutation(str1, str2):
    def permute(str1, str2, prefix):
        if len(str1) == 0 and str2 == prefix:
            print('Yes')
        else:
            for i in range(len(str1)):
                rem = str1[0:i] + str1[i+1:]
                permute(rem, str2, prefix + str1[i])

    return permute(str1, str2, "")


if __name__ == '__main__':
    is_permutation(sys.argv[1], sys.argv[2])

# TODO
# count/display UNIQUE permutations?
# permutations of substrings of length k where 1 <= k <= len(str)?
# permutations of all substrings?
# is this even the optimal algorithm for calculating permutations?
