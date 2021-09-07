# You are climbing a staircase. It takes n steps to reach the top.

# Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

# Input: n = 2
# Output: 2
# Explanation: There are two ways to climb to the top.
# 1. 1 step + 1 step
# 2. 2 steps

# fibonacci approach

class Solution:
    def climbStairs(self, n: int) -> int:
        if (n == 1):
            return 1
        
        f = [1,2]

        for i in range(2, n):
            step = f[0] + f[1]
            f[0] = f[1] 
            f[1] = step
            
        return f[1]