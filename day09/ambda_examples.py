# lambda_examples.py
# Day 09 - Lambda & Functional Programming Basics

# Simple lambda
square = lambda x: x * x
print("Square of 5:", square(5))


# Lambda with two arguments
add = lambda a, b: a + b
print("Addition:", add(10, 20))


# Using map()
numbers = [1, 2, 3, 4, 5]
squares = list(map(lambda x: x * x, numbers))
print("Squares using map:", squares)


# Using filter()
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print("Even numbers using filter:", even_numbers)
