# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root):
        
        # ans, level = [], [root]
        # while root and level:
        #     ans.append([node.val for node in level])
        #     LRpair = [(node.left, node.right) for node in level]
        #     level = [leaf for LR in LRpair for leaf in LR if leaf]
        # return ans
        a=[]
        q=collections.deque()
        q.append(root)
        while q:
            qlen= len(q)
            level=[]
            for i in range(qlen):
                node=q.popleft()
                if node:
                    level.append(node.val)
                    q.append(node.left)
                    q.append(node.right)
            if level:
                a.append(level)
        return a    