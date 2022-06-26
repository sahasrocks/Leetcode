class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        import numpy as np
        lst3 = [value for value in nums1 if value in nums2] 
        x = np.array(lst3)
        return (np.unique(x))