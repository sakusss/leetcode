# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        res = []
        queue = [root]
        index = -1
        
        while queue :
            
            temp = []
            
            index += 1
            
            for node in queue:
                
                queue = queue[1:]
                
                temp.append(node.val) if node else None
            
                queue += [node.left,node.right] if node else []
                
            if index%2 == 1:
                
                temp.reverse()
          
            res.append(temp) if temp else None
            
            #res.append(temp) if (index%2==0) else res.append(temp.reverse())
            
        return res

                

### 加了一个index就可以解决的问题，不要忘记思考，现在信息过于爆炸，信息得来太过容易，所以不要坐享其成 
            
            
            
            
        
        
        
