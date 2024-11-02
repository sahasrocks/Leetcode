class Solution:
    def maxArea(self, height: List[int]) -> int:
        # a,b=0 , len(height)-1
        # r=0
        # while a<b:
        #     area = min(height[a],height[b]) * (b-a)
        #     r= max(r,area)
        #     if height[a]<=height[b]:
        #         b+=1
        #     else:
        #         a-=1
        # return r
        l, r = 0, len(height) - 1
        res = 0

        while l < r:
            area = min(height[l], height[r]) * (r - l)
            res = max(res, area)
            if height[l] <= height[r]:
                l += 1
            else:
                r -= 1
        return res  