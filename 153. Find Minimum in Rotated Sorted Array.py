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
        
        # 这道题是Search in Rotated Sorted Array的扩展，区别就是现在不是找一个目标值了，而是在bst中找最小的元素。
        # 主要思路还是跟Search in Rotated Sorted Array差不多，还是通过左边界和中间的大小关系来得到左边或者右边有序的信息，如果左半边有序，
        # 那么左半边最小就是左边第一个元素，可以和当前最小相比取小的，然后走向右半边。否则，那么就是右半半边第一个元素，然后走向左半边。
        # 这样子每次可以截掉一半元素，所以最后复杂度等价于一个二分查找，是O(logn)，空间上只有四个变量维护二分和结果，所以是O(1)。
