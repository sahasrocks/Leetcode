# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root):
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
                res.append(level)
        return res                
        
        
        # res=[]
        # q=deque([root])
        # while q:
        #     n=len(q)
        #     level=[]

        #     for i in range(n):
        #         node=q.popleft()
        #         if node:
        #             level.append(node.val)
        #             q.append(node.left)
        #             q.append(node.right)
        #     if level:
        #         res.append(level) 
        # return res               


        
        
        
        
        
        
        
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
        # return ans
        
        
        # ans, level = [], [root]
        # while root and level:
        #     ans.append([node.val for node in level])
        #     LRpair = [(node.left, node.right) for node in level]
        #     level = [leaf for LR in LRpair for leaf in LR if leaf]
        # return ans
        # a=[]
        # q=collections.deque()
        # q.append(root)
        # while q:
        #     qlen= len(q)
        #     level=[]
        #     for i in range(qlen):
        #         node=q.popleft()
        #         if node:
        #             level.append(node.val)
        #             q.append(node.left)
        #             q.append(node.right)
        #     if level:
        #         a.append(level)
        # return a
        