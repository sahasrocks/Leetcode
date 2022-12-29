class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        # 1) Make a dictionary where 
        # the element's key - `piles[i]` and value - number of piles
        dictPiles = {}
        for p in piles:
            if p in dictPiles:
                dictPiles[p] += 1
            else:
                dictPiles[p] = 1
        
        # 2) Find max stones in piles
        maxp = max(piles)        

        # 3) Iterate from max to 0
        for stones in range(maxp,0,-1):
            # 3.a) Find pile with this number of stones
            if stones in dictPiles:
                # 3.b) Remove stones (while there are the piles 
                # and k is not 0) and move new piles
                while dictPiles[stones] and k:
                    dictPiles[stones] -= 1
                    # move the pile after deletion
                    t = stones - (stones // 2)
                    if t in dictPiles:
                        dictPiles[t] += 1
                    else:
                        dictPiles[t] = 1
                    k -= 1

            # 3.c) Break if k==0
            if not k:
                break
        
        # 4) Count the amount
        sumS = 0
        for k,v in dictPiles.items():
            sumS += k*v

        return sumS