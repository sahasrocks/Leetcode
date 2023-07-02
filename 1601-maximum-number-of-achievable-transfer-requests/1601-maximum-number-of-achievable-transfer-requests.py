class Solution:
    def maximumRequests(self, n, requests):  
        N = len(requests)
        for i in range(N, -1, -1): # Try longer lengths first
            for combination in combinations(range(N), i): # Generate combination with length = i
                arr = [0] * n
                for j in combination:
                    [x,y] = requests[j]
                    arr[x] += 1
                    arr[y] -= 1
                if not any(arr): return i # If all zero then net change in employees is 0