def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

num = int(input("Enter a number For Fibonacci:"))
print("Fibonacci Series:")
for i in range(num):
    result = fibonacci(i)
    print(result, end=" ")
