# class Solution(object):
#     def getHeight(self, root):
#         height = 0
#         while root:
#             height += 1
#             root = root.left
#         return height

#     def countNodes(self, root):
#         count = 0
#         while root:
#             l, r = map(self.getHeight, (root.left, root.right))
#             if l == r:
#                 count += 2 ** l
#                 root = root.right
#             else:
#                 count += 2 ** r
#                 root = root.left
#         return count
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        q=deque([root])
        c=0
        while q:
            node=q.popleft()
            c+=1
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        return c                
        # def pre(node):
        #     if not node:
        #         return 0
        #     return pre(node.left)+pre(node.right)+1
        # return pre(root)        
        # from collections import deque

        # if not root:
        #     return 0
        # q=deque([root])
        # c=0
        # while q:
        #     node=q.popleft()   
        #     c+=1
        #     if node.left:
        #         q.append(node.left) 
        #     if node.right:
        #         q.append(node.right) 

        # return c           
        