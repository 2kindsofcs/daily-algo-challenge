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
        children = []
        while q:
            node = q.get()
            if node:
                children.append(node.left)
                children.append(node.right)
            if q.empty():
                valueList = [ child.val for child in children ]
                if x in valueList and y in valueList:
                    xP = valueList.index(x) // 2
                    yP = valueList.index(y) // 2
                    if xP and yP and xP != yP:
                        return True
                    else:
                        return False
                for child in children:
                    if child:
                        q.put(child.left)
                        q.put(child.right)
                children = []
        return False
    
# time limit exceeded가 뜬다. 어디선가 무한반복이 되고 있다는 것. 
