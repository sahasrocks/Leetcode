class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        self.max = {}
        self.find(root,lv=0)
        return list(self.max.values())
    
    def find(self,root,lv):
        if root == None:
            return
        if self.max.get(lv,None)!=None:
            self.max[lv] = max(self.max[lv],root.val)
        else:
            self.max[lv] = root.val
        self.find(root.left,lv+1)
        self.find(root.right,lv+1)