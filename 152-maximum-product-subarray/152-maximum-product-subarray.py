class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        minval = nums[0]
        maxval = nums[0]

        currmax = nums[0]
        if len(nums)==1:
            return currmax


        for x in range(1 , len(nums)):
            if nums[x]<0:
                tmp = minval
                minval = maxval
                maxval = tmp

            minval  = min(nums[x] , nums[x]*minval)
            maxval = max(nums[x] , nums[x]*maxval)

            currmax = max(currmax , maxval)



        return(currmax)