# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res =[]
        self.recursive_preorder(root,res)
        return res
    def iterative_preorder(self,root,res):
        stack = []
        while root or stack:
            if root :
                res.append(root.val)
                stack.append(root)
                root = root.left
            else:
                root = stack.pop()
                root = root.right
        return res
        
    def recursive_preorder(self,root,res):
        if root:
            res.append(root.val)
            self.recursive_preorder(root.left,res)
            self.recursive_preorder(root.right,res)
        
    
