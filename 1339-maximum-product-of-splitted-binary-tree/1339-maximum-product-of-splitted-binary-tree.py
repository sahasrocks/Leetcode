# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        def total(root):
            if not root:
                return 0
            return root.val + total(root.left) + total(root.right)
        mod = 10**9 +7
        treeSum=total(root)
        best=0
        def findMax(node):
            if not node:
                return 0
            subTreeSum = node.val + findMax(node.left) + findMax(node.right)
            nonlocal best
            best = max(best, subTreeSum * (treeSum-subTreeSum))
            return subTreeSum
        findMax(root)
        return best % mod        

        
        # def dfs(root):
        #     if root == None: return 0
        #     currSum = dfs(root.left) + dfs(root.right) + root.val
        #     self.ans = max(self.ans, currSum * (self.totalSum - currSum))
        #     return currSum

        # self.ans, self.totalSum = 0, 0
        # self.totalSum = dfs(root)  # Firstly, get total sum of all nodes in the Binary Tree
        # dfs(root)  # Then dfs in post order to calculate sum of each subtree and its complement
        # return self.ans % (10 ** 9 + 7)