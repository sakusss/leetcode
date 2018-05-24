# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def dfs(self,root,currsum,temp,res):
        if root == None: return None
        if root.left == None and root.right == None and currsum == root.val:
            res.append(temp+[root.val])
            return 
        
        self.dfs(root.left,currsum-root.val,temp+[root.val],res)
        self.dfs(root.right,currsum-root.val,temp+[root.val],res)
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        res =[]
        self.dfs(root,sum,[],res)
        return res
