# Nested Comprehensions
pairs = [(x, y) for x in [1, 2] for y in [3, 4]]
print(pairs)
# Use this sparingly. If it hurts readability, use a normal loop.

# When NOT to Use Comprehensions
# Avoid comprehensions when:

# logic becomes hard to read
# there are multiple side effects
# debugging becomes difficult
# Readability matters more than clever code.