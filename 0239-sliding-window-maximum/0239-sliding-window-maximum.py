class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q=deque()
        res=[]
        l=r=0
        while r<len(nums):
            while q and nums[q[-1]]<nums[r]:
                q.pop()
            q.append(r)
            if l>q[0]:
                q.popleft()
            if r+1>=k:
                res.append(nums[q[0]])
                l+=1
            r+=1
        return res                
        
        # q=collections.deque()
        # output=[]
        # l=r=0
        # while r<len(nums):
        #     while q and nums[q[-1]]<nums[r]:
        #         q.pop()
        #     q.append(r)
        #     if l>q[0]:
        #         q.popleft()
        #     if r+1 >=k:
        #         output.append(nums[q[0]])
        #         l+=1
        #     r+=1
        # return output                
        
        
        # from collections import deque
        # q = deque() ;res = []
        # j = 0 ; i = 0
        # while j<len(nums):
        #     while q and nums[j]>q[-1]:
        #         q.pop()
        #     q.append(nums[j])
        #     if j-i+1<k:
        #         j+=1
        #     elif j-i+1==k:
        #         res.append(q[0])
        #         if q[0]==nums[i]:
        #             q.popleft()
        #         i+=1
        #         j+=1
        # return res