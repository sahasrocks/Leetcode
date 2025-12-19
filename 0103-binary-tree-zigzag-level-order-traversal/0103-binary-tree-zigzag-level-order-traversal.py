# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res=[]
        q=deque([root])
        while q:
            n=len(q)
            level=[]
            for i in range(n):
                node=q.popleft()
                if node:
                    level.append(node.val)
                    q.append(node.left)
                    q.append(node.right)
            if level:        
                level=(level)[::-1] if len(res)%2 else level
                res.append(level)
        return res                



















# Definition for a binary tree node.
# # class TreeNode:
# #     def __init__(self, val=0, left=None, right=None):
# #         self.val = val
# #         self.left = left
# #         self.right = right
# class Solution:
# # @param root, a tree node
# # @return a list of lists of integers
#     def zigzagLevelOrder(self, root):
#         res=[]
#         q=deque([root] if root else [])
#         while q:

#             level=[]
#             for i in range(len(q)):
#                 node=q.popleft()
#                 level.append(node.val)
#                 if node.left:
#                     q.append(node.left)
#                 if node.right:
#                     q.append(node.right)
#             level=list(reversed(level) if len(res)%2 else level)
#             res.append(level)
#         return res                 
        
        
        
        
        
#         # queue = collections.deque([root])
#         # res = []
#         # while queue:
#         #     r = []
#         #     for _ in range(len(queue)):
#         #         q = queue.popleft()
#         #         if q:
#         #             r.append(q.val)
#         #             queue.append(q.left)
#         #             queue.append(q.right)
#         #     r = r[::-1] if len(res) % 2 else r
#         #     if r:
#         #         res.append(r)
#         # return res

        