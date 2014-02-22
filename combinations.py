#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Combinations module

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
    return print(comb)

#combinations(49,6)
#print(comb)