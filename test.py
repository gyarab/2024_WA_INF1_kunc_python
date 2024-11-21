def fibonacci(n):
    if not isinstance(n, int) or n <= 0:
        raise ValueError("n must be a positive integer")
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)
