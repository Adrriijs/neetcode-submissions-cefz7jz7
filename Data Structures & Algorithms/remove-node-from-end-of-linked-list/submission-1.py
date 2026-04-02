# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        max_l = 0
        cur = head
        while cur: # get the len of linkedlist (counting nodes)
            max_l += 1
            cur = cur.next

        if max_l - n == 0:
            return head.next
        
        cur = head
        for i in range(max_l - 1):
            if (i + 1) == max_l - n:
                cur.next = cur.next.next
                break
            cur = cur.next
        return head
