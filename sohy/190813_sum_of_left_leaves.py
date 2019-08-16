# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        ret = 0;        
        
        if root is None:
            return 0
        
        else:
            if root.left is not None:
                if root.left.left is None and root.left.right is None:
                    ret += root.left.val
                else:
                    ret += self.sumOfLeftLeaves(root.left)
            ret += self.sumOfLeftLeaves(root.right)
        
        return ret; 
    
'''
- redo [ ] 
- logic: checking if this left node is the last one of this branch -> if it is, just add 
        if not, recursive call. 

'''