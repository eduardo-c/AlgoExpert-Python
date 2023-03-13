

def nth_fib_num(n):
    """
    The Fibonacci sequence is defined as follows: the first number of the sequence is 0,
    the second number is 1, and the nth number is the sum of the (n - 1)th and (n - 2)th numbers.
    Write a function that takes in an integer n and returns the nth Fibonacci number.

    Important note: the Fibonacci sequence is often defined with its first two numbers as f(0) = 0
    and f(1) = 1. For the purpose of this question, the first Fibonacci number is f(0); therefore,
    getNthFib(1) is equtal to f(0), getNthFib(2) is equal to f(1), etc

    Sample Input:
    n = 6

    Sample Output:
    5 // 0, 1, 1, 2, 3, 5

    Optimal Space & Time Complexity
    O(n) time | O(1) space - where n is the input number

    :param n:
    :return:
    """
    if n <= 1:
        return 0
    elif n == 2:
        return 1
    else:
        return nth_fib_num(n-1) + nth_fib_num(n-2)


def nth_fib_num_test():
    print(nth_fib_num(2))
    print(nth_fib_num(6))