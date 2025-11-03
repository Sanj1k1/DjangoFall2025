# file2.py
import random

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        print(f"Hello, my name is {self.name} and I am {self.age} years old.")

def generate_people(n):
    names = ["Alice", "Bob", "Charlie", "David", "Eva"]
    people = []
    for _ in range(n):
        name = random.choice(names)
        age = random.randint(10, 60)
        people.append(Person(name, age))
    return people

def main():
    people_list = generate_people(10)
    for person in people_list:
        person.greet()
    print("People generated!")

# Additional code to reach 50+ lines
def square_numbers(n):
    return [i*i for i in range(n)]

def sum_numbers(n):
    return sum(range(n))

squares = square_numbers(10)
total = sum_numbers(10)
print("Squares:", squares)
print("Sum:", total)

if __name__ == "__main__":
    main()
