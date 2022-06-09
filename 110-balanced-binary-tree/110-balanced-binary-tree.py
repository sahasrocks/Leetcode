# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        return self.traverse(root)
    
    def traverse(self, node):
        if not node: return True
                
        return abs(self.height(node.left) - self.height(node.right)) < 2 \
            and self.traverse(node.left) \
            and self.traverse(node.right)
        
    def height(self, node):
        if node == None: 
            return -1
        
        left = self.height(node.left) + 1
        right = self.height(node.right) + 1
        
        return max(left, right)
        