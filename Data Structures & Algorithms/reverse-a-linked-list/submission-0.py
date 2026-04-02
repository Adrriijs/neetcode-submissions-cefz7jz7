# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head

        while curr != None:
            holder = prev # 3 points swap
            prev = curr
            tmp = curr.next
            prev.next = holder
            curr = tmp

        return prev