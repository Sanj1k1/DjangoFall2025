# file1.py
class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b != 0:
            return a / b
        return "Division by zero!"

def main():
    calc = Calculator()
    for i in range(1, 11):
        print(f"{i} + {i} = {calc.add(i, i)}")
        print(f"{i} - {i//2} = {calc.subtract(i, i//2)}")
        print(f"{i} * 2 = {calc.multiply(i, 2)}")
        print(f"{i} / 2 = {calc.divide(i, 2)}")
    print("Loop done!")

if __name__ == "__main__":
    main()

# Adding extra functions to reach 50 lines
def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n-1)

def fibonacci(n):
    a, b = 0, 1
    result = []
    for _ in range(n):
        result.append(a)
        a, b = b, a + b
    return result

print(factorial(5))
print(fibonacci(10))
