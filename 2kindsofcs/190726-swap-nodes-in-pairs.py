# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if not head:
            return None
        node = head
        while node.next:
            tempVal = node.val
            node.val = node.next.val
            node.next.val = tempVal
            if node.next.next:
                node = node.next.next
                continue
            else:
                break
        return head
        
# Runtime: 56 ms, faster than 10.47% of Python3 online submissions for Swap Nodes in Pairs.
# Memory Usage: 14 MB, less than 5.12% of Python3 online submissions for Swap Nodes in Pairs.
