class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        arr = []
        n = len(gain)
        arr.append(0)
        for i in range(0,n):
            z = arr[i]+gain[i]
            arr.append(z)
        return max(arr)
            