#!/usr/bin/python
from math import ceil, sqrt

def find_prime_factors(n):
    """
    Returns an array of the prime factors on n
    Loops from 2 to sqrt(n) to pull off a prime factor
    Recursively computes factors until the remaining number is prime
    """
    for i in range(2,ceil(sqrt(n))+1):
        if n % i == 0:
            return [i] + find_prime_factors(int(n/i))
    return [n]

if __name__ == '__main__':
    prime_factors = {}
    for i in range(2,21):
        prime_factors_of_i = {}
        for j in find_prime_factors(i):
            if j not in prime_factors_of_i:
                prime_factors_of_i[j] = 1
            else:
                prime_factors_of_i[j] += 1
        for key in prime_factors_of_i:
            if key not in prime_factors or prime_factors_of_i[key] > prime_factors[key]:
                prime_factors[key] = prime_factors_of_i[key]
    smallest_multiple = 1
    for key in prime_factors:
        smallest_multiple *= key ** prime_factors[key]
    print("The smallest multiple of the numbers 1 through 20 is "+str(smallest_multiple))
