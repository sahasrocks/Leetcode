class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res=[]
        nums.sort()
        for i,e in enumerate(nums):
            if e>0:
                break
            if i>0 and e==nums[i-1]:
                continue
            l,r=i+1,len(nums)-1
            while l<r:
                ts=e+nums[l]+nums[r]
                if ts<0:
                    l+=1
                elif ts>0:
                    r-=1
                else:
                    res.append((e,nums[l],nums[r]))
                    l+=1
                    r-=1
                    while nums[l]==nums[l-1] and l<r:
                        l+=1
        return res                                
        
        
        
        # res=[]
        # nums.sort()
        # for i,e in enumerate(nums):
        #     if e>0:
        #         break
        #     if i>0 and e==nums[i-1]:
        #         continue
        #     l,r=i+1,len(nums)-1
        #     while l<r:
        #         ts=nums[l]+nums[r]+e
        #         if ts<0:
        #             l+=1
        #         elif ts>0:
        #             r-=1
        #         else:
        #             res.append([e,nums[l],nums[r]])
        #             l+=1
        #             r-=1
        #             while nums[l]==nums[l-1] and l<r:
        #                 l+=1
        # return res                                
        
        
        
        
        
        
        
        # res=[]
        # nums.sort()
        # for i,e in enumerate(nums):
        #     if e>0:
        #         break
        #     if i>0 and e==nums[i-1]:
        #         continue
        #     l,r=i+1,len(nums)-1
        #     while l<r:
        #         ts=nums[l]+nums[r]+e
        #         if ts>0:
        #             r-=1
        #         elif ts<0:
        #             l+=1
        #         else:
        #             res.append([e,nums[l],nums[r]])
        #             l+=1
        #             r-=1
        #             while nums[l]==nums[l-1] and l<r:
        #                 l+=1
        # return res                                
        
        
        
        
        
        
        
        
        # res=[]
        # nums.sort()
        # for i,e in enumerate(nums):
        #     if e>0:
        #         break
        #     if i>0 and e==nums[i-1]:
        #         continue
        #     l,r=i+1,len(nums)-1
        #     while l<r:
        #         ts=nums[l]+nums[r]+e
        #         if ts>0:
        #             r-=1
        #         elif ts<0:
        #             l+=1
        #         else:
        #             res.append([e,nums[l],nums[r]])
        #             l+=1
        #             r-=1
        #             while nums[l]==nums[l-1] and l<r:
        #                 l+=1
        # return res                                
        
        # res=[]
        # nums.sort()
        # for i,e in enumerate(nums):
        #     if e>0:
        #         break
        #     if i>0 and e==nums[i-1]:
        #         continue
        #     l,r=i+1,len(nums)-1
        #     while l<r:
        #         ts=e+nums[r]+nums[l]
        #         if ts>0:
        #             r-=1
        #         elif ts<0:
        #             l+=1
        #         else:
        #             res.append([e,nums[l],nums[r]])
        #             l+=1
        #             r-=1
        #             while nums[l]==nums[l-1] and l<r:
        #                 l+=1
        # return res                                    
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        # res=[]
        # nums.sort()
        # for i,e in enumerate(nums):
        #     if e>0:
        #         break
        #     if i>0 and e==nums[i-1]:
        #         continue
        #     l,r=i+1,len(nums)-1
        #     while l<r:
        #         ts=e+nums[r]+nums[l]
        #         if ts>0:
        #             r-=1
        #         elif ts<0:
        #             l+=1
        #         else:
        #             res.append([e,nums[l],nums[r]])
        #             l+=1
        #             r-=1
        #             while nums[l]==nums[l-1] and l<r:
        #                 l+=1
        # return res                                
        
        
        
        
        
        # res=[]
        # nums.sort()
        # for i,e in enumerate(nums):
        #     if e>0:
        #         break
        #     if i>0 and e==nums[i-1]:
        #         continue
        #     l,r=i+1,len(nums)-1
        #     while l<r:
        #         thSum=e+nums[l]+nums[r]
        #         if thSum>0:
        #             r-=1
        #         elif thSum<0:
        #             l+=1
        #         else:
        #             res.append([e,nums[l],nums[r]])
        #             l+=1
        #             r-=1
        #             while nums[l]==nums[l-1] and l<r:
        #                 l+=1
        # return res                    
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        # nums.sort()
        # res=[]
        # for i,e in enumerate(nums):
        #     if i > 0 and e==nums[i-1]:
        #         continue
        #     l,r=i+1,len(nums)-1
        #     while l<r:
        #         threeSum= e + nums[l]+nums[r]
        #         if threeSum >0:
        #             r-=1
        #         elif threeSum<0:
        #             l+=1
        #         else:
        #             res.append([e,nums[l],nums[r]])
        #             l+=1
        #             while nums[l]==nums[l-1] and l<r:
        #                 l+=1 
        # return res                    

