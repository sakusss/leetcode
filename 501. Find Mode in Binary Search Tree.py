# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:        
    def findMode(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root == None: return []
        
        dict  = collections.defaultdict(int)
        
        def inorder(root):
            
            if root:

                inorder(root.left)

                dict[root.val] += 1

                inorder(root.right)
        
        inorder(root)
    
        maxcount = max(dict.values()) 
        
        return [key for key in dict if dict[key] == maxcount ]
        
# 要求不能使用额外空间，所以使用哈希表
# 知识点1： dict  = collections.defaultdict(int)  初始化哈希表的好方法
# 知识点2： 已知values值去找dict的key值，使用遍历算法
# 无关树的遍历，所以采用什么遍历方式都可以
