class Solution:
    def maxArea(self, height: List[int]) -> int:
        l=0
        r=len(height)-1
        res=0
        while l<r:
            a=min(height[l],height[r])*(r-l)
            res=max(res,a)
            if height[l]<height[r]:
                l+=1
            else:
                r-=1
        return res            
        
        
        
        # l=0
        # r=len(height)-1
        # res=0
        # while l<r:
        #     a=min(height[l],height[r])*(r-l)
        #     res=max(res,a)
        #     if height[l]<height[r]:
        #         l+=1
        #     else:
        #         r-=1
        # return res        

        
        
        
        
        
        
        
        
        
        
        
        
        # l=0
        # r=len(height)-1
        # res=0
        # while l<r:
        #     a=min(height[l],height[r]) *(r-l)
        #     res=max(res,a)
        #     if height[l]<height[r]:
        #         l+=1
        #     else:
        #         r-=1
        # return res            
        
        
        # l=0
        # r=len(height)-1
        # res=0
        # while l<r:
        #     a=min(height[l],height[r])*(r-l)
        #     res=max(res,a)
        #     if height[l]<height[r]:
        #         l+=1
        #     else:
        #         r-=1
        # return res            
        
        
        
        
        
        
        # l,r=0,len(height)-1
        # res=0
        # while l<r:
        #     a=min(height[l],height[r])*(r-l)
        #     res=max(res,a)
        #     if height[l]<height[r]:
        #         l+=1
        #     else:
        #         r-=1
        # return res            
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        # l,r=0,len(height)-1
        # res=0
        # while l<r:
        #     a=min(height[l],height[r])*(r-l)
        #     res=max(res,a)
        #     if height[l]<=height[r]:
        #         l+=1
        #     else:
        #         r-=1
        # return res            
        
        
        
        # l=0
        # res=0
        # r=len(height)-1
        # while l<r:
        #     a=min(height[l],height[r])*(r-l)
        #     res=max(res,a)
        #     if height[l]<=height[r]:
        #         l+=1
        #     else:
        #         r-=1
        # return res            
