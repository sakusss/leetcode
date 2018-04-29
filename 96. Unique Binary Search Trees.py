# 这道题求二叉查找树的数量，二叉查找树可以任意取根，只要满足中序遍历有序即可
# 从处理子问题的角度上来看，选取一个结点为根，就把结点切成左右子树，以这个结点为根的可行二叉树就是左右
# 子树可行二叉树数量的乘积，所以总的数量就是将以所有结点为根的可行结果累加起来。
# 表达式为 卡特兰数 dp[n]=dp[0]*dp[n-1]+...+dp[n-1]*dp[0]

class Solution:
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp= [1,1]
        dp += [0 for i in range(n-1)]
        for i in range(2,n+1):
            for j in range(i):
                dp[i] += dp[j]*dp[i-j-1]
        return dp[n]
     
  class Solution:
    # @return an integer
    def numTrees(self, n):
        dp = [1, 1, 2]
        if n <= 2:
            return dp[n]
        else:
            dp += [0 for i in range(n-2)]
            for i in range(3, n + 1):
                for j in range(1, i+1):
                    dp[i] += dp[j-1] * dp[i-j]
            return dp[n]
            
            
            ##出错的时候注意列表的初始值，在累加的时候
            #这道题的模型正好是卡特兰数的定义。当然这道题还可以用卡特兰数的通项公式来求解，
            这样时间复杂度就可以降低到O(n)。因为比较直接，这里就不列举代码了。
如果是求解所有满足要求的二叉树（而不仅仅是数量）那么时间复杂度是就取决于结果的数量了，
不再是一个多项式的解法了，有兴趣的朋友可以看看Unique Binary Search Trees II。
时间上每次求解i个结点的二叉查找树数量的需要一个i步的循环，总体要求n次，
所以总时间复杂度是O(1+2+...+n)=O(n^2)。
空间上需要一个数组来维护，并且需要前i个的所有信息，所以是O(n)。
