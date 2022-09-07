# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        
        def dfs(root):
            
            if not root:return ''
            
            l=dfs(root.left)
            
            r=dfs(root.right)
            
            if not l and not r:
                return str(root.val)
            
            if l and r:
                return f"{root.val}({l})({r})"
            
            return f"{root.val}({l})" if l else f"{root.val}()({r})"
            
            
        return dfs(root)