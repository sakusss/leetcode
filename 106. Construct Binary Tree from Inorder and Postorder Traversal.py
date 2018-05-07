class Solution:
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        if len(inorder) == 0:return None
        if len(inorder) == 1: return TreeNode(inorder[0])
        root = TreeNode(postorder[len(postorder)-1])
        index = inorder.index(postorder[len(postorder)-1])
        root.left =self.buildTree(inorder[:index],postorder[:index])
        root.right = self.buildTree(inorder[index+1:len(inorder) ],postorder[index:len(postorder)-1])
        return root
        
        题意：根据二叉树的中序遍历和后序遍历恢复二叉树。

解题思路：看到树首先想到要用递归来解题。以这道题为例：如果一颗二叉树为{1,2,3,4,5,6,7}，则中序遍历为{4,2,5,1,6,3,7}，后序遍历为{4,5,2,6,7,3,1}，我们可以反推回去。由于后序遍历的最后一个节点就是树的根。也就是root=1，然后我们在中序遍历中搜索1，可以看到中序遍历的第四个数是1，也就是root。根据中序遍历的定义，1左边的数{4,2,5}就是左子树的中序遍历，1右边的数{6,3,7}就是右子树的中序遍历。而对于后序遍历来讲，一定是先后序遍历完左子树，再后序遍历完右子树，最后遍历根。于是可以推出：{4,5,2}就是左子树的后序遍历，{6,3,7}就是右子树的后序遍历。而我们已经知道{4,2,5}就是左子树的中序遍历，{6,3,7}就是右子树的中序遍历。再进行递归就可以解决问题了。
，自然时间复杂度和空间复杂度也还是O(n)。代码如下：
这道题和Construct Binary Tree from Preorder and Inorder Traversal是树中难度比较大的题目了，有朋友可能会想根据先序遍历和后序遍历能不能重新构造出树来，答案是否定的。只有中序便利可以根据根的位置切开左右子树，其他两种遍历都不能做到，其实先序遍历和后序遍历是不能唯一确定一棵树的，会有歧义发生，也就是两棵不同的树可以有相同的先序遍历和后序遍历，有兴趣的朋友可以试试举出这种例子哈。
