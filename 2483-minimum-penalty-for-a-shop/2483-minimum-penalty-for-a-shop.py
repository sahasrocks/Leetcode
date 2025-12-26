class Solution:
    def bestClosingTime(self, customers: str) -> int:
        n=len(customers)
        pren=[0]*(n+1)
        posty=[0]*(n+1)
        for i in range(1,n+1):
            pren[i]=pren[i-1]
            if customers[i-1]=="N":
                pren[i]+=1
        for i in range(n-1,-1,-1):
            posty[i]=posty[i+1]
            if customers[i]=="Y":
                posty[i]+=1
        minp,idx=float('inf'),0
        for i in range(n+1):
            pen=pren[i]+posty[i]
            if pen<minp:
                minp=pen
                idx=i
        return idx                        

        