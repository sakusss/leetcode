class Solution:
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        n = len(strs)
        res = []
        
        for i in range(n):
            
            for j in strs[:i]+strs[i+1:] :
                
                temp = []
                
                if sorted(strs[i]) == sorted(j) :
                    
                    temp += [strs[i],j]
                    # print(temp)
                    
                    strs.remove(j)
            print(strs)
                    
            strs.remove(strs[i])
                    
            res.append(temp)
        
        return res
            
                
                
            
        
        
        
