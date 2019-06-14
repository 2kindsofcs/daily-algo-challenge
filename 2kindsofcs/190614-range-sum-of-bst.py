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
                isSmall = root.val < L
                isBig = root.val > R
                if not isSmall and not isBig:
                    sum += root.val
                    sum += preOrder(root.right, L, R)                    
                    sum += preOrder(root.left, L, R)
                elif isSmall:
                    sum += preOrder(root.right, L, R)
                elif isBig:
                    sum += preOrder(root.left, L, R)
            return sum 
        return preOrder(root, L, R)

# Runtime: 236 ms, faster than 64.77% of Python3 online submissions for Range Sum of BST.
# Memory Usage: 22 MB, less than 5.20% of Python3 online submissions for Range Sum of BST.

# 각 노드의 값은 고유하다고 했고, BST 특성을 이용하면 노드 값이 L보다 작다면 해당 노드의 왼쪽 자식은 애초에 검사할 필요가 없음.
# 반대로 오른쪽은 R보다 크면 오른쪽 자식을 검사할 필요가 없음. 이를 활용해서 조금 고쳐보았는데, 속도는 조금 빨라졌지만 코드가 썩 맘에 들지는 않는다.