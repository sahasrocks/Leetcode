class Solution:
    def simplifyPath(self, path: str) -> str:
        ans=[]
        for p in path.split("/"):
            if p==".." and ans:
                ans.pop()
            elif p not in "..":
                ans.append(p)
        #print(ans)
        return "/"+"/".join(ans)            