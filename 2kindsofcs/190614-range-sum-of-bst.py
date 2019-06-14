# https://github.com/2kindsofcs/daily-algo-challenge.git


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:
        def preOrder(root, L, R):
            sum = 0 
            if root:
                if root.val >= L and root.val <= R:
                    sum += root.val
                sum += preOrder(root.left, L, R)
                sum += preOrder(root.right, L, R)
            return sum 
        return preOrder(root, L, R)


# Runtime: 300 ms, faster than 28.68% of Python3 online submissions for Range Sum of BST.
# Memory Usage: 21.9 MB, less than 5.20% of Python3 online submissions for Range Sum of BST.
# 재귀를 이용해서 일단 풀었는데 굉장히 느리고 메모리도 많이 잡아 먹는다. 