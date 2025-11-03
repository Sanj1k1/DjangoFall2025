# file1.py

def greet(name):
    return f"Hello, {name}!"

def addition(a, b, c):
    return a + b + c

def add(a, b, c, d, e):
    return a + b + c + d + e

def add(a, b, c, d, e, f):
    return a + b + c + d +e + f

def add(a, b, c, d, e, f, g, h, i):
    return a + b + c +d + e + f +g + h + i

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return None
    return a / b

def power(a, b):
    return a ** b

def is_even(n):
    return n % 2 == 0

def is_odd(n):
    return n % 2 != 0

def factorial(n):
    if n == 0:
        return 1
    result = 1
    for i in range(1, n+1):
        result *= i
    return result

def fibonacci(n):
    a, b = 0, 1
    result = []
    for _ in range(n):
        result.append(a)
        a, b = b, a + b
    return result

def sum_list(lst):
    return sum(lst)

def max_list(lst):
    return max(lst)

def min_list(lst):
    return min(lst)

def reverse_list(lst):
    return lst[::-1]

def sort_list(lst):
    return sorted(lst)

def count_occurrences(lst, value):
    return lst.count(value)
<<<<<<< HEAD

<<<<<<< HEAD
<<<<<<< HEAD

=======
>>>>>>> 46c5d05 (duplicate 3)
=======
>>>>>>> 1e9feef (duplicate 4)
=======
_
>>>>>>> 3cd3937 (duplicate 5)
