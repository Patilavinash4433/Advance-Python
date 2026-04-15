# Iterables & How Python Loops Over Data
# What Problem This Solves
# When working with data, you rarely deal with single values.
# You deal with collections of values.

# Python handles all such collections using iterations.

# Iterables in One Sentence
# If you can loop over something using a for loop, it is an iterable.

a = ["Harry", 5, False, "Shubham"]
for i in a:
    print(i)
#or
data = [10, 20, 30]
 
for x in data:
    print(x)

# Lists, strings, dictionaries, and files are all iterables.

# What the for Loop Does
# A for loop takes values one by one from the data.

# You do not control how the values are fetched. Python does it for you.

# This is why the same loop works for many data types.

# Iterating Over Common Data Structures
# List:

for x in [1, 2, 3]:
    print(x)

# String:

for ch in "data":
    print(ch)

# Dictionary:

record = {"name": "Ali", "age": 20}
 
for key in record:
    print(key)

# Generators
# Sometimes data is produced one value at a time instead of all at once.

# This approach:

# Saves memory
# Is useful for large data
# Is common in data workflows