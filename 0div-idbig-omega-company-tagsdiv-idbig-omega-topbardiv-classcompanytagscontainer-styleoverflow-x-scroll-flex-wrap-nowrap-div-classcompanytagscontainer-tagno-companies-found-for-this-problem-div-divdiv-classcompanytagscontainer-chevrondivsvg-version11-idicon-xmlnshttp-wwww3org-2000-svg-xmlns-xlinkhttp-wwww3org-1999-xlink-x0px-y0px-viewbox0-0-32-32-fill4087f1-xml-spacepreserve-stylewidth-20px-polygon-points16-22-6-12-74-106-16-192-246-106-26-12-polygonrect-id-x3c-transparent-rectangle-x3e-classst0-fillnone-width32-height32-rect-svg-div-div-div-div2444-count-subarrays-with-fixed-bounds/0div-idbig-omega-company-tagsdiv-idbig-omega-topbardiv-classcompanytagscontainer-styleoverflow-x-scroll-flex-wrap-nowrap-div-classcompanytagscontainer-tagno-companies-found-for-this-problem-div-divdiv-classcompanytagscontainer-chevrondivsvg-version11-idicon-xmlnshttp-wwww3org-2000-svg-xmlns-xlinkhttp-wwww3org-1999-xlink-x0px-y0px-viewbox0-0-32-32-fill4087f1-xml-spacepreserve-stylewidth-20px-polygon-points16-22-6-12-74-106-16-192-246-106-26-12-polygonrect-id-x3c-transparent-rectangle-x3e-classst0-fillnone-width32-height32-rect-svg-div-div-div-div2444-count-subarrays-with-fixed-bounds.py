class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
                
        bad_point_temp = left_min_temp = left_max_temp = -1
        
        has_min = has_max = False
        
        sub_arr_cnt = 0
        
        for ix, num in enumerate(nums):
            
            if num > maxK or num < minK:
                bad_point_temp = ix
                has_min = False
                has_max = False

            if num == minK:
                left_min_temp = ix
                has_min = True
            
            if num == maxK:
                left_max_temp = ix
                has_max = True
            
            if has_min and has_max:
            
                sub_arr_cnt += min(left_min_temp, left_max_temp) - bad_point_temp
        
        return sub_arr_cnt