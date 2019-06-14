# https://github.com/2kindsofcs/daily-algo-challenge.git

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:
        # nested function 이므로 L,R에 바로 접근 가능. 인자로 넣어주지 않아도 됨. 
        # 또한 바깥 변수를 shadowing 하지 않게 하자. 겹치는 이름을 쓰지 말자. 
        def preOrder(node):
            sum = 0
            if node:
                isSmall = node.val < L
                isBig = node.val > R
                if not isSmall and not isBig:
                    sum += node.val + preOrder(node.right) + preOrder(node.left)
                elif isSmall:
                    sum += preOrder(node.right)
                else:
                    sum += preOrder(node.left)
            return sum 
        return preOrder(root)

# Runtime: 208 ms, faster than 99.60% of Python3 online submissions for Range Sum of BST.
# Memory Usage: 21.8 MB, less than 29.73% of Python3 online submissions for Range Sum of BST.

# 각 노드의 값은 고유하다고 했고, BST 특성을 이용하면 노드 값이 L보다 작다면 해당 노드의 왼쪽 자식은 애초에 검사할 필요가 없음.
# 마지막 elif isBig을 else로 수정. isBig을 확인할 필요가 없다. 값이 L과 R 사이에 있는 것도 아니고, L보다 작은 것도 아니라면 R보다 큰 경우밖에 없기 때문이다.
# 확실히 속도가 많이 향상되었다. 
