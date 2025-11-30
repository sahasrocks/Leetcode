class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        total = sum(nums)
        remain = total % p
        if remain ==0:
            return 0
        res = len(nums)
        cur_sum=0
        remain_to_inx=defaultdict(int)
        remain_to_inx[0]=-1
        for i,e in enumerate(nums):
            cur_sum= (cur_sum+e) % p
            prefix = (cur_sum - remain + p) % p
            if prefix in remain_to_inx :
                length = i - remain_to_inx[prefix]
                res=min(res,length)
            remain_to_inx[cur_sum]=i
        return -1 if res==len(nums) else res             