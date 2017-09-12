#!/usr/bin/python
from math import floor

def sum_of_multiples_of_n(n,max_val):
    """
    Calculates the sum of multiples of n from 0 to some max_val:
    SUM = n + 2n + 3n + ... Mn
    SUM = n * ( 1 + 2 + 3 + ... M )
    SUM = n * (M * (M + 1) / 2)
    M = floor(max_val / n)
    """
    return int(n*floor(max_val/n)*(floor(max_val/n)+1)/2)

if __name__ == "__main__":
    print("The sum of multiples of 3 and 5 below 1000 is " + str(sum_of_multiples_of_n(3,999)+sum_of_multiples_of_n(5,999)-sum_of_multiples_of_n(15,999)))
