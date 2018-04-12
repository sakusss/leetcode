# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        dummy = ListNode(0);dummy.next = head
        p1 = p2 =dummy
        for i in range(n):
            p1=p1.next
        while p1.next :
            p1=p1.next
            p2=p2.next
        p2.next = p2.next.next
        return dummy.next
        
   ##使用双指针，确定要删除的节点位置
   ##增加一个头结点
   ## 时间复杂度 O（n），空间复杂度O(1)
