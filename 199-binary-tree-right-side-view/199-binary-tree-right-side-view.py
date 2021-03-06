# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        self.h = -1
        def prog(root,height):
            if root is None:
                return
            if height > self.h:
                ans.append(root.val)
                self.h = height
            prog(root.right, height + 1)
            prog(root.left, height + 1)
        prog(root,0)
        return ans