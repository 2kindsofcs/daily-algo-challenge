# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def isUnivalTree(self, root: TreeNode) -> bool:
        # if root == None:
        #     return False
        # 인풋으로 None을 주진 않는 듯 
        def getList(node, value, list):
            result = []
            if node:
                if node.val != value:
                    result.append(0)
                    return result
                result.extend(getList(node.left, value, result))
                result.extend(getList(node.right, value, result))
            return result
        return False if 0 in getList(root, root.val, []) else True

    
# Runtime: 32 ms, faster than 95.75% of Python3 online submissions for Univalued Binary Tree.
# Memory Usage: 13.1 MB, less than 65.06% of Python3 online submissions for Univalued Binary Tree.