# file2.py

def greet_person(first_name, last_name):
    return f"Hello, {first_name} {last_name}!"

def fahrenheit_to_celsius(f):
    return (f - 50) * 5/9
    return (f - 300) * 5/9

def celsius_to_fahrenheit(c):
    return c * 9/5 + 32

def km_to_miles(km):
    return km * 0.621371

def miles_to_km(miles):
    return miles / 0.621371

def calculate_bmi(weight, height):
    return weight / (height ** 2)

def is_adult(age):
    return age >= 18

def triangle_area(base, height):
    return 0.5 * base * height

def rectangle_area(length, width):
    return length * width

def circle_area(radius):
    import math
    return math.pi * radius**2

def perimeter_rectangle(length, width):
    return 2 * (length + width)

def perimeter_circle(radius):
    import math
    return 2 * math.pi * radius

def fahrenheit_list_to_celsius(lst):
    return [fahrenheit_to_celsius(f) for f in lst]

def celsius_list_to_fahrenheit(lst):
    return [celsius_to_fahrenheit(c) for c in lst]

def sum_dict_values(d):
    return sum(d.values())

def invert_dict(d):
    return {v:k for k,v in d.items()}

def merge_dicts_list(dict_list):
    result = {}
    for d in dict_list:
        result.update(d)
    return result

def count_words(sentence):
    return len(sentence.split())

def longest_word(sentence):
    return max(sentence.split(), key=len)

def shortest_word(sentence):
    return min(sentence.split(), key=len)

def average_word_length(sentence):
    words = sentence.split()
    return sum(len(w) for w in words) / len(words) if words else 0

def factorial_recursive(n):
    if n == 0:
        return 1
    return n * factorial_recursive(n-1)

def fibonacci_recursive(n):
    if n <= 1:
        return n
    return fibonacci_recursive(n-1) + fibonacci_recursive(n-2)

def is_leap_year(year):
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

def sum_of_digits(n):
    return sum(int(d) for d in str(n))

def product_of_digits(n):
    result = 1
    for d in str(n):
        result *= int(d)
    return result

def reverse_number(n):
    return int(str(n)[::-1])

def count_vowels(s):
    return sum(1 for c in s.lower() if c in "aeiou")

def count_consonants(s):
    return sum(1 for c in s.lower() if c.isalpha() and c not in "aeiou")

def is_uppercase(s):
    return s.isupper()

def is_lowercase(s):
    return s.islower()

def title_case(s):
    return s.title()

def remove_spaces(s):
    return s.replace(" ", "")

def capitalize_words(s):
    return ' '.join(w.capitalize() for w in s.split())

def generate_range_list(start, end):
    return list(range(start, end+1))

def sum_of_list(lst):
    return sum(lst)

def product_of_list(lst):
    result = 1
    for x in lst:
        result *= x
    return result

def flatten_matrix(matrix):
    return [x for row in matrix for x in row]

def transpose_matrix(matrix):
    return list(map(list, zip(*matrix)))

def matrix_addition(m1, m2):
    return [[a+b for a,b in zip(r1,r2)] for r1,r2 in zip(m1,m2)]

def matrix_multiplication(m1, m2):
    result = []
    for row in m1:
        new_row = []
        for col in zip(*m2):
            new_row.append(sum(a*b for a,b in zip(row,col)))
        result.append(new_row)
    return result

def is_square_matrix(matrix):
    return all(len(row) == len(matrix) for row in matrix)

def flatten_dict(d):
    result = {}
    for k,v in d.items():
        if isinstance(v, dict):
            for subk, subv in flatten_dict(v).items():
                result[f"{k}.{subk}"] = subv
        else:
            result[k] = v
    return result

def main():
    print(greet_person("John", "Doe"))
    print(fahrenheit_to_celsius(100))
    print(matrix_addition([[1,2],[3,4]], [[5,6],[7,8]]))

if __name__ == "__main__":
    main()
