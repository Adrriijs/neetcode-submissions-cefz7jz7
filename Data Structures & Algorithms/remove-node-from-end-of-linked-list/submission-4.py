# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        tail = runner = head
        length = 1

        while tail and tail.next:
            tail = tail.next
            length += 1
        
        run = length - n

        if run == 0:
            return head.next

        for _ in range(run - 1):
            runner = runner.next

        runner.next = runner.next.next

        return head