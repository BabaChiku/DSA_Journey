# Problem Description
'''
Given an array A of N integers. Construct prefix sum of the array in the given array itself.
'''

# Problem Constraints
'''
1 <= N <= 10^5
1 <= A[i] <= 10^3
'''

# Input Format
'''
Only argument A is an array of integers.
'''

# Output Format
'''
Return an array of integers denoting the prefix sum of the given array.
'''

class Solution:
    # @param A : list of integers
    # @return a list of integers
    def solve(self, A):
        # Initialize the length of the array A
        n = len(A)
        # Check if the length of A is less than or equal to 1
        if n <= 1:
            # If true, return A as it is already a prefix sum
            return A
        # Loop through the array A starting from index 1
        for i in range(1, n):
            # Update the current element with the sum of itself and the previous element
            A[i] += A[i - 1]
        # Return the modified array A which now contains the prefix sums
        return A


# Time Complexity
'''
The time complexity of the solve function is O(N) where N is the length of the array A.
This is because we are iterating through the array A once to calculate the prefix sums.
'''

# Space Complexity
'''
The space complexity of the solve function is O(1) as we are modifying the input array A in place and not using any additional space.
'''

# Solution
'''
This solution constructs the prefix sum of the array in place, meaning it modifies the original array A to contain the prefix sums.
The prefix sum at index i is the sum of all elements from index 0 to i in the original array.
'''