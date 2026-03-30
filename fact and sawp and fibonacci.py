# fact
def factorial(n):
    fact = 1
    for i in range(1, n + 1):
        fact = fact * i
    return fact
print("Factorial:", factorial(5))

# sawp
a = 5
b = 10
temp = a
a = b
b = temp
print(a, b)

# Fibonacci 
n = int(input())
a, b = 0, 1
for i in range(n):
    print(a, end=" ")
    a, b = b, a + b
