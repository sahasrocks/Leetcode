class Solution:
    def maximizeSquareHoleArea(self, n: int, m: int, hBars: List[int], vBars: List[int]) -> int:
        hBars.sort()
        vBars.sort()
        def cal(nums):
            best=1
            streak=1
            for i in range(len(nums)-1):
                if nums[i]+1==nums[i+1]:
                    streak+=1
                else:
                    streak=1
                best=max(best,streak)
            return best
        return (min(cal(hBars),cal(vBars))+1) **2               