class Solution:
    def minSpeedOnTime(self, dist: List[int], hour: float) -> int:
        low=1
        high=10**7+1
        n=len(dist)
        while low<high:
            mid=(low+high)//2
            time=sum((dist[i]+mid-1)//mid for i in range(0,n-1))+dist[-1]/mid
            if time<=hour:
                high=mid

            else:
                low=mid+1

        return low if low <10**7+1 else-1