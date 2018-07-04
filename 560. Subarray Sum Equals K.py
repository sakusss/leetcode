class Solution:
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        if len(nums) == 0 :return 0
        if len(nums) == 1 and k!= nums[0]: return 0
        dp = [0]+ [sum(nums[:i+1]) for i in range(len(nums))]
        
        print(dp)
        
        res = 0
        
        for i in range(len(dp)):
            
            for j in range(i+1,len(dp)):
            
                if (dp[j]-dp[i] == k):
                
                    res += 1
                    print(res)
                    print(dp[i],dp[j])

                    
        return res
        
        我的想法，暴力解法，把一段一段的和都求出来，两者之间的差如果是k，则subarray就是i，j之间的序列。
        但是出现了TLE的问题。
        
        
        
 
