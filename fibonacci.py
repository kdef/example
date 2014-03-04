import sys
import re

def fibNum(n):
    # calculate the nth fibonacci number

    if n == 0 or n == 1:
        return n
    else:
        return fibNum(n - 1) + fibNum(n - 2)

def fibNum_iterative(n):
    # calculate the nth fibonacci number

    if n == 0 or n == 1:
        return n

    a = 0
    b = 1
    for i in range(2, n + 1):
        tmp = a
        a = b
        b = tmp + b
    return b

def printFib(n):
    # print a sequence of fibonacci numbers up to n
    
    sequence = ''
    for i in range(n):
        sequence += str(fibNum(i)) + ', '
    print re.sub(r', $', '\n', sequence)

def sumFib(n):
    # calculate the sum of the first n fibonacci numbers
    
    fib_sum = 0
    for i in range(n):
        fib_sum += fibNum_iterative(i)
    return fib_sum

try:
    test = int(sys.argv[1])
except IndexError:
    test = 10
printFib(test)
print 'Sum = ' + str(sumFib(test))
