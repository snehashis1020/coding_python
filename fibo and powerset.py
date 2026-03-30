def fibonacci_series(n, a=0, b=1):
    if n <= 0:
        return
    print(a, end=" ")
    fibonacci_series(n - 1, b, a + b)

num = int(input("Enter the number of series : "))

if num <= 0:
    print("Please enter a positive integer.")
else:
    print("Fibonacci Series:")
    fibonacci_series(num)

def power_set(s):
    
    if len(s) == 0:
        return [[]]
    
    first = s[0]
    rest_power_set = power_set(s[1:])
    
    new_subsets = []
    for subset in rest_power_set:
        new_subsets.append([first] + subset)
    
    return rest_power_set + new_subsets
 
elements = input("Enter elements separated by space: ").split()

result = power_set(elements)

print("Power Set:")
for subset in result:
    print(subset)
