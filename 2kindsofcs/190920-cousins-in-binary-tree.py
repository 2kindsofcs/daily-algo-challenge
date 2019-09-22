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
        while not q.empty():
            node = q.get()
            if node:
                children.append(node.left)
                children.append(node.right)
            if q.empty():
                valueList = []
                for child in children:
                    if child:
                        valueList.append(child.val)
                    else:
                        valueList.append(-1)
                if x in valueList and y in valueList:
                    xP = valueList.index(x) // 2
                    yP = valueList.index(y) // 2
                    if xP != yP:
                        return True
                    else:
                        return False
                for child in children:
                    if child:
                        q.put(child)
                children = []
        return False
            
                
# Runtime: 48 ms, faster than 6.64% of Python3 online submissions for Cousins in Binary Tree.
# Memory Usage: 14.1 MB, less than 6.12% of Python3 online submissions for Cousins in Binary Tree.
# 큐가 비었는지 확인하는 것을 while q 라고 했더니 무한 반복에 빠진 것이었다. q가 비어있더라도 if q는 True이다.
