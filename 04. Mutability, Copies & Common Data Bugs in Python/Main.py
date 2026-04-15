# Mutability, Copies & Common Data Bugs in Python
# Many data bugs in Python are not syntax errors. They happen because data changes in places you did not expect.

# This usually comes from mutability.

# Mutable vs Immutable (Only What You Need)
# Immutable objects cannot be changed:

# int
# float
# str
# tuple
# Mutable objects can be changed:

# list
# dict
# set
# The Most Common Bug
a = [1, 2, 3]
b = a
 
b.append(4)
 
print(a)

# Both a and b change.

# Why:

# a and b point to the same data
# No copy was created
# Copying Data Correctly
# Shallow copy:

a = [1, 2, 3]
b = a.copy()

# Now changes to b do not affect a.

# For dictionaries:

record = {"name": "Ali", "marks": [80, 90]}
copy_record = record.copy()

# Nested data can still be shared.

# Hidden Mutation Inside Functions
def add_item(items):
    items.append(10)
 
data = [1, 2, 3]
add_item(data)
 
print(data)

# Functions can modify mutable data passed to them.

# This is expected behavior, but often forgotten.
