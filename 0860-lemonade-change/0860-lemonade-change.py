class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        f,t=0,0
        for i in bills:
            if i==5:
                f+=1
            elif i==10:
                f,t=f-1,t+1
            elif t>0:
                t-=1
                f-=1
            else:
                f-=3
            if f<0:
                return False
        return True                

        # five,ten=0,0
        # for i in bills:
        #     if i==5:
        #         five+=1
        #     elif i==10:
        #         five,ten=five-1,ten+1
        #     elif ten>0:
        #         ten-=1
        #         five-=1
        #     else:
        #         five-=3
        #     if five<0:
        #         return False
        # return True                        
        