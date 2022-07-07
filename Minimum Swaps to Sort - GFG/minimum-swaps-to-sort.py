

class Solution:
    
    #Function to find the minimum number of swaps required to sort the array.
	def minSwaps(self, nums):
		#Code here
		temp = list(nums)
		map = {}
		temp.sort()
		for i in range(len(temp)):
		    map[temp[i]] = i
	
		count = 0
		i = 0
		while i < len(nums):
		    if nums[i] == temp[i]:
		        i+=1
		    else:
		        count+=1
		        index = map[nums[i]]
		        nums[i],nums[index] = nums[index],nums[i]
		return count
#{ 
#  Driver Code Starts


if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n = int(input())
		nums = list(map(int, input().split()))
		obj = Solution()
		ans = obj.minSwaps(nums)
		print(ans)

# } Driver Code Ends