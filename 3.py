# file3.py

def fibonacci_generator(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

def factorial_generator(n):
    result = 1
    for i in range(1, n+1):
        result *= i
        yield result

def prime_generator(limit):
    for n in range(2, limit+1):
        for i in range(2, int(n**0.5)+1):
            if n % i == 0:
                break
        else:
            yield n

def even_numbers(lst):
    return [x for x in lst if x % 2 == 0]

def odd_numbers(lst):
    return [x for x in lst if x % 2 != 0]

def squares(lst):
    return [x**2 for x in lst]

def cubes(lst):
    return [x**3 for x in lst]

def reverse_list_inplace(lst):
    lst.reverse()
    return lst

def merge_sorted_lists(lst1, lst2):
    return sorted(lst1 + lst2)

def unique_sorted(lst):
    return sorted(set(lst))

def dict_values_to_list(d):
    return list(d.values())

def dict_keys_to_list(d):
    return list(d.keys())

def swap_dict_keys_values(d):
    return {v:k for k,v in d.items()}

def sum_nested_list(lst):
    return sum(sum(inner) if isinstance(inner,list) else inner for inner in lst)

def multiply_nested_list(lst):
    result = 1
    for item in lst:
        if isinstance(item, list):
            for x in item:
                result *= x
        else:
            result *= item
    return result

def factorial_list(lst):
    import math
    return [math.factorial(x) for x in lst]

def fibonacci_list(n):
    return list(fibonacci_generator(n))

def is_palindrome_number(n):
    return str(n) == str(n)[::-1]

def reverse_string(s):
    return s[::-1]

def count_characters(s):
    from collections import Counter
    return Counter(s)

def common_elements(lst1, lst2):
    return list(set(lst1) & set(lst2))

def difference_elements(lst1, lst2):
    return list(set(lst1) - set(lst2))

def symmetric_difference(lst1, lst2):
    return list(set(lst1) ^ set(lst2))

def flatten_list_of_lists(lol):
    return [item for sublist in lol for item in sublist]

def matrix_sum(matrix):
    return sum(sum(row) for row in matrix)

def matrix_product(matrix):
    import math
    result = 1
    for row in matrix:
        for x in row:
            result *= x
    return result

def transpose(matrix):
    return list(map(list, zip(*matrix)))

def main():
    print(list(fibonacci_generator(10)))
    print(list(prime_generator(20)))
    print(flatten_list_of_lists([[1,2],[3,4],[5]]))

if __name__ == "__main__":
    main()
