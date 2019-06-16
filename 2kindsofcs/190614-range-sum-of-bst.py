# https://github.com/2kindsofcs/daily-algo-challenge.git

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:
        def preOrder(node):
            sum = 0
            if node:
                if node.val >= L and node.val <= R:
                    sum += node.val
                if node.val < R:
                    sum += preOrder(node.right)
                if node.val > L:
                    sum += preOrder(node.left)
            return sum 
        return preOrder(root)

    
# if, else로 나누지 않고 해
