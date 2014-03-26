#! /usr/bin/env python

from random import choice

class Sieve:
    @staticmethod
    def __numbers(upper_bound):
        ns = [ (n, []) for n in range(1, upper_bound) ]
        ns[0][1].append(0)
        return ns

    @staticmethod
    def __next_current_index(numbers, current_index):
        current_index += 1
        while (len(numbers[current_index][1]) > 0):
            current_index += 1
        return current_index

    def __init__(self, upper_bound):
        self.numbers = Sieve.__numbers(upper_bound)
        self.__sieve();

    def __sieve_step(self, current_index):
        d = self.numbers[current_index][0]
        index = 2
        while d * index - 1 < len(self.numbers):
            self.numbers[d * index - 1][1].append(d)
            index += 1

    def __sieve(self):
        current_index = 1
        while 2 * self.numbers[current_index][0] - 1 < len(self.numbers):
            self.__sieve_step(current_index)
            current_index = Sieve.__next_current_index(self.numbers, current_index)

    def for_primes(self):
        for entry in self.numbers:
            if len(entry[1]) == 0:
                yield entry[0];

if __name__ == '__main__':
    four_digit = []
    for p in Sieve(10000).for_primes():
        if p > 999:
            four_digit.append(p)

    p, q = choice(four_digit), choice(four_digit)
    print min(p, q), max(p, q)
