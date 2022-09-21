class Solution:
    def sumEvenAfterQueries(self, array: List[int], queries: List[List[int]]) -> List[int]:
        evenSum = 0
        for num in array:
            if num % 2 == 0:
                evenSum += num
                
                
        result = []
        for val, index in queries:
            
            if array[index] % 2 == 0:
                evenSum -= array[index]
            array[index] += val
                
            if array[index] % 2 == 0:
                evenSum += array[index]
                    
            result.append(evenSum)
            
                
        return result