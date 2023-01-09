import numpy as np

def ways_to_go(n):
    return fibonacci(n+1)


#space optimised tabulation
#1, 1, 2, 3, 5, 8, 13.........
def fibonacci(n):
    if n==0 or n==1: return n
        
    prev1 = 0  #f(0) = 0 
    prev2 = 1  #f(1) = 1
    #f(n) = f(n-1) + f(n-2)

    for i in range(2, n+1):
        current = prev1 + prev2

        #move prev1, prev2 pointers forward
        prev1 = prev2
        prev2 = current

    return current