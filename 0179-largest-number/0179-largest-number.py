class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        for i, num in enumerate(nums):
            nums[i] = str(num)

        def compare(n1, n2):
            if n1 + n2 > n2 + n1:
                return -1
            else:
                return 1
        nums = sorted(nums, key=cmp_to_key(compare))
        return str(int("".join(nums)))                 
        
        
        #return '0' if max(nums) == 0 else ''.join(sorted(map(str, nums), cmp=lambda a, b: 1 if a + b < b + a else -1))