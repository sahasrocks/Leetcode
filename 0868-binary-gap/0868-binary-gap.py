class Solution:
    def binaryGap(self, n: int) -> int:
        maxGap = 0
        bitpos = 0
        lastSetBit = -1

        while bitpos < 31:
            if (n >> bitpos) & 1:
                if lastSetBit != -1:
                    maxGap = max(maxGap, bitpos - lastSetBit)
                lastSetBit = bitpos
            bitpos += 1

        return maxGap