# Problem Description
'''
You are given an integer array A of size N.
You have to perform B operations. In one operation, you can remove either the leftmost or the rightmost element of the array A.
Find and return the maximum possible sum of the B elements that were removed after the B operations.
NOTE: Suppose B = 3, and array A contains 10 elements, then you can:
    Remove 3 elements from front and 0 elements from the back, OR
    Remove 2 elements from front and 1 element from the back, OR
    Remove 1 element from front and 2 elements from the back, OR
    Remove 0 elements from front and 3 elements from the back.
'''

# Problem Constraints
'''
1 <= N <= 10^5
1 <= B <= N
-10^3 <= A[i] <= 10^3
'''

# Input Format
'''
First argument is an integer array A.
Second argument is an integer B.
'''

# Output Format
'''
Return an integer denoting the maximum possible sum of elements you removed.
'''

class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        # Initialize the length of the array A
        n = len(A)

        # Initialize the prefix sum of the array A, till B elements
        prefix_sum = [0] * (B + 1)
        # Calculate the prefix sum of the array A
        for i in range(B):
            prefix_sum[i + 1] = prefix_sum[i] + A[i]

        # Initialize the suffix sum of the array A
        suffix_sum = [0] * (B + 1)
        # Calculate the suffix sum of the array A
        for i in range(B):
            suffix_sum[i + 1] = suffix_sum[i] + A[n - 1 - i]
        
        # Initialize the maximum sum to negative infinity
        max_sum = float('-inf')
        
        # Loop through the array A to find the maximum sum of B elements
        for i in range(B + 1):
            # Calculate the sum of B elements by taking i elements from the prefix and (B - i) elements from the suffix
            current_sum = prefix_sum[i] + suffix_sum[B - i]
            # Update the maximum sum if the current sum is greater
            max_sum = max(max_sum, current_sum)
        
        # Return the maximum sum
        return max_sum


# Time Complexity
'''
The time complexity of this solution is O(N), where N is the length of the array A.
This is because we are iterating through the array A twice: once to calculate the prefix sum and once to calculate the suffix sum.
Then we iterate through the prefix and suffix sums to find the maximum sum.
This results in a total time complexity of O(N), because the maximum value of B can be N.
'''

# Space Complexity
'''
The space complexity of this solution is O(B), where B is the number of elements to be removed.
This is because we are using two additional arrays of size B + 1 to store the prefix and suffix sums.
'''

# Solution
'''
This solution uses prefix and suffix sums to find the maximum sum of B elements that can be removed from the array A.
The prefix sum is calculated for the first B elements, and the suffix sum is calculated for the last B elements.
The maximum sum is then calculated by taking i elements from the prefix and (B - i) elements from the suffix for all possible values of i.
'''


import sys

if __name__ == "__main__":
    s = Solution()
    if len(sys.argv) == 1:
        # Test case 1
        A = [5, -2, 3 , 1, 2]
        B = 3
        print("Test case 1: Finding maximum sum of B elements removed from A=[5, -2, 3 , 1, 2], B=3")
        print("Maximum sum:", s.solve(A, B))
        # Test case 2
        A = [ 2, 3, -1, 4, 2, 1 ]
        B = 4
        print("Test case 2: Finding maximum sum of B elements removed from A=[2, 3, -1, 4, 2, 1], B=4")
        print("Maximum sum:", s.solve(A, B))
    else:
        try:
            A = list(map(int, sys.argv[1].strip("[]").split(",")))
            B = int(sys.argv[2])
            print("Finding maximum sum of B elements removed from A=", A, ", B=", B)
            print("Maximum sum:", s.solve(A, B))
        except Exception as e:
            print("Invalid input. Please provide a list of integers separated by commas.")
            print("Error:", e)
            print("Usage: python AP1-PickFromBothSides.py [1,2,3] 2")
            print("Where [1,2,3] is the input array and 2 is the number of elements to be removed.")