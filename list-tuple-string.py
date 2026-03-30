# Tuple Value Change using Typecasting
tup = (3, 4, 5)
print("Original Tuple:", tup)
li = list(tup)
li[0] = "Lets Learn"
li[1] = "PYTHON"
li[2] = "Coding"
print("Modified List:", li)
tup = tuple(li)
print("Again converted into tuple:", tup)
print("Type:", type(tup))

# Tuple Value Change using Concatenation
new_tup = (12,) + tup[1:]
print("Tuple after concatenation:", new_tup)

# List Slicing Operations
li = [2, 4, 3, 10, 25, 45, 17, 20, 30, 80]
print("Full List:", li[0:])
print("Slicing [1:9:2]:", li[1:9:2])
print("Third element from end:", li[-3])
print("Reverse Printing:", li[::-1])

# String Operations and Immutability
st = "Snehashis pal"
greeting = "Hello, " + st
print(greeting)

# Correct way to modify string
st = "S" + st[1:]
print("Modified String:", st)

# Palindrome Check
word1 = "racecar"
word2 = "Snehashis"
print("Is racecar palindrome?", word1 == word1[::-1])
print("Is Snehashis palindrome?", word2 == word2[::-1])
