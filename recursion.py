

def nth_fib_num(n):
    if n <= 1:
        return 0
    elif n == 2:
        return 1
    else:
        return nth_fib_num(n-1) + nth_fib_num(n-2)


def nth_fib_num_test():
    print(nth_fib_num(2))
    print(nth_fib_num(6))