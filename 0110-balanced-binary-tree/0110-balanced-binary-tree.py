# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
#     def isBalanced(self, root: Optional[TreeNode]) -> bool:
#         return self.traverse(root)
    
#     def traverse(self, node):
#         if not node: return True
                
#         return abs(self.height(node.left) - self.height(node.right)) < 2 \
#             and self.traverse(node.left) \
#             and self.traverse(node.right)
        
#     def height(self, node):
#         if node == None: 
#             return -1
        
#         left = self.height(node.left) + 1
#         right = self.height(node.right) + 1
        
#         return max(left, right)
    def isBalanced(self, root):
        def dfs(root):
            if not root:
                return [True,0]
            left,right=dfs(root.left),dfs(root.right)
            balanced=(left[0] and right[0] and abs(left[1]-right[1])<=1)
            return [balanced,1+max(left[1],right[1])]
        return dfs(root)[0]