# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(node,l,r):
            if not node:
                return True
            if not (l<node.val and r>node.val):
                return False
            return (dfs(node.left,l,node.val) and dfs(node.right,node.val,r))
        return dfs(root,float("-inf"),float("inf"))            
        # def dfs(node,l,r):
        #     if not node:
        #         return True
        #     if not (l < node.val and r > node.val):
        #         return False
        #     return (dfs(node.left,l,node.val) and dfs(node.right,node.val,r))
        # return dfs(root,float('-inf'),float('inf'))            
        
        
        
        # def valid(node,left,right):
        #     if not node:
        #         return True
        #     if not (left<node.val and right>node.val):
        #         return False
        #     return (valid(node.left,left,node.val) and valid(node.right,node.val,right))     
        # return valid(root,float("-inf"),float("inf"))      
        
        
        
        
        
        
        
        
        
        
        
        # def valid(node,left,right):
        #     if not node:
        #         return True
        #     if not (node.val <right and node.val > left):
        #         return False
        #     return (valid(node.left, left, node.val) and
        #             valid(node.right, node.val, right))
        
        # return valid(root, float("-inf"), float("inf"))
        