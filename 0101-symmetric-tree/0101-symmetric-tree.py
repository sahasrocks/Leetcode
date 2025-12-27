# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def dfs(l,r):
            if not l and not r:
                return True
            if not l or not r:
                return False
            return (l.val == r.val and dfs(l.left, r.right) and dfs(l.right, r.left))   
        return dfs(root.left,root.right)         




        # def isSym(L,R):
        #     if L and R and L.val == R.val: 
        #         return isSym(L.left, R.right) and isSym(L.right, R.left)
        #     return L == R
        # return not root or isSym(root.left, root.right)
        # def dfs(left,right):
        #     if not left and not right:
        #         return True
        #     if not left or not right:
        #         return False
        #     return (left.val==right.val and dfs(left.left,right.right) and dfs(left.right, right.left))
        # return dfs(root.left,root.right)            
        