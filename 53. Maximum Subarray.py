#----------------------DP:局部最优和全局最优解法---------------------
class Solution:
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums == None or len(nums)== 0: return 0
        global_max =nums[0]
        local_max = nums[0]
        for i in range(1,len(nums)):
            local_max = max(nums[i],local_max+nums[i])
            global_max = max(global_max,local_max)
        return global_max
        
        这是一道非常经典的动态规划的题目，用到的思路我们在别的动态规划题目中也很常用，以后我们称为”局部最优和全局最优解法“。
基本思路是这样的，在每一步，我们维护两个变量，一个是全局最优，就是到当前元素为止最优的解是，一个是局部最优，就是必须包含当前元素的最优的解。接下来说说动态规划的递推式（这是动态规划最重要的步骤，递归式出来了，基本上代码框架也就出来了）。假设我们已知第i步的global[i]（全局最优）和local[i]（局部最优），那么第i+1步的表达式是：
local[i+1]=Math.max(A[i], local[i]+A[i])，就是局部最优是一定要包含当前元素，所以不然就是上一步的局部最优local[i]+当前元素A[i]（因为local[i]一定包含第i个元素，所以不违反条件），但是如果local[i]是负的，那么加上他就不如不需要的，所以不然就是直接用A[i]；
global[i+1]=Math(local[i+1],global[i])，有了当前一步的局部最优，那么全局最优就是当前的局部最优或者还是原来的全局最优（所有情况都会被涵盖进来，因为最优的解如果不包含当前元素，那么前面会被维护在全局最优里面，如果包含当前元素，那么就是这个局部最优）。

接下来我们分析一下复杂度，时间上只需要扫描一次数组，所以时间复杂度是O(n)。空间上我们可以看出表达式中只需要用到上一步local[i]和global[i]就可以得到下一步的结果，所以我们在实现中可以用一个变量来迭代这个结果，不需要是一个数组，也就是如程序中实现的那样，所以空间复杂度是两个变量（local和global），即O(2)=O(1)。
class Solution:
    def maxSubArray(self, nums):
        
        n = len(nums)
        if n == 1 : return nums[0]
        
        local_sum = [nums[0]] + [0]*(n-1)
        global_sum = [nums[0]] + [0]*(n-1)
        
        
        for i in range(n-1):
            
            local_sum[i+1] = max(local_sum[i]+nums[i+1], nums[i+1])  ##local_sum是指以i+1作为结尾的序列的最大和
            
            global_sum[i+1] = max(global_sum[i],local_sum[i+1])  ## 序列长度为i+1的数组的最大和
            
        return global_sum[n-1]
    
    
# 发现我写的很复杂，但是这个必须自己理清楚思路，做的题没什么用，需要认真研究每道题的思路和所用的算法
# 实际上说是使用了Kadane算法解决最大子序列和的问题，实际上调用了两个迭代的dp算法
# 有个特点 这个序列肯定是以正数开头，正数结尾（除去全是负数的情况）？？？？

## 首先分析 我们要求的是长度为n的数组的最大序列和，这个问题可以分解为长度为i的数组的序列最大和的问题，在后面插入一个数后变成
## 长度为i+1的序列最大和问题
## 则maxsum(i+1) = 这个最大序列以i+1为结尾 || 不以i+1作为结尾 ==（maxsum（i））
## 这个最大序列以i+1为结尾（肯定有i+1这个数，这个数肯定是正数） == 这个序列的前缀是以i结尾 （加上i+1这个数）|| 不以i结尾（因为是连续的区间，所以只能是单独一个数了）
## 这个问题比较简单 解决的区间是连续的  还没找到不用连续的题目 找到再加      
        
