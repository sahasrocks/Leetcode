# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    
    # def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
    #     q = deque()
    #     q.append(root)
    #     while q:
    #         node = q.popleft()
    #         if node:
    #             node.left, node.right = node.right, node.left
    #             q.append(node.left)
    #             q.append(node.right)
    #     return root
    def invertTree(self, root):
        # if not root:
        #     return None
        # tmp = root.left
        # root.left=root.right
        # root.right=tmp
        
        # self.invertTree(root.left)
        # self.invertTree(root.right)
        
        # return root
        # if not root:
        #     return None
        # root.left,root.right=root.right,root.left
        # self.invertTree(root.left)
        # self.invertTree(root.right)    
        # return root
        from collections import deque

        if not root:
            return None
        q=deque([root])
        while q:
            node=q.popleft()
            node.left,node.right=node.right,node.left
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        return root            