# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        node = head
        count, index = 1, 1
        middle = 0
        while node.next != None:
            node = node.next
            count = count + 1
        if count % 2 == 1:
            middle = (count + 1) // 2
        else:
            middle = count // 2 + 1
        node = head
        while index < middle:
            node = node.next
            index = index + 1
        return node
        
            
# Runtime: 32 ms, faster than 83.60% of Python3 online submissions for Middle of the Linked List.
# Memory Usage: 13 MB, less than 88.25% of Python3 online submissions for Middle of the Linked List.
            
