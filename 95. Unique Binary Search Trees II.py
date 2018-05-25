# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def helper(self,min,max):
        res =[]
        if min > max :  return [None]
        # if min == max:  return [TreeNode(min)]
        #res =[]
        for val in range(min,max+1):
            lefttree = self.helper(min,val-1)
            righttree = self.helper(val+1,max)
            for i in lefttree:
                for j in righttree:
                    root = TreeNode(val)
                    root.left = i
                    root.right = j
                    res.append(root)
        return res
        
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        return self.helper(1,n)
    
        
