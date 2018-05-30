class Solution:
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m  = len(grid)
        n = len(grid[0])
        if m == 0 or n == 0:return None
        if m == 1 and n == 1:return grid[0][0]
        dp=[[0 for i in range(n)] for j in range(m)]
        dp[0][0] = grid[0][0]
        for i in range(m):
            for j in range(n):
                if i-1 <0:
                    dp[i][j] = grid[i][j] + dp[i][j-1] 
                elif j-1 <0:
                    dp[i][j] = grid[i][j] + dp[i-1][j]
                else:
                    dp[i][j] = grid[i][j] + min(dp[i-1][j],dp[i][j-1])
                
        return dp[m-1][n-1]
        
      ### 动态规划 找出递归函数  注意边界条件  而这个当前最短路径可以取前面一格和上面一格中小的最短路径长度得到，因此递推式是res[i][j]=min(res[i-1][j], res[i][j-1])+grid[i][j]。总共进行两层循环，时间复杂度是O(m*n)。而空间复杂度仍是使用Unique Paths中的方法来省去一维，是O(m)
      ### 最简单的动态规划问题
      
     class Solution:
    # @param grid, a list of lists of integers
    # @return an integer
    def minPathSum(self, grid):
        m = len(grid); n = len(grid[0])
        dp = [[0 for i in range(n)] for j in range(m)]
        dp[0][0] = grid[0][0]
        for i in range(1, n):
            dp[0][i] = dp[0][i-1] + grid[0][i]
        for i in range(1, m):
            dp[i][0] = dp[i-1][0] + grid[i][0]
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + grid[i][j]
        return dp[m-1][n-1]
