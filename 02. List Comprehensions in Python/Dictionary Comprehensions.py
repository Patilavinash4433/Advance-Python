# Dictionary Comprehensions
# You can create dictionaries the same way.

items = ["apple", "banana", "cherry"]
prices = [0.5, 0.3, 0.2]
price_dict = {item: price for item, price in zip(items, prices)}

print(price_dict)
# Also you can filter items like this:

scores = {"math": 80, "science": 90, "english": 75}
 
passed = {k: v for k, v in scores.items() if v >= 80}
print(passed)
# Useful when:

# filtering records
# remapping keys or values

# Set Comprehensions
# Set comprehensions remove duplicates automatically.

values = [1, 2, 2, 3, 3, 4]
 
unique_squares = {x * x for x in values}
print(unique_squares)
# This is helpful when you only care about unique results.

