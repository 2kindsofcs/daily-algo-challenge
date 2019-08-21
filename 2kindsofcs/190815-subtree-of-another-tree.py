# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool: 
        if s == t:
            return True
        # 재귀를 사용하지 않고 proorder
        def preorder(root):
            nodeList, result = [], []
            nodeList.append(root)
            while nodeList:
                node = nodeList.pop()
                # 단순히 s의 preorder 결과물 안에 t의 preorder의 결과물이 있는지를 확인할 경우
                # s = [1,2,3] 이고 t = [2, 3] 같은 경우를 올바르게 판단할 수 없으므로 왼쪽 없는 자식과 오른쪽 없는 자식을 구분해서 표기 
                if node and node != 'rNull' and node != 'lNull':
                    result.append(node.val)
                    if node.right:
                        nodeList.append(node.right)
                    else:
                         result.append('rNull')
                    if node.left:
                        nodeList.append(node.left)
                    else:
                         result.append('lNull')
            return result
        tList, sList = preorder(t), preorder(s)
        tLength, sLength = len(tList), len(sList)
        for i in range(sLength):
            if sList[i] == tList[0]:
                if sList[i:i + tLength] == tList:
                    return True
                else:
                    continue
        return False
                
# Runtime: 88 ms, faster than 89.05% of Python3 online submissions for Subtree of Another Tree.
# Memory Usage: 14 MB, less than 100.00% of Python3 online submissions for Subtree of Another Tree.
