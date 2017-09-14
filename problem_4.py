#!/usr/bin/python
from math import ceil, floor

def is_palendrome(n,b):
    """
    Return true if n is a palendrome in base b
    """
    n_list = []
    while n > 0:
        n_list.append(n % b)
        n = floor(n / b)
    for i in range(0,ceil((len(n_list)-1)/2)):
        if n_list[i] != n_list[len(n_list)-1-i]:
            return False
    return True

if __name__ == '__main__':
    largest_palendrome = 0
    for i in range(100,999):
        for j in range(100,999):
            if is_palendrome(i*j,10):
                largest_palendrome = i*j if i*j > largest_palendrome else largest_palendrome
    print("The largest palendrome that is the product of two three-digit numbers is "+str(largest_palendrome))
