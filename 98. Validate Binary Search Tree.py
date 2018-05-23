# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return self.dfs(root,-float('inf'),float('inf'))
    def dfs(self,root,minint,maxint):
        if root == None:return True
        elif root.val <= minint or root.val >= maxint:
            return False
        else:
            return self.dfs(root.left,minint,root.val) and self.dfs(root.right
                                                                    ,root.val,maxint)
        ## 就是一个递归，注意python3 没有对整数大小的限制了 用float('inf')来表示最大值
        ## 注意特殊情况，就是只有左右子树的情况
