class Solution:
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l=0;r=len(nums)-1
        while l< r and nums[l]>nums[r]:
            m = (l+r)//2
            if nums[m] >nums[r]:
                l = m+1
            else:
                r = m
        return nums[l]
        
   二分查找 时间复杂度O（logn）
   用于 数组且排好序
