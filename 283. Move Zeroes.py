class Solution:
    def moveZeroes(self, nums):
        
        for i in range(len(nums)):
            
            if nums[i] == 0 :
                
                for j in range(i+1,len(nums)):
                    
                    if nums[j] != 0 :
                        
                        nums[i],nums[j] = nums[j], nums[i]
                        
                        break
                        
        我的思路很简单，就是将零和后面第一个不为零的数进行交换
        时间复杂度应该是线性的
