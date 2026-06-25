class Solution:
    def countMajoritySubarrays(self, nums, target):
        dict1 = {0:1}

        count, pcount, res = 0, 0, 0 

        for num in nums:
            if num == target:
                pcount += dict1.get(count,0)
            else:
                pcount -= dict1.get(count-1,0)

            res += pcount 
            count += 1 if num == target else -1 
            dict1[count] = dict1.get(count,0) + 1 

        return res 