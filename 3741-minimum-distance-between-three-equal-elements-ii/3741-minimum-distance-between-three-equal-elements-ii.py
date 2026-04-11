class Solution:
    def minimumDistance(self, nums: List[int]) -> int:
        mp = defaultdict(list)
        n = len(nums)

        # Store indices for each value
        for i in range(n):
            mp[nums[i]].append(i)

        ans = float('inf')

        # Process each value
        for indices in mp.values():
            if len(indices) < 3:
                continue

            # Try consecutive triplets
            for i in range(len(indices) - 2):
                dist = 2 * (indices[i + 2] - indices[i])
                ans = min(ans, dist)

        return -1 if ans == float('inf') else ans
        