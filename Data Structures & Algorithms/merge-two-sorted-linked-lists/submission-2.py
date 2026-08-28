# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        """
        1 2 4 6 7 8
        1 3 5

        1 1 2 3 4 5 6 7 8 -> check which one is smaller
        """

        dummy = ListNode()
        curr = dummy
        head1, head2 = list1, list2

        while head1 and head2:
            if head1.val < head2.val:
                curr.next = head1
                head1 = head1.next
            elif head1.val >= head2.val:
                curr.next = head2
                head2 = head2.next

            curr = curr.next
        
        if head1:
            curr.next = head1
        else:
            curr.next = head2
        
        return dummy.next
