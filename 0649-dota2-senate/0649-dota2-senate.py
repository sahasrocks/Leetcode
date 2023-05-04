class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        N=len(senate)
        Rs, Ds = [], []
        for i in range(len(senate)):
            if senate[i]=='R':
                Rs.append(i)
            else:
                Ds.append(i)
        while Rs and Ds:
            if Rs[0]<Ds[0]:
                Ds.pop(0)
                Rs.append(Rs.pop(0)+N)
            else:
                Rs.pop(0)
                Ds.append(Ds.pop(0)+N) 
        if Rs:
            return "Radiant"
        return "Dire"
        