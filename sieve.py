#! /usr/bin/env python

def numbers(upper_bound):
    return [ (n, []) for n in range(1, upper_bound) ]

if __name__ == '__main__':
    numbers = numbers(10)
    numbers[0][1].append(0)
    current_index = 1
    d = numbers[current_index][0]
    index = 2
    while d * index - 1 < len(numbers):
        numbers[d * index - 1][1].append(d)
        index += 1

    print numbers
