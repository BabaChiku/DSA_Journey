# Problem Description
'''
You are given an array A of integers of size N.
Your task is to find the equilibrium index of the given array
The equilibrium index of an array is an index such that the sum of elements at lower indexes is equal to the sum of elements at higher indexes.
If there are no elements that are at lower indexes or at higher indexes, then the corresponding sum of elements is considered as 0.
Note:
    * Array indexing starts from 0.
    * If there is no equilibrium index then return -1.
    * If there are more than one equilibrium indexes then return the minimum index.
'''

# Problem Constraints
'''
1 <= N <= 10^5
-10^5 <= A[i] <= 10^5
'''

# Input Format
'''
First arugment is an array A .
'''

# Output Format
'''
Return the equilibrium index of the given array. If no such index is found then return -1.
'''

class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        # Initialize the length of the array A
        n = len(A)
        # Initialize the total sum of the array A to zero
        total_sum = 0
        
        # Calculate the prefix sum of the array A
        for i in range(n):
            total_sum += A[i]
            A[i] = total_sum
        
        # Check if the first element is an equilibrium index
        if total_sum - A[0] == 0:
            return 0
        
        # Loop through the array A to find equilibrium indices
        for i in range(1, n):
            if A[i - 1] == total_sum - A[i]:
                return i
        
        # If no equilibrium index is found, return -1
        return -1

# Time Complexity
'''
The time complexity of this solution is O(N), where N is the length of the array A.
This is because we are iterating through the array A twice: once to calculate the prefix sum and once to check for equilibrium indices.
'''

# Space Complexity
'''
The space complexity of this solution is O(1), as we are using the input array A to store the prefix sum and not using any additional space.
This is an in-place solution.
'''

# Solution
'''
This solution uses the prefix sum technique to find the equilibrium index of the given array A.
The prefix sum is calculated in the first loop, and then we check for equilibrium indices in the second loop.
The edge case of the first element being an equilibrium index is also handled.
'''


import sys

if __name__ == "__main__":
    s = Solution()
    if len(sys.argv) == 1:
        # Example input A = [-7, 1, 5, 2, -4, 3, 0]
        A = [-7, 1, 5, 2, -4, 3, 0]
        print("Test case 1: Finding equilibrium index of A=[-7, 1, 5, 2, -4, 3, 0]")
        print("Equilibrium index:", s.solve(A)) # This should return 3
        # Example input A = [1, 2, 3]
        A = [1, 2, 3]
        print("Test case 2: Finding equilibrium index of A=[1, 2, 3]")
        print("Equilibrium index:", s.solve(A)) # This should return -1
    else:
        try:
            A = list(map(int, sys.argv[1].strip("[]").split(",")))
            print("Finding equilibrium index of A =", A)
            print("Equilibrium index:", s.solve(A))
        except Exception as e:
            print("Invalid input. Please provide a list of integers separated by commas.")
            print("Error:", e)
            print("Usage: python script.py [1,2,3]")
            print("Where [1,2,3] is the input array.")
            print("Example: python AP1-EquilibriumIndex.py [-7,1,5,2,-4,3,0]")
