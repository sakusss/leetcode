class Solution(object):    
    def twosum(self,s,target):
        dict = {}
        a = []
        for k,v in enumerate(s):
            if dict.get(target-v,None) == None:
                dict[s[k]]=k
            else:
                a.append([v,target-v])
            return a
        
        
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        a=[]
        if len(nums) == 1:
            if nums ==[0]:return [[0]]
            else:return None
        else:
            for k,v in enumerate(nums): 
                nums.remove(v)
                a.append(self.twosum(nums,-v))
                for i in range(len(a)):
                    a[i].append(v)
            return a
            
