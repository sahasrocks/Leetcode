class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        perms=[[]]
        for n in nums:
            new_perms=[]
            for p in perms:
                for i in range(len(p)+1):
                    p_copy=p.copy()
                    p_copy.insert(i,n)
                    new_perms.append(p_copy)
            perms=new_perms
        return perms            

        
        
        # if not nums: 
        #     return [[]]
        # return [[nums[i]] + j for i in range(len(nums)) for j in self.permute(nums[:i]+nums[i+1:])]