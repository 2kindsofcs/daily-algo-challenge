# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        leftLeavesList = []
        def leftLeaves(node):
            if not node:
                return
            if node.left:
                if not node.left.left and not node.left.right:
                    leftLeavesList.append(node.left.val)
                else:
                    leftLeaves(node.left)
            leftLeaves(node.right)
        leftLeaves(root)
        return sum(leftLeavesList)
                    
            
# Runtime: 32 ms, faster than 95.90% of Python3 online submissions for Sum of Left Leaves.
# Memory Usage: 14.7 MB, less than 7.69% of Python3 online submissions for Sum of Left Leaves.
            
