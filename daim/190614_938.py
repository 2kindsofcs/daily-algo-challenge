"""
LeetCode : 938. Range Sum of BST
problem : https://leetcode.com/problems/range-sum-of-bst/
Runtime : 224ms, faster than 89.05%
Memory Usage : 21.9 MB, less than 8.39%
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def checkChildBST(self, root, result, l, r):

        # if leaf node, recursion must be closed
        if root == None:
            return result

        if root.val <= l:
            if root.val == l:
                result += root.val
            result = self.checkChildBST(root.right, result, l, r)

        if r <= root.val:
            if r == root.val:
                result += root.val
            result = self.checkChildBST(root.left, result, l, r)

        if l < root.val < r:
            result = self.checkChildBST(root.left, result + root.val, l, r)
            result = self.checkChildBST(root.right, result, l, r)

        # Returns the result of the tree of child
        return result


    def rangeSumBST(self, root, L: int, R: int) -> int:
        return self.checkChildBST(root, 0, L, R)
