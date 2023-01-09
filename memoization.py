#link: https://leetcode.com/problems/climbing-stairs/
import numpy as np

#jumps = [1,2]
#total number of ways to go from stair 0 to stair n
def climbStairs(n) -> int:
    #for 3 stairs or less
    if n<=3 : return n

    #array for storing cache
    cache = np.zeros(n+1)
    #cache[i] = number of ways to go from stair i to stair n
    #0 intiailly

    cache[n] = 1
    cache[n-1] = 1
    #always true

    #taking a jump while at stair "src"
    def go(src, jump, ways):
        dest = src + jump
        
        if dest==n : #we have reached our desire destination
            return ways+1
        if dest > n : #overshot
            return ways+0

        #if we have already found the number of ways to go to stair n from dest
        if cache[dest] != 0 :
            return ways + cache[dest]
            
        #from this stair, we can take a jump of 1 or 2
        ways = go(dest, 1, ways)
        ways = go(dest, 2, ways)
           
        #we have now found the tot ways to go from stair "dest" to stair n
        cache[dest] = ways

        return ways
        
    ways = go(0,0, 0)  #initial call, so jump=0
    return ways
    