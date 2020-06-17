#!/usr/bin/env python


def diff_sum_and_square(n: int, m: int) -> int:
    """Calculate the difference between the sum of squares and square of sums
    for all natural numbers between minimum n and maximum m inclusive.

    Arguments:
        n: int
            The minimum natural number
        m: int
            The maximum natural number

    Return:
        int: difference between sum of squares and square of sums
    """
    return sum([i for i in range(n, m+1)]) ** 2 - sum([i ** 2 for i in range(n, m+1)])


if __name__ == '__main__':
    print(
        'The difference in between the sum of squares of the first one '
        'hundred natural numbers and the square of the sum is: '
        '{}'.format(diff_sum_and_square(1, 100)))
