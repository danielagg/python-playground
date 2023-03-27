animals = ["Mouse", "Cat", "Cat", "Dog"]

print(animals)

# .sort() mutates the list, sorted() creates a new one
print(sorted(animals))
print(sorted(animals, reverse=True))

# set() to remove duplicates
print(sorted(set(animals)))
