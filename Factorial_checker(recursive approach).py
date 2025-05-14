def factorial_recursive(n):
    if n == 0 or n == 1:
        return 1
    elif n < 0:
        return "factorial for negative numbers isn't possible"
    else:
        return n * factorial_recursive(n-1)
    
num = int(input("Enter Number: "))
print(f"The Factorial for {num} is :{factorial_recursive(num)}")


