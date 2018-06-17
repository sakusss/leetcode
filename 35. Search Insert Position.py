class Solution:
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        n = len(nums)-1
        left = 0 
        right = len(nums)-1
        
        while left <= right:
            
            mid = (left+right) //2
            # print(mid)
            
            if target > nums[mid]:
                
                left = mid + 1
                
            else:
                
                right = mid - 1
        
        return left if left <= n else n+1
