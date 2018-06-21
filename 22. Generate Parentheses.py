class Solution:
    
    def dfs(self,left,right,temp,res):
        
        if left > right : return 
        
        if left == 0 and right == 0:
            
            res.append(temp)
            
        if left > 0 :
            
            self.dfs(left-1,right,temp+"(",res)
            
        if right > 0 :
            
            self.dfs(left,right-1,temp+")",res)
        
        
    
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        res = []
        
        self.dfs(n, n, "",res)
        
        return res
        
        ## 使用了回溯法，还是需要多多分析一下，因为在没有加结束条件之前，返回值是空值，明天分析一下
        
