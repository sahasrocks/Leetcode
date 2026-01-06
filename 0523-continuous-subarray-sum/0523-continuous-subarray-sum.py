class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        m={0:-1}
        total=0
        for i,n in enumerate(nums):
            total+=n
            r=total%k
            if r not in m:
                m[r]=i
            elif i-m[r]>1:
                return True
        return False            
        # dic = {0:-1}
        # summ = 0
        # for i, n in enumerate(nums):
        #     if k != 0:
        #         summ = (summ + n) % k
        #     else:
        #         summ += n
        #     if summ not in dic:
        #         dic[summ] = i
        #     else:
        #         if i - dic[summ] >= 2:
        #             return True
        # return False