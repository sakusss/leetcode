class Solution:
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums) == 0: return []
        
        if len(nums) == 1: return [nums]
        
        
        dp = []
        
        for i in range(len(nums)):
            
            for j in self.permute(nums[:i]+nums[i+1:]):
                
                dp.append([nums[i]]+j)

        
        return dp
            
            
        
