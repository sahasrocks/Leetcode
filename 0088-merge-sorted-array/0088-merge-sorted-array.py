class Solution(object):
    def merge(self, num1, m, num2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        while m>0 and n>0:
            if num1[m-1]>num2[n-1]:
                num1[m+n-1]=num1[m-1]
                m-=1
            else:
                num1[m+n-1]=num2[n-1]
                n-=1
        while n>0:
            num1[n-1]=num2[n-1]
            n-=1            

        