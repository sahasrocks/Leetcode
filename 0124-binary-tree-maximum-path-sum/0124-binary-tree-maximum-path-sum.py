# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# class Solution:
#     def maxPathSum(self, root: Optional[TreeNode]) -> int:
#         def dfs(node):
#             if not node:
#                 return (0, float('-inf'))

#             left_down, left_max = dfs(node.left)
#             right_down, right_max = dfs(node.right)

#             # max path going down from this node
#             down = node.val + max(left_down, right_down, 0)

#             # max path passing through this node
#             through = node.val + left_down + right_down

#             # overall max
#             max_sum = max(left_max, right_max, through)

#             return (down, max_sum)

#         return dfs(root)[1]

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:       
        
        
        def maxsums(node):
            if not node:
                return [-2**31] * 2
            left = maxsums(node.left)
            right = maxsums(node.right)
            return [node.val + max(left[0], right[0], 0),max(left + right + [node.val + left[0] + right[0]])]
        return max(maxsums(root))