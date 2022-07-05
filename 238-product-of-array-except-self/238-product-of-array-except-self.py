class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n=len(nums)
        product = []
        prefix =1
        for i in range(n):
            product.append(prefix)
            prefix = prefix*nums[i]
        suffix =1
        for i in range(n-1,-1,-1):
            product[i] = suffix * product[i]
            suffix = suffix*nums[i]
        return product 