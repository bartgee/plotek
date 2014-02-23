#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Combinations module


def splitthousands(s, sep=','):
    if len(s) <= 3: return s
    return splitthousands(s[:-3], sep) + sep + s[-3:]


def factorial(x):
    if x == 0:
        return 1
    else:
        return x * factorial(x-1)


def combinations(nums,numsdrawed):
    #global comb
    n = factorial(nums)
    k = factorial(numsdrawed) * factorial(nums - numsdrawed)
    comb = n / k
    comb = int(comb)
    #return print(comb)
    return comb


def matched(nums,numsdrawed,matched):
    global comb
    n = nums
    k = 20
    r = numsdrawed
    s = matched
    print(n,k,r,s)
    c1 = factorial(n) / (factorial(r) * factorial(n - r))
    c2 = factorial(k) / (factorial(s) * factorial(k -s))
    c3 = factorial(n - k) / (factorial(r - s) * factorial(n - k - (r - s)))
    comb = c1 / (c2 * c3)
    comb = int(round(comb,0))
    return comb
#combinations(49,6)
#print(comb)

#matched(80,10,10)
#print(comb)

