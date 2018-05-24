# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        a=[]
        while head:
            a.append(head.val)
            head=head.next
        a.sort()
        print(a)
        head = ListNode(0)
        dummy = ListNode(0)
        head.next = dummy
        for i in a:
            dummy.next = ListNode(i)
            dummy=dummy.next
        return head.next.next
        ## 我自己的方法，把值全取到列表中排序，再重建链表
        
        # Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None or head.next == None:
            return head
        slow = fast  = head 
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        head1=slow.next
        head2=head
        slow.next = None
        l1 = self.sortList(head1)
        l2 = self.sortList(head2)
        l = self.merge(l1,l2)
        return l
    def merge(self,l1,l2):
        head = cur= ListNode(0) 
        while l1 and l2: 
            if l1.val > l2.val: 
                cur.next = l2 
                l2 = l2.next 
            else: 
                cur.next = l1 
                l1 = l1.next 
            cur = cur.next 
        cur.next = l1 or l2 
        return head.next
            
        
        
# 时间复杂度是O（nlogn），空间复杂度是O（n）
##  由于链表在归并操作时并不需要像数组的归并操作那样分配一个临时数组空间，所以这样就是常数空间复杂度了，当然这里不考虑递归所产生的系统调用的栈。
