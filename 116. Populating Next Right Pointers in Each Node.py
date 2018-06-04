# Definition for binary tree with next pointer.
# class TreeLinkNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None

class Solution:
    # @param root, a tree link node
    # @return nothing
    def connect(self, root):
        
        if root and root.left:
            '分成几种情况，因为是完全二叉树，所以如果有左子树，肯定有存在右子树'
            '所以左结点的next一定是根节点的右结点'
            '但是右结点有几种情况，需要判断父结点的next是否为空'
            root.left.next = root.right
            
            if root.next :
                
                root.right.next = root.next.left
                
            else:
                
                root.right.next = None
                
            self.connect(root.left)
            self.connect(root.right)  ## 从根结点开始处理，所以遍历在处理后面
            
        
