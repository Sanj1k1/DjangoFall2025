# file3.py
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def prime_numbers(n):
    primes = []
    for i in range(2, n):
        if is_prime(i):
            primes.append(i)
    return primes

def main():
    n = 30
    print(f"Prime numbers up to {n}: {prime_numbers(n)}")
    numbers = list(range(1, n+1))
    squares = [x**2 for x in numbers]
    cubes = [x**3 for x in numbers]
    print("Squares:", squares)
    print("Cubes:", cubes)

# Extra functions to reach 50+ lines
def fibonacci(n):
    a, b = 0, 1
    result = []
    for _ in range(n):
        result.append(a)
        a, b = b, a + b
    return result

def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n-1)

fib = fibonacci(10)
fact = factorial(5)
print("Fibonacci:", fib)
print("Factorial:", fact)

if __name__ == "__main__":
    main()
