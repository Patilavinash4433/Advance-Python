# Generators in Python
# Sometimes data is large. Sometimes data is produced over time. Sometimes storing everything at once is unnecessary.

# Generators solve this by producing values one at a time.

# The Core Idea
# A generator does not store all values in memory. It gives you the next value only when you ask for it.

# This makes generators memory efficient.

# Generator Using yield
def get_numbers():
    for i in range(5):
        yield i

# Using it:

for x in get_numbers():
    print(x)

# Values are generated one by one, not all at once.

# Generator vs List
# In Python, you can create generators using parentheses () instead of brackets []. Parenthesis are not tuple comprehensions, they create generators. List version:

numbers = [i for i in range(5)]

# Generator version:

numbers = (i for i in range(5))

# Difference:

# List stores all values
# Generator produces values when needed
# When Generators Are Useful
# Generators are useful when:

# Data is large
# Data comes from files
# Data is processed step by step
# You only need one value at a time
# Example:

def read_lines(filepath):
    with open(filepath) as file:
        for line in file:
            yield line.strip()

# next Function
# You can get the next value from a generator using next().

gen = (x * x for x in range(3))
print(next(gen))  # 0
print(next(gen))  # 1
print(next(gen))  # 4

# Important Limitation
# Generators can be used only once.

# gen = (x for x in range(3))
 
list(gen)
list(gen)

# The second result will be empty.

# Key Takeaway
# Generators produce data lazily
# They save memory
# They fit well with data workflows
# Use them when you do not need all data at once