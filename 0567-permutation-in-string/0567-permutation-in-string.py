class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        window=len(s1)
        s1_c=Counter(s1)
        for i in range(len(s2)-window+1):
            s2_c=Counter(s2[i:i+window])
            if s2_c==s1_c:
                return True
        return False        
        
        # if len(s1) > len(s2):
        #     return False

        # s1Count = [0] * 26
        # s2Count = [0] * 26

        # for c in s1:
        #     s1Count[ord(c) - ord('a')] += 1

        # l = 0
        # for r in range(len(s2)):
        #     s2Count[ord(s2[r]) - ord('a')] += 1

        #     if (r - l + 1) > len(s1):
        #         s2Count[ord(s2[l]) - ord('a')] -= 1
        #         l += 1

        #     if s1Count == s2Count:
        #         return True

        # return False

# class Solution:
#     def checkInclusion(self, s1: str, s2: str) -> bool:
#         s1 = sorted(s1)

#         for i in range(len(s2)):
#             for j in range(i, len(s2)):
#                 subStr = s2[i : j + 1]
#                 subStr = sorted(subStr)
#                 if subStr == s1:
#                     return True
#         return False
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        # n1, n2 = len(s1), len(s2)                   # Example: s1 = "abi"  s2 = "eidbiaoo"
        #                                             # ctr1 = {b:2, a:1, i:1}
        # ctr1, ctr2 = Counter(s1), Counter(s2[:n1])  
        #                                             #  i     ctr2                  ctr1 == ctr2 
        # for i in range(n1,n2):                      # ––––   –––––––––––––––       ––––––––––––
        #     if ctr1 == ctr2: return True            #  4     {e:1, i:1, d:1, b:1}      False
        #                                             #  5     {b:2, i:1, d:1}           False
        #     ctr2[s2[i-n1]]-= 1                      #  6     {b:2, a:1, i:1}           True
        #     ctr2[s2[i   ]]+= 1

        # return ctr1 == ctr2