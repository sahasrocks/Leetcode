# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        ordered = []
        def inorder(curr = root):
            nonlocal ordered
            if curr != None:
                inorder(curr.left)
                ordered.append(curr.val)
                inorder(curr.right)
            return
        inorder()
        mini = float("inf")
        for i in range(len(ordered)-1):
            mini = min(ordered[i+1] - ordered[i], mini)
        return mini