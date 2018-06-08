class Solution:
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        k = small_list = ListNode(0)
        m = large_list = ListNode(0)
        p = head
        while p :
            if p.val < x :
                k.next = p
                # p = p.next
                k = k.next
                # k.next = None
            else:
                m.next = p
                # p = p.next
                m = m.next
                # m.next = None
            p = p.next
        m.next = None
        k.next = large_list.next
        return small_list.next   
        
        
        ######最后，把小链表接在大链表上，别忘了把大链表的结尾赋成null!!!!!!!!!!
        ######就是这个出的错
        
