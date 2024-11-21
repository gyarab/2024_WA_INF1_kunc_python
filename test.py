def fibonacci(n):
    if not isinstance(n, int) or n < 0:
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


def fareheit_to_celsius(fahrenheit):
    if not isinstance(fahrenheit, (int, float)):
        raise ValueError("fahrenheit must be a number")
    
    return (fahrenheit - 32) * 5/9