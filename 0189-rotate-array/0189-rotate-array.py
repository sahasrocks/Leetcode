class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # k = k % len(nums)
        # nums[:] = nums[-k:] + nums[:-k] 
        def swap(arr,i,j):
            while i<j:
                arr[i],arr[j]=arr[j],arr[i]
                i+=1
                j-=1
            return arr
        if k>len(nums):
            k=k%len(nums)
        if k>0:
            swap(nums,0,len(nums)-1)
            swap(nums,0,k-1)
            swap(nums,k,len(nums)-1)            
        
        # def swap(arr,i,j):
        #     while i<j:
        #         arr[i],arr[j]=arr[j],arr[i]
        #         i+=1
        #         j-=1
        #     return arr
        # if k>len(nums):
        #     k=k%len(nums)
        # if k>0:
        #     swap(nums,0,len(nums)-1)
        #     swap(nums,0,k-1)
        #     swap(nums,k,len(nums)-1)               
              
        