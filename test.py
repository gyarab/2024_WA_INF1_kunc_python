def fib(n):
    if not isinstance(n, int) or n <= 0:
        raise ValueError("n must be a positive integer")
    elif n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)
