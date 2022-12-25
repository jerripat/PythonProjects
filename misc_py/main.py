
# Iterative factorial
def iterative_factorial(n):
    fact = 1
    for i in range(2, n+1):
        fact *= i
    return fact
    

print(iterative_factorial(5))

# Recursion factorial
def recur_factorial(n):
    if n == 1:
        return n
    else:
        temp = recur_factorial(n - 1)
        temp = temp * n
    return temp

print(recur_factorial(5))  

# Premutations


        
        
    