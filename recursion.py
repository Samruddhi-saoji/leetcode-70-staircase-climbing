#link: https://leetcode.com/problems/climbing-stairs/

#jumps = [1,2]
#total number of ways to go from stair 0 to stair n
def ways_to_go(n) -> int:
    #for 3 stairs or less
    if n<=3 : return n

    #taking a jump while at stair "src"
    def go(src, jump, ways):
        dest = src + jump
        
        if dest==n : #desired destination
            return ways+1
        if dest > n : #overshot
            return ways+0
            
        #from this stair, we can take a jump of 1 or 2
        ways = go(dest, 1, ways)
        ways = go(dest, 2, ways)
           
        return ways
        
    ways = go(0,0, 0)  #initial call, so jump=0
    return ways
    