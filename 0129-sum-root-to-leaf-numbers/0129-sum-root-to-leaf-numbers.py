# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def dfs(root,sum):
            if not root:
                return 0
            sum= sum*10 + root.val
            if not root.left and not root.right:
                return sum
            return dfs(root.left,sum)+ dfs(root.right,sum)
        return dfs(root,0)            


    #     return self.dfs(root, 0)
    
    # def dfs(self, root, sum):
    #     if not root:
    #         return 0
    #     sum = sum * 10 + root.val
    #     if not root.left and not root.right:
    #         return sum
    #     return self.dfs(root.left, sum) + self.dfs(root.right, sum)
        

        # if not root:
        #     return 0
        # total=0
        # stack=[(root,root.val)]
        # while stack:
        #     node,cur_num=stack.pop()
        #     if not node.left and not node.right:
        #         total+=cur_num
        #     if node.right:
        #         stack.append((node.right,cur_num*10 +node.right.val))     
        #     if node.left:
        #         stack.append((node.left,cur_num*10 +node.left.val))
        # return total        
