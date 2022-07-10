class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        value = int(''.join([str(data) for data in digits])) + 1
        
        return [int(data) for data in str(value)] 
        
       