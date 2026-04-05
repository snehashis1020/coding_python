# fact
def factorial(n):
    fact = 1
    for i in range(1, n + 1):
        fact = fact * i
    return fact
print("Factorial:", factorial(5))

# sawp
def swap(a, b):
    temp = a
    a = b
    b = temp
    return a, b
x, y = 5, 10
x, y = swap(x, y)
print("After swap:", x, y)

# Fibonacci 
def fibonacci(n):
    a, b = 0, 1
    for i in range(n):
        print(a, end=" ")
        a, b = b, a + b
num = int(input("Enter number: "))
fibonacci(num)
