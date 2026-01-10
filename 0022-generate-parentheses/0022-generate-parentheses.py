class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res=[]
        def bt(cur,open,close):
            if len(cur) == 2*n:
                res.append(cur)
                return
            if open<n:
                bt(cur+'(',open+1,close)
            if close<open:
                bt(cur+')',open,close+1)
        bt("",0,0)
        return res                
        
        # stack=[]
        # res=[]
        # def bt(open,close):
        #     if open == close==n:
        #         res.append("".join(stack))
        #         return
        #     if open<n:
        #         stack.append("(")
        #         bt(open+1,close)
        #         stack.pop()
        #     if close<open:
        #         stack.append(")")
        #         bt(open,close+1)
        #         stack.pop()
        # bt(0,0)
        # return res                
        
        # stack=[]
        # res=[]
        # def backtrack(open,close):
        #     if open==close==n:
        #         res.append("".join(stack))
        #         return
        #     if open<n:
        #         stack.append("(")
        #         backtrack(open+1,close)
        #         stack.pop()
        #     if close<open:
        #         stack.append(")")
        #         backtrack(open,close+1)
        #         stack.pop()
        # backtrack(0,0)
        # return res                
        