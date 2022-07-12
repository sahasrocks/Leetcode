class Solution:
    def lengthOfLongestSubstring(self, string: str) -> int:
        charSet = set()
        l = 0
        res = 0
        
        for r in range(len(string)):
            while string[r] in charSet:
                charSet.remove(string[l])
                l += 1
            charSet.add(string[r])
            res = max(res, r - l + 1)
        return res
        
        
        
        
        
        
        
        
        
        
        
        
        last_idx = {}
        max_len = 0
        start_idx = 0

        for i in range(0, len(string)):

            # Find the last index of str[i]
            # Update start_idx (starting index of current window)
            # as maximum of current value of start_idx and last
            # index plus 1
            if string[i] in last_idx:
                start_idx = max(start_idx, last_idx[string[i]] + 1)

            # Update result if we get a larger window
            max_len = max(max_len, i-start_idx + 1)

            # Update last index of current char.
            last_idx[string[i]] = i

        #return max_len   