def fibonacci_recursive_method(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci_recursive_method(n-1) + fibonacci_recursive_method(n-2)
    
num = int(input("enter number: "))
for i in range(num):
    print(fibonacci_recursive_method(i), end=' ')
    