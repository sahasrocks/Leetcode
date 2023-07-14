from collections import defaultdict

class Solution:
    def longestSubsequence(self, arr: List[int], dif: int) -> int:
        # Create a defaultdict to store the lengths of subsequences
        lengths = defaultdict(lambda: 0)
        
        # Iterate over the array elements
        for num in arr:
            # Calculate the length of the subsequence ending at the current element
            lengths[num] = lengths[num - dif] + 1

        # Return the maximum length of subsequences
        return max(lengths.values())
