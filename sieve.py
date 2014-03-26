#! /usr/bin/env python

def numbers(upper_bound):
    return [ (n, []) for n in range(1, upper_bound) ]

if __name__ == '__main__':
    numbers = numbers(10)
    print numbers
