# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def length(self,head):
        n = 0
        while head:
            head=head.next
            n+=1
        return n
        
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if not head : return  None
        n = self.length(head)
        if k > n:
            k=k%n
    
        dummy = ListNode(0)
        
        dummy.next = head
        
        slow = fast = head
        
        i = 0
        while fast.next:
        
            while i< k : 

                fast = fast.next

                i   += 1

            slow = slow.next 
            
            fast = fast.next
        temp = slow.next 
        # print(slow.next.val)
        
        slow.next = None
        
        fast.next = head
        
        dummy.next = temp
        
        return dummy.next
        
   ------------------------------------------------自己的做法，将链表拆分，然后重组-------------------------------     
   
   # Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if k == 0: return head
        if head == None : return  None

        dummy = ListNode(0)
        
        dummy.next = head
        
        p = dummy   ## 围成一个环
        
        count = 0

        while p.next:
            
            p = p.next
            
            count+=1
        
        p.next = dummy.next
        
        k = count - (k%count)
        
        for i in range(k):
            
            p = p.next
        
        dummy.next = p.next
        
        p.next = None
    
        return dummy.next            
        
        
      #### 围成环就可以解决了比链长的问题
        
