class Solution:
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums) == 0: return []
        if len(nums) == 1: return [nums]
        
        res = []
        
        for i in range(len(nums)):
            
            for j in self.permuteUnique(nums[:i]+nums[i+1:]):
                
                if [nums[i]]+j in res:
                
                    pass
                
                else:
                    
                    res.append([nums[i]]+j)
            
        return res
        
      ## 学会如何判断list中有某个元素 if a in list: pass
        
