#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Assignment 1 - Part 1"""


def listDivide(numbers, divide=2):
    counter = 0
    for value in numbers:
        if value%divide == 0:
            counter+=1 
    return (counter)

class ListDivideException(Exception):
    pass

def testListDivide():
    if listDivide([1,2,3,4,5]) !=2:
        raise ListDivideException
    if listDivide([2,4,6,8,10]) != 5:
        raise ListDivideException
    if listDivide([30, 54, 63,98, 100], divide=10) != 2:
        raise ListDivideException
    if listDivide([]) != 0:
        raise ListDivideException
    if listDivide([1,2,3,4,5], 1) != 5:
        raise ListDivideException
