class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        results = ['']
        map = {'2':'abc', '3':'def', '4':'ghi', '5':'jkl', '6':'mno', '7':'pqrs', '8':'tuv', '9':'wxyz'}

        for digit in digits:
            results = [result+d for result in results for d in map[digit]]

        return results