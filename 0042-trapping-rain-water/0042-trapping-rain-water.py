class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        l,r=0,len(height)-1
        leftMax,rightMax=height[l],height[r]
        res=0
        while l<r:
            if leftMax<rightMax:
                l+=1
                leftMax=max(leftMax,height[l])
                res+=leftMax-height[l]
            else:
                r-=1
                rightMax=max(rightMax,height[r])
                res+=rightMax-height[r]
        return res                
        
        
        
        
        
        
        
        
        # i, j, ans, mx, mi = 0, len(height) - 1, 0, 0, 0
        # while i <= j:
        #     # take the min height
        #     mi = min(height[i], height[j])
        #     # find the max min height
        #     mx = max(mx, mi)
        #     # the units of water being tapped is the diffence between max height and min height
        #     ans += mx - mi
        #     # move the pointer i if height[i] is smaller
        #     if height[i] < height[j]: i += 1
        #     # else move pointer j
        #     else: j -= 1
        # return ans