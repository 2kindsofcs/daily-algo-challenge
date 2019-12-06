class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        head = ListNode(0) 
        sortList = head
        while l1 and l2:
            if l1.val < l2.val:
                sortList.next = l1
                l1 = l1.next
                sortList = sortList.next
            elif l1.val >= l2.val:
                sortList.next = l2
                l2 = l2.next
                sortList = sortList.next
        sortList.next = l1 or l2
        return head.next

# Runtime: 32 ms, faster than 94.19% of Python3 online submissions for Merge Two Sorted Lists.
# Memory Usage: 12.6 MB, less than 100.00% of Python3 online submissions for Merge Two Sorted Lists.
            
