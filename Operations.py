numbers = []
n = int(input("How many numbers do you want to enter: "))
for i in range(n):
    num = int(input(f"enter numbers {i + 1}:"))
    numbers.append(num)
print(f"The original list of numbers are {numbers}")
# Sort Operation
numbers.sort()
print(f"After Sorting the numbers are {numbers}")
# Reverse Operation
numbers.reverse()
print(f"After reversing of all  numbers are {numbers} ")
# Remove Operation
remove_num = int(input("enter a number: "))
if remove_num in numbers:
    numbers.remove(remove_num)
    print(f"After removing {remove_num} the list are {numbers}")
else:
    print(f"{remove_num} not in {numbers}")
# POP Operation
popped_num = numbers.pop()
print(f"After the popping the number {popped_num} the list are : {numbers}")
# Tuple Example - Tuples are Immutable
tuple(numbers)
print(f"The Tuple Elements are :{tuple(numbers)}")
# Set Operations - In Sets we can remove duplicate elements
set(numbers)
print(f"The Set elements are{set(numbers)}")

