class Solution:
    def numTrees(self, n: int) -> int:
        numTree = [1] * (n + 1)

        for nodes in range(2, n + 1):
            total = 0
            for root in range(1, nodes + 1):
                left = root - 1
                right = nodes - root
                total += numTree[left] * numTree[right]
            numTree[nodes] = total

        return numTree[n]      

                
        
        
        # if n == 0 or n == 1:
        #     return 1
        # # Create 'sol' array of length n+1...
        # sol = [0] * (n+1)
        # # The value of the first index will be 1.
        # sol[0] = 1
        # # Run a loop from 1 to n+1...
        # for i in range(1, n+1):
        #     # Within the above loop, run a nested loop from 0 to i...
        #     for j in range(i):
        #         # Update the i-th position of the array by adding the multiplication of the respective index...
        #         sol[i] += sol[j] * sol[i-j-1]
        # # Return the value of the nth index of the array to get the solution...
        # return sol[n]