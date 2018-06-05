class Solution:
    def generate(self, n):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if n == 0: return []
        if n == 1: return [[1]]
        if n == 2: return [[1],[1,1]]
        if n > 2:
            list = [[] for i in range(n)]
            for i in range(n):
                list[i] = [1 for j in range(i+1)]
            for i in range(2,n):
                for j in range(1,i):
                    list[i][j] = list[i-1][j-1]+list[i-1][j]
        return list
        
        ## 杨辉三角的构造，主要学习list的初始化构造
