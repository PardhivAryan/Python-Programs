def fibanocci_series(n):
    fib_series = [0,1]
    for i in range(2, n):
        adding_terms = fib_series[-1] + fib_series[-2] 
        fib_series.append(adding_terms)
    return fib_series[:n]
n = int(input("enter a number: "))
print(fibanocci_series(n))