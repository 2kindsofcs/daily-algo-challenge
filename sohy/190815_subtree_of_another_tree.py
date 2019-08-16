# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    
    def equals(self, s, t):
        if s == None and t == None:
            return True 
        if s == None or t == None:
            return False 
        return s.val == t.val and self.equals(s.left, t.left) and self.equals(s.right, t.right)
    
    
    def isSubtree(self, s, t):
        """
        :type s: TreeNode
        :type t: TreeNode
        :rtype: bool
        """
        
        return s != None and (self.equals(s,t) or self.isSubtree(s.left, t) or self.isSubtree(s.right,t))
        
'''
Runtime: 336 ms, faster than 12.96% of Python online submissions for Subtree of Another Tree.
Memory Usage: 12.9 MB, less than 80.00% of Python online submissions for Subtree of Another Tree.

- Redo [ ] : had to look at sol 
- logic: traverse, and check if this equals, if not look at its subtrees and see if they match 

'''