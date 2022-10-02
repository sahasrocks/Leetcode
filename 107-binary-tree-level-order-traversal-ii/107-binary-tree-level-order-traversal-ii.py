# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root: return []
        q, ans = deque([root]), []
        while len(q):
            n, curLevel = len(q), []
            for i in range(n):
                cur = q.popleft()
                if cur.left: 
                    q.append(cur.left)
                if cur.right: 
                    q.append(cur.right)
                curLevel.append(cur.val)
            ans.append(curLevel)
        return ans[::-1]