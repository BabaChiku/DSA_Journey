# Problem Description
'''
Given an array A, find the size of the smallest subarray such that it contains at least one occurrence of the maximum value of the array and at least one occurrence of the minimum value of the array.
'''

# Problem Constraints
'''
1 <= |A| <= 2000
'''

# Input Format
'''
First and only argument is vector A.
'''

# Output Format
'''
Return the length of the smallest subarray which has at least one occurrence of minimum and maximum element of the array.
'''

class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        # Initialize the length of the array A
        n = len(A)
        
        # Get the minimum and maximum values of the array A, if use of function is not allowed you can use two pointers to find min and max
        min_val = min(A)
        max_val = max(A)
        # If the minimum and maximum values are the same, return 1 as the smallest subarray size
        if min_val == max_val:
            return 1
        
        # Initialize the minimum length of the subarray to n
        min_length = n

        # Initialize the indices of the last occurrences of the minimum and maximum values to -1
        last_min_index = -1
        last_max_index = -1

        # Loop through the array A to find the last occurrences of the minimum and maximum values
        for i in range(n):
            if A[i] == min_val:
                last_min_index = i
                # If the last maximum index is not -1, update the minimum length of the subarray
                if last_max_index != -1:
                    min_length = min(min_length, i - last_max_index + 1)
            elif A[i] == max_val:
                last_max_index = i
                # If the last minimum index is not -1, update the minimum length of the subarray
                if last_min_index != -1:
                    min_length = min(min_length, i - last_min_index + 1)

        # Return the minimum length of the subarray
        return min_length
    

# Time Complexity
'''
The time complexity of this solution is O(N), where N is the length of the array A.
This is because we are iterating through the array A once to find the last occurrences of the minimum and maximum values.
'''

# Space Complexity
'''
The space complexity of this solution is O(1), as we are using a constant amount of space to store the minimum and maximum values and their last occurrences.
'''

# Solution
'''
This solution uses a single pass through the array to find the last occurrences of the minimum and maximum values.
The minimum length of the subarray is updated whenever a new minimum or maximum value is found.
'''


import sys

if __name__ == "__main__":
    s = Solution()
    if len(sys.argv) == 1:
        # Example input A = [1, 3, 2]
        A = [1, 3, 2]
        print("Test case 1: ", A)
        print("Smallest subarray length:", s.solve(A)) # This should return 2
        # Example input A = [2, 6, 1, 6, 9]
        A = [2, 6, 1, 6, 9]
        print("Test case 2: ", A)
        print("Smallest subarray length:", s.solve(A))
    else:
        try:
            A = list(map(int, sys.argv[1].strip("[]").split(",")))
            print("Finding smallest subarray length of A =", A)
            print("Smallest subarray length:", s.solve(A))
        except Exception as e:
            print("Invalid input. Please provide a list of integers separated by commas.")
            print("Error:", e)
            print("Usage: python P1-ClosestMinMax.py [1,2,3]")
            print("Where [1,2,3] is the input array.")