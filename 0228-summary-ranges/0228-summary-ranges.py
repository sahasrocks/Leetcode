class Solution(object):
	def summaryRanges(self, nums):
		ans=[]

		for i in nums:
			if i-1 not in nums:
				y=i+1
				while y in nums:
					y+=1
				if i==y-1:
					ans.append(str(i))
				else:
					ans.append(str(i)+"->"+str(y-1))
		return ans