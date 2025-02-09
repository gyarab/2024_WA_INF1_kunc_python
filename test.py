def fibonacci(n):
    if not isinstance(n, int):
        raise ValueError("n must be an integer")
    
    if n < 0:
        raise ValueError("n must be a positive integer")
    
    elif n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

def celsius_to_fahrenheit(celsius):
    if not isinstance(celsius, (int, float)):
        raise ValueError("celsius must be a number")
    
    return celsius * 9/5 + 32


def fahrenheit_to_celsius(fahrenheit):
    if not isinstance(fahrenheit, (int, float)):
        raise ValueError("fahrenheit must be a number")
    
    return (fahrenheit - 32) * 5/9

def is_prime(number):
    if not isinstance(number, int):
        raise ValueError("n must be an integer")
    
    if number <= 0:
        raise ValueError("n must be a positive integer")
    
    if number < 2:
        return False
    for i in range(2, number):
        if number % i == 0:
            return False
    return True

def primes_in_range(start, end):
    if not isinstance(start, int) or not isinstance(end, int):
        raise ValueError("start and end must be integers")
    
    if start < 0 or end < 0:
        raise ValueError("start and end must be positive integers")
    
    if start > end:
        start, end = end, start 
    
    return [i for i in range(start, end+1) if is_prime(i)]