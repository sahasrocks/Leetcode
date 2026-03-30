class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack=[]
        s=list(s)
        for i,e in enumerate(s):
            if e=='(':
                stack.append(i)
            elif e==')':
                if stack:
                    stack.pop()
                else:
                    s[i]=''
        while stack:
            s[stack.pop()]=''
        return ''.join(s)            



        # stack=[]
        # s=list(s)
        # for i,e in enumerate(s):
        #     if e=='(':
        #         stack.append(i)
        #     elif e==')':
        #         if stack:
        #             stack.pop()
        #         else:
        #             s[i]=''
        # while stack:
        #     s[stack.pop()]=''
        # return ''.join(s)                    

        
        
        
        
        # stack=[]
        # s=list(s)
        # for i,c in enumerate(s):
        #     if c=='(':
        #         stack.append(i)
        #     elif c==')':
        #         if stack:
        #             stack.pop()
        #         else:
        #             s[i]=''
        # while stack:
        #     s[stack.pop()]=''
        # return ''.join(s)                        
        