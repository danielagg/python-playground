# ------ lists

animals = ["Mouse", "Cat", "Cat", "Dog", "Rat"]

print(animals)

# .sort() mutates the list, sorted() creates a new one
print(sorted(animals))
print(sorted(animals, reverse=True))

# set() to remove duplicates
print(sorted(set(animals)))

# inclusive : exclusive --> returns [2, 3] from indices 1 and 2
print([1, 2, 3, 4, 5, 6][1:3])
print([1, 2, 3, 4, 5, 6][:3])  # start from 0, end at index 2
print([1, 2, 3, 4, 5, 6][1:])  # start from 1, end at last entry

print([1, 2, 3, 4, 5, 6, 7, 8][1:6:2])  # start from 1, end at 5, by stepping 2
print([1, 2, 3, 4, 5, 6, 7, 8][::-1])  # reverse the list

print([i + " test" for i in animals])

map(lambda x: print(x + "test"), animals)

test = filter(lambda x: "t" in x, animals)
print(list(test))

# ------ tuples
