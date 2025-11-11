def count_items(items):
    # TODO: Return the number of items in the list
    return len(items)

def sum_numbers(numbers):
    # TODO: Return the sum of all numbers in the list
    return sum(numbers)

def find_largest(numbers):
    # TODO: Return the largest number in the list
    return max(numbers)

def count_even_numbers(numbers):
    # TODO: Return the count of even numbers in the list
    count = 0
    for i in numbers:
        if i % 2 == 0:
            count += 1
    return count

def sum_digits(number):
    # TODO: Return the sum of digits in the given number
    total = 0
    for i in str(number):
        total += int(i)
    return total
       

def count_vowels(string):
    # TODO: Return the count of vowels in the string (case-insensitive)
    vowels = "aeiouAEIOU"
    count = 0
    for char in string:
        if char in vowels:
            count = count +1
    return count
        

def multiply_list_elements(numbers):
    # TODO: Return the product of all elements in the list
    total = 1
    for i in numbers:
        total *= i
    return total

def create_number_triangle(n):
    # TODO: Return a list of strings representing a number triangle
    # Example for n=3: ['1', '22', '333']
    pass

def fibonacci_sequence(n):
    # TODO: Return a list of first n Fibonacci numbers
    pass

def remove_vowels(string):
    # TODO: Return the string with all vowels removed
    vowels = 'aeiouAEIOU'
    count = 0
    for char in string:
        if char in string:
            count += 1
    return string


def create_multiplication_table(n):
    # TODO: Return a 2D list representing multiplication table up to n
    pass

def count_character_frequency(string):
    # TODO: Return a dictionary with character frequencies
    pass

def reverse_words(sentence):
    # TODO: Return the sentence with each word reversed
    char = 'abc'
    for n in range(-1):
        if n in char:
            return sentence

