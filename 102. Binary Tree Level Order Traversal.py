#使用深度优先搜索，节点深度与输出结果数组的下标对应，注意在递归时要保存每次访问的结点

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
#         res=[]
#         queue =[]
#         level=0
#         if root ==  None: return None
#         queue.append(root)
#         while queue :
#             res.append([])
#             t = queue.pop(0)
#             res[level].append(t.val)
#             if t.left!= None :
#                 queue.append(t.left)
#             if t.right!=None :
#                 queue.append(t.right)
#             level +=1
                
#         return res
        ## 怎么放到一个格子里？？？
        res = []
        queue = [root]
        
        while queue:
        
            temp = []
            
            for node in queue:
                
                queue = queue[1:]
                
                temp.append(node.val) if node else None
                
                queue += [node.left, node.right] if node else []
                
            res.append(temp) if temp else None
            
        return res
      
      ## 使用队列，进行广度优先搜索，先进先出，时间复杂度使树的节点数 O（n）,空间复杂度是一层的节点数，也是O（n）
      ## 先确定使用广度优先搜索，然后根据题目条件，应该是先进先出的遍历方式，所以使用队列的数据结构。
            
