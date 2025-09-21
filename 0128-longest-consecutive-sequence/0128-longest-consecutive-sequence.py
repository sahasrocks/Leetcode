class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # st = set(nums)    
        # mx = 0
        # for num in nums:
        #     if num-1 not in st:
        #         tmp = 1
        #         while num+1 in st:
        #             tmp += 1
        #             num += 1
        #         mx = max(mx, tmp)

        # return mx
        numSet=set(nums)
        longest=0
        for n in numSet:
            if (n-1) not in numSet:
                length=0
                while (n+length) in numSet:
                    length+=1
                longest=max(longest,length)
        return longest          
        