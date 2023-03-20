class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        pad_flowerbed = [0] + flowerbed + [0]
        count = 0
        for idx in range(len(flowerbed)):
            if pad_flowerbed[idx:idx+3] == [0, 0, 0]:
                pad_flowerbed[idx+1]=1
                count+=1
        return count >= n   
        