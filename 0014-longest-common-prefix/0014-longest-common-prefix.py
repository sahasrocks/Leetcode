class Solution:
    def longestCommonPrefix(self, a: List[str]) -> str:
        # s = len(a)
        # if s==0:
        #     return ""
        # if s ==1:
        #     return a[0]
        
        # a.sort()
        # end = min(len(a[0]), len(a[s - 1]))
        # i = 0
        # while (i < end and
        #        a[0][i] == a[s - 1][i]):
        #     i += 1

        # pre = a[0][0: i]
        # return pre
        res = ""
        for i in range(len(a[0])):
            for s in a:
                if i ==len(s) or s[i] != a[0][i]:
                    return res
            res += a[0][i]
        return res           
