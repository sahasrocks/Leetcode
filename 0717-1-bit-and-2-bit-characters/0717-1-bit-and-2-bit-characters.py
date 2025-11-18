class Solution:
    def isOneBitCharacter(self, bits):
        q=collections.deque(bits)

        last=False
        while len(q)>0:
            a=q.popleft()
            if a==0:
                last=True
                continue
            last=False
            q.popleft()
        return last        

        
        
        # i, n, numBits = 0, len(bits), 0
        # while i < n:
        #     bit = bits[i]
        #     if bit == 1:
        #         i += 2
        #         numBits = 2
        #     else:
        #         i += 1
        #         numBits = 1
        # return numBits == 1