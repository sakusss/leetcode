class Solution:
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp =[1 for i in range(n+1)]
        for i in range(2,n+1):
            dp[i]=dp[i-1]+dp[i-2]
        return dp[n]
        
        ##复杂度为O(N)
        ##利用斐波那契的通项公式有O（logn）的解法，利用分治法
