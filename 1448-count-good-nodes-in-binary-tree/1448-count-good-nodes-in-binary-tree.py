# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(node, max_so_far):
			#if there is no node then there is no good nodes so return 0
            if not node:
                return 0
			
			#if current node is good then 1 otherwise 0
            good = 1 if node.val>=max_so_far else 0
			
			#Checking if current node is greater than max_so_far , if yes then update max_so_far to current node's value
            max_so_far = max(max_so_far, node.val)
            
			#returning total of current good , no. of good nodes in left and right
            return good + dfs(node.left, max_so_far) + dfs(node.right, max_so_far)
        
        return dfs(root, -int(1e5))#Since constraints are [-10^4, 10^4] so we take -10^5 as maximum