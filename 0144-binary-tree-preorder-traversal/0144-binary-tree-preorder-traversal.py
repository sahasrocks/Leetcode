# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # def traversal(self, root, preorder):
    #     if root:
    #         preorder.append(root.val)
    #         self.traversal(root.left, preorder)
    #         self.traversal(root.right, preorder)
            
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res=[]
        def dfs(root,res):
            if not root:
                return []
            res.append(root.val)
            dfs(root.left,res)
            dfs(root.right,res)
        dfs(root,res)
        return res    
        
        # preorder = []
        # self.traversal(root, preorder)
        # return preorder