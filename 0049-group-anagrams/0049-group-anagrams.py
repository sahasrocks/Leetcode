class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # a_dict=defaultdict(list)
        # for s in strs:
        #     count=[0]*26
        #     for c in s:
        #         count[ord(c)-ord('a')] += 1
        #     key = tuple(count)
        #     a_dict[key].append(s)
        # return list(a_dict.values())        
        a_dict = defaultdict(list)
        for s in strs:
            key = "".join(sorted(s))   # ✅ sorted string as key
            a_dict[key].append(s)
        return list(a_dict.values())