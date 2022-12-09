class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        def rec(root, min_so_far, max_so_far):
            if not root: return
            nonlocal res
            min_so_far, max_so_far = min(min_so_far, root.val), max(max_so_far, root.val)
            res = max(res, root.val - min_so_far, max_so_far - root.val)
            rec(root.left, min_so_far, max_so_far); rec(root.right, min_so_far, max_so_far);
            
        res = 0
        rec(root, math.inf, -math.inf)
        return res