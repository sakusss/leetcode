class Solution:
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        # dict = {}
        from collections import defaultdict
        
        ##为了避免不在dict中的key值返回keyerror
        
        dict = defaultdict(list)
        
        ## 用一种类型作为初始值 如果没有这个key调用时就返回[]
        
        for word in strs:
           
            sortedword  = ''.join(sorted(word))
            
            # dict[sortedword] = [word] if sortedword not in dict else dict[sortedword]+[word]
            dict[sortedword].append(word)
        
        return [dict[key] for key in dict]
#         res = []
            
#         for key in dict:
            
#             res.append(dict[key])
            
#         return res

#tag :hashtable
                
            
        
        
        
            
                
                
            
        
        
        
