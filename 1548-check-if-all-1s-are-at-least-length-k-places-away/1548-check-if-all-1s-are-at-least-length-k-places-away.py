class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        a=k
        for n in nums:
            if n==1:
                if a<k:
                    return False
                a=0
            else:
                a+=1
        return True                
                    

        