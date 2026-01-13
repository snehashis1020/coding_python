def fibonacci(n):
    a, b = 0, 1
    for i in range(n):
        print(a, end=" ")
        c = a + b
        a = b
        b = c    
    print()
fibonacci(5)
