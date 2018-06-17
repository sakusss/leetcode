class Solution:
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        res = [-1]*2
        left = 0  
        right = len(nums)-1

        while left <= right:
            
            mid = (left+right)//2
            
            if target > nums[mid]:
                
                left = mid + 1
            
            elif target < nums[mid]:
                
                right = mid - 1 
                
            else:
                if nums[right] == target: res[1] = right
                if nums[left] == target: res[0] = left
                
                for i in range(mid+1,right+1):
                    
                    if nums[i] != target : res[1] = i-1;break
                        
                for j in range(mid,left-1,-1):
                    
                    if nums[j] != target: res[0] = j+1;break
                
                return res
                
        return res
                
            
        
