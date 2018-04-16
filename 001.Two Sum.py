class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: (int)
        :rtype: List[int]
        """
        dict = {}
        for k,v in enumerate(nums):
            if dict.get(target-v,None) == None:
                dict[nums[k]] = k
            else:
                return [k,dict[target-v]]
            
            
## 利用hash table 将value:key 存入hash table中，从pyhton字典中取字，无论长度多少，其
时间空间复杂度都是O(1)
## 则hash table 的时间空间复杂度都为O(n)
