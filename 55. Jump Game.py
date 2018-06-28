首先说一下我的错误想法，使用dp算法，想法是一步一步走肯定能走到，但是只有52/75通过，【2，0，0】这种无法通过。
class Solution:
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        n = len(nums)
        dp = [True for i in range(n)]
        
        for i in range(n-1):
            
            dp[i+1] = dp[i] and (nums[i] >= 1)
            
        return dp[n-1]
           
discuess上的一种解法，

找到从后往前数，能到达最后点的最小的index，时间复杂度事o(n)
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        n = len(nums) - 1
        last = n
        
        for i in range(n, -1, -1):
            
            if i + nums[i] >= last : last = i
                
        return last == 0
                
            
        
        
