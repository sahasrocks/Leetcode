# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: TreeNode) -> List[float]:
        q=deque([root])
        avgs=[]
        while q:
            avg=0
            n=len(q)
            for i in range(n):
                node=q.popleft()
                avg+=node.val
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            avg /=n
            avgs.append(avg)
        return avgs                
        
        
        
        
        
        
        
        
        
        
        
        # q, ans = [root], []
        # while len(q):
        #     qlen, row = len(q), 0
        #     for i in range(qlen):
        #         curr = q.pop(0)
        #         row += curr.val
        #         if curr.left: q.append(curr.left)
        #         if curr.right: q.append(curr.right)
        #     ans.append(row/qlen)
        # return ans
        