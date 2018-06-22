class Solution:
    def dfs(self,candidates,target,start,temp):
        
        if target == 0:
            
            Solution.res.append(temp)
            
        else:
            
            for i in range(start,len(candidates)):
                
                if target >= candidates[i]:
                    
                    self.dfs(candidates,target-candidates[i],i,temp+[candidates[i]])
                    
                else:
                    
                    break
            
    
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates.sort()
        
        Solution.res = []
        
        self.dfs(candidates,target,0,[])
        
        return Solution.res
        
  ## 需要注意的点有两个，一个是res需要设置成class中的全局变量，在两个函数中比较好操作和传递
  ## 第二个就是递归的思路还是不清楚
