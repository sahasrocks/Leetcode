# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        res=[]
        if not root:
            return []
        q=deque([root])
        while q:
            n=len(q)
            level=[]
            for i in range(n):
                node=q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
                level.append(node.val)
            res.append(level)
        return res[::-1]        

        
        
        
        
        # if not root: return []
        # q, ans = deque([root]), []
        # while len(q):
        #     n, curLevel = len(q), []
        #     for i in range(n):
        #         cur = q.popleft()
        #         if cur.left: 
        #             q.append(cur.left)
        #         if cur.right: 
        #             q.append(cur.right)
        #         curLevel.append(cur.val)
        #     ans.append(curLevel)
        # return ans[::-1]