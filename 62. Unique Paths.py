class Solution:
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        dp = [[0 for i in range(m)] for j in range(n)]
        
        dp[0][0] = 1
        
        for i in range(m):
            
            dp[0][i] =1
            
        for j in range(n):
            
            dp[j][0] =1
            
        for i in range(1,m):
            
            for j in range(1,n):
                
                dp[j][i] = dp[j-1][i] + dp[j][i-1]
                
        return dp[n-1][m-1]
        
        
        ## dp问题 时间复杂度是O(MN)
        ## 空间复杂度
        
    public int uniquePaths(int m, int n) {  
    if(m<=0 || n<=0)  
        return 0;  
    int[] res = new int[n];  
    res[0] = 1;  
    for(int i=0;i<m;i++)  
    {  
        for(int j=1;j<n;j++)  
        {  
           res[j] += res[j-1];  
        }  
    }  
    return res[n-1];  
}  
        
