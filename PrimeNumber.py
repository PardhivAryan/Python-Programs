def prime(n):
    if n <= 1:
        print('not defined')
        return False
    elif n == 2:
        print('Prime Number')
        return True
    elif n % 2 == 0:
        print('Composite Number')
        return False
    
    for i in range(3, int(n ** 0.5)+ 1, 2):
        #2 is already a prime number so if we take a number(29) (29 ** 0.5=5.38(or)5) 5+1=6 so i in range(3,6,2)
        #which means(start,stop,step) if we take 29 it is divisible 3 and 5. 6 means it exceeds limit 
        #it dont divide by four because the step is 2 so it jumps two numbers in range(3,6,2) which means 29 not 
        #divided by 3 and 5
        if n%i==0: # means it checks 29 % with 3 and 5 == 0
            print('not prime')
            return False
    return True
    
n = int(input("enter number: "))
if prime(n):
    print(f"{n} is Prime number")
else:
    print(f"{n} is Composite number")