# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

import queue

class Solution:
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        q = queue.Queue()
        q.put(root)
        xP, yP = 0, 0
        while q:
            node = q.get()
            if node:
                children = []
                children.append(node.left)
                children.append(node.right)
                if x in children:
                    xP = node.val
                if y in children:
                    yP = node.val
                if xP and yP:
                    if xP != yP:
                        return True
                    else:
                        return False
            for child in children:
                if child:
                    q.put(child.left)
                    q.put(child.right)
        return False
                
# 같은 높이임을 어떻게 체크할 것인가?
