# List Copy vs Reference
a = [1, 10, 2]
b = a              # reference variable (same memory)
c = a.copy()       # new list (separate memory)
b.append(3)
c.append(4)
print("Original List =>", a)
print("Copy using '=' =>", b)
print("Using Copy method =>", c)

# Deep Copy (Nested List)
import copy
a = [[1, 2], [3, 4]]
b = copy.deepcopy(a)   # completely new copy
b[0].append(10)
print("Original Nested List:", a)
print("Deep Copied List:", b)

# Reverse Words in String
i = "I am busy right now"
print("Original String:", i)
split_i = i.split()
reversed_i = split_i[::-1]
reverse_join = " ".join(reversed_i)
print("Reversed Words:", reverse_join)

# One line method
print("One-line reverse:", " ".join(i.split()[::-1]))

# List Slicing
a = [2, 5, 4, 10, 1, 5, 3]
print("Slicing [5:1:-1]:", a[5:1:-1])

# Tuple with Mutable Elements
b = ([2, 3], [4, 5, 10])
b[0].append(5)   # allowed
print("After append:", b)

b[0][0] += 1     # allowed
print("After increment:", b)

# Not allowed (tuple is immutable)
# b[0] = [7, 8]   # This will give error

print("Cannot reassign tuple element because tuple is immutable")
