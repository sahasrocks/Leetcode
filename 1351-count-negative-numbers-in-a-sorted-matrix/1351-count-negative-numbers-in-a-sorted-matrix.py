class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        def bin(row):
            l,r=0,len(row)
            while l<r:
                m=(l+r)//2
                if row[m]<0:
                    r=m
                else:
                    l=m+1
            return len(row)-l
        c=0
        for row in grid:
            c+=bin(row)
        return c                    
        

        #return sum([1 for i in grid for j in i if j < 0])