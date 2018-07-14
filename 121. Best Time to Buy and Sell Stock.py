这道题实际上将其转化为，日收益的最大子序列和的问题，借用53题的fuc，但是有一点不同的是，最大收益必须是正的或者0，这是实际情况约束的
时间复杂度是 o(n)

class Solution:
    def maximum_subarray(self,nums):
        
        if nums == None or len(nums) == 0 : return 0
        
        global_sum = nums[0]
        local_sum = nums[0]
        
        for i in range(1,len(nums)):
            
            local_sum = max(local_sum + nums[i], nums[i])
            
            global_sum = max(global_sum , local_sum)
            
        return max(0,global_sum)
        
        
    def maxProfit(self, prices):
        
        new_prices = [0] + prices[:-1]
        margin = [prices[i] - new_prices[i] for i in range(len(prices))]
        print(margin)
        
        return self.maximum_subarray(margin[1:])
