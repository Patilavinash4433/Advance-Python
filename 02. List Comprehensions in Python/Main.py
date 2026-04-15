# List Comprehensions in Python #

# When working with data, you often:
# transform values
# filter values
# create new collections from old ones
# List comprehensions are a clean and readable way to do this.

# Basic List Comprehension
# Instead of writing a loop:

numbers = [1, 2, 3, 4, 5]
 
squared = []
for x in numbers:
    squared.append(x * x)
print(squared)
# You can write:

squared = [x * x for x in numbers]
print(squared)
# Same logic, less noise.