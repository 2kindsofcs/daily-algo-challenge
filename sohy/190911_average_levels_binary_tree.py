# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def averageOfLevels(self, root):
        """
        :type root: TreeNode
        :rtype: List[float]
        """
        
        queue = [(root, 0)]
        sum_map = {}
        
        while queue:
            node, level = queue.pop(0)
            if level in sum_map:
                sum_map[level] = (sum_map[level][0] + node.val, sum_map[level][1]+1.0)
            else:
                sum_map[level] = (node.val, 1)

            if node.left:
                queue.append((node.left, level + 1))
            if node.right:
                queue.append((node.right, level + 1))
        
        ret_list = [0]*len(sum_map)
        for key, value in sum_map.items():
            ret_list[key] = value[0]/value[1]
        return ret_list
    
        