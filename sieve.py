#! /usr/bin/env python

def numbers(upper_bound):
    return [ (n, []) for n in range(1, upper_bound) ]

def sieve_step(numbers, current_index):
    d = numbers[current_index][0]
    index = 2
    while d * index - 1 < len(numbers):
        numbers[d * index - 1][1].append(d)
        index += 1

def next_current_index(numbers, current_index):
    current_index += 1
    while (len(numbers[current_index][1]) > 0):
        current_index += 1
    return current_index

def sieve(upper_bound):
    ns = numbers(upper_bound)
    ns[0][1].append(0)
    current_index = 1
    while 2 * ns[current_index][0] - 1 < len(ns):
        sieve_step(ns, current_index)
        current_index = next_current_index(ns, current_index)
    return ns

if __name__ == '__main__':
    print sieve(10)
