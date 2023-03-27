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

test = filter(lambda x: "t" in x.lower(), animals)
print(list(test))

# ------ tuples (immutable) --> can't do firstTuple[0] = "Daniel"

firstTuple = ("Dan", 27, "La Coruna")
secondTuple = tuple(["Item1", 2, True])

name, age, city = firstTuple
print(city)

print(secondTuple)
print(secondTuple[0])
print(secondTuple[-1])  # last item
print(secondTuple[-2])  # 2nd to last item
print(secondTuple[::-1])  # same idea, reverse

my_tuple = tuple([1, 2, 3, 4, 5, 6, 2])
for i in range(0, len(my_tuple), 2):  # step 2
    print(my_tuple[i])  # 1, 3, 5, 2

if 3 in my_tuple:
    print("in it!")
else:
    print("nope!")

print(f"3 appears {tuple([1, 1, 2, 3, 3, 3, 3, 4]).count(3)} times in the tuple")

print(my_tuple.index(2))
print(list(reversed(my_tuple)).index(2))

test = (0, 1, 2, 3, 4, 5, 6)
t1, *t2, t3 = test
print(f"t1 is {t1}, t2 is {t2} and t3 is {t3}")
