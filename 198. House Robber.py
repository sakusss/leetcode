实际上思路是rob[i]表示抢劫第i个房子的最大收益，pass[i]表示不抢第i个房子的最大收益
则状态方程：

rob[i] = nums[i] + pass[i-1]
pass[i] = max(rob[i-1] , pass[i-1])

则有

pass[i] = max(nums[i-1]+ pass[i-2], pass[i-1])

最后的结果是max(n) = max(pass[n],rob[n])


-----------------------
这道题的本质在于在一列数组中取出一个或多个不相邻的数，求其和的最大值
在求最大极值问题时，一般使用动态规划
我们维护一个一位数组dp，其中dp[i]表示到i位置时不相邻数能形成的最大和
在写递推公式时，要从最简单的形式开始想
*其实动态规划啥的第一眼很难想到，大多数情况下我都是先写递归算法，因为从递归算法很就容易推导出所谓的动态规划公式出来，然后再转换成动态规划，再优化空间等。
对于这个问题，可以理解为在任意一个房子的时候，他能所拿到的最多的钱就是max
（偷这个房子=在第n-2个房子的时候钱的最大值+第n个房子的钱，只要第n-1个房子没偷就行），
不偷这个房子（这个时候钱的最大值等于在第n-1个房子时候的钱的最大值，第n-1个房子他偷了还是没偷我们不用关心）.


class Solution:
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0 : return 0
        
        if len(nums) == 1: return nums[0]
        
        dp = [0]*len(nums)
        dp[0] = nums[0]
        dp[1] = max(nums[0],nums[1])
        
        for i in range(2,len(nums)):
            
            dp[i] = max(dp[i-1],dp[i-2]+nums[i])
            
        return dp[-1]
        
        
