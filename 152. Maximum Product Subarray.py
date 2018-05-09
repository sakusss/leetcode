class Solution:
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums == None or len(nums)==0:return 0
        local_max = nums[0]
        global_max = nums[0]
        local_min = nums[0]
        for i in range(1,len(nums)):
            max_copy = local_max
            local_max = max(max(local_max*nums[i],nums[i]),local_min*nums[i])
            local_min = min(min(max_copy*nums[i],nums[i]),local_min*nums[i])
            global_max = max(global_max,local_max)
        return global_max
        
        这道题跟Maximum Subarray模型上和思路上都比较类似，还是用一维动态规划中的“局部最优和全局最优法”。这里的区别是维护一个局部最优不足以求得后面的全局最优，这是由于乘法的性质不像加法那样，累加结果只要是正的一定是递增，乘法中有可能现在看起来小的一个负数，后面跟另一个负数相乘就会得到最大的乘积。不过事实上也没有麻烦很多，我们只需要在维护一个局部最大的同时，在维护一个局部最小，这样如果下一个元素遇到负数时，就有可能与这个最小相乘得到当前最大的乘积和，这也是利用乘法的性质得到的。
        这道题是一道很不错的面试题目，因为Maximum Subarray这道题过于常见了，所以可能大部分人都做过，这道题模型类似，但是又有一些新的考点，而且总体还是比较简单，无论是思路上还是实现上，又能考察动态规划
