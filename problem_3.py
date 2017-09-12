#!/usr/bin/python
from math import floor

def find_largest_factor(n):
    """
    Return the largest prime factor of n:
    1. Find i such that i is the smallest number that i * j = n
    2. Therefore the largest prime factor of n is also the largest prime factor of j
    3. Repeat until j is a prime number
    """
    for i in range(2,floor(n/2)):
        if n % i == 0:
            return find_largest_factor(int(n/i))
    return n

if __name__ == '__main__':
    print("The largest prime factor of 600851475143 is " + str(find_largest_factor(600851475143)))
