# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    # def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
    def mergeTwoLists(self, l1, l2):
        pseudoNode = ListNode()
        ptr = pseudoNode
        while l1 is not None and l2 is not None:
            if l1.val < l2.val:
                ptr.next = l1
                l1 = l1.next
            else:
                ptr.next = l2
                l2 = l2.next
            ptr = ptr.next
        if l1 is not None:
            ptr.next = l1
        if l2 is not None:
            ptr.next = l2
        return pseudoNode.next
