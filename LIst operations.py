# 1
my_list = [10, 20, 30, 40, 50]
print("the list is:", my_list)

#  2
fruits = ["apple", "banana", "mango"]
print("first fruit:", fruits[0])
print("third fruit:", fruits[2])

#  3
numbers = [1, 2, 3, 4]
numbers[2] = 10
print("modified list:", numbers)


# 🔹 4
print("4")
numbers = [1, 2, 3]
numbers.append(5)
numbers.remove(2)
print("updated list:", numbers)

# 6
list1 = [5, 10, 15, 20]
list2 = list1[:]   # copy using slicing
print("original list:", list1)
print("copied list:", list2)

#  7
list1 = [5, 10, 15, 20]
list2 = list(list1)   # copy using constructor
print("original list:", list1)
print("copied list:", list2)
