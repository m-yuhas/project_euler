#!/usr/bin/python

if __name__ == '__main__':
    running_sum = 0
    last_fib = 1
    curr_fib = 1
    while curr_fib < 4e6:
        if curr_fib % 2 == 0:
            running_sum += curr_fib
        curr_fib = last_fib + curr_fib
        last_fib = curr_fib - last_fib
    print("The sum of the even Fibonacci numbers less than 4 million is " + str(running_sum))
