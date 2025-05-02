# Problem Description
'''
Given an array A of size N. You need to find the sum of Maximum and Minimum element in the given array.
'''

# Problem Constraints
'''
1 <= N <= 10^5
-10^9 <= A[i] <= 10^9
'''

# Input Format
'''
First argument A is an integer array.
'''

# Output Format
'''
Return the sum of maximum and minimum element of the array.
'''

class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        # Initialize the maximum and minimum values to the first element of the array A
        max_value = A[0]
        min_value = A[0]

        # initialize the length of the array A, i and j
        n = len(A)
        i = 0
        j = n - 1

        # Loop through the array A to find the maximum and minimum values
        while i <= j:
            # Check if A[i] is lesser or A[j] is lesser
            if A[i] < A[j]:
                # If A[i] is lesser, check if it is less than min_value
                if A[i] < min_value:
                    min_value = A[i]
                # Check if A[j] is greater than max_value
                if A[j] > max_value:
                    max_value = A[j]
            else:
                # If A[j] is lesser, check if it is less than min_value
                if A[j] < min_value:
                    min_value = A[j]
                # Check if A[i] is greater than max_value
                if A[i] > max_value:
                    max_value = A[i]

            # Move the pointers towards each other
            i += 1
            j -= 1
        
        # Return the sum of maximum and minimum values
        return max_value + min_value
    

# Time Complexity
'''
The time complexity of the solution is O(N) where N is the length of the array A.
This is because we are iterating through the array A once to find the maximum and minimum values.
'''

# Space Complexity
'''
The space complexity of the solution is O(1) because we are using a constant amount of extra space.
This is because we are only using a few variables to store the maximum and minimum values.
'''

# Solution
'''
The solution is to loop through the array A and for each element, check if it is greater than the current maximum value or less than the current minimum value. If we find such an element, we update the maximum or minimum value accordingly. Finally, we return the sum of the maximum and minimum values.
This solution is efficient and works well for large arrays as it only requires a single pass through the array to find the maximum and minimum values.
'''

import sys

if __name__ == "__main__":
    s = Solution()
    if len(sys.argv) == 1:
        # Example input: [1, 2, 3, 4, 5]
        A = [1, 2, 3, 4, 5]
        print("Test case 1: Finding max and min of A=[1, 2, 3, 4, 5]")
        print("Output:", s.solve(A))
        # Expected output: 6 (5 + 1)
        # Example input: [10, -10, 20, -20]
        A = [10, -10, 20, -20]
        print("Test case 2: Finding max and min of A=[10, -10, 20, -20]")
        print("Output:", s.solve(A))
    else:
        try:
            A = list(map(int, sys.argv[1].strip('[]').split(',')))
            print("Finding max and min of A={}".format(A))
            print("Output:", s.solve(A))
        except Exception as e:
            print("Invalid input, please provide a valid array of integers.")
            print("Error:", e)
            print("Usage: python P4-MaxMinOfAnArray.py [1,2,3,4,5]")
