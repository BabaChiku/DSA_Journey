# Problem Description
'''
Misha likes finding all Subarrays of an Array. Now she gives you an array A of N elements and told you to find the number of subarrays of A, that have unique elements.
Since the number of subarrays could be large, return value % (10^9) +7.
'''

# Problem Constraints
'''
1 <= N <= 10^5
1 <= A[i] <= 10^6
'''

# Input Format
'''
The only argument given is an Array A, having N integers.
'''

# Output Format
'''
Return the number of subarrays of A, that have unique elements.
'''

class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        # Initialize the length of the array A
        n = len(A)
        # Initialize the count of unique subarrays to zero
        count = 0
        # Initialize a dictionary to store the last occurrence of each element
        last_occurrence = {}
        # Initialize the start index of the current subarray to zero
        start = 0

        # Loop through the array A to count unique subarrays
        for i in range(n):
            # If the element A[i] has been seen before, update the start index
            if A[i] in last_occurrence:
                start = max(start, last_occurrence[A[i]] + 1)
            # Update the last occurrence of the element A[i]
            last_occurrence[A[i]] = i
            # Calculate the number of unique subarrays ending at index i
            count += (i - start + 1)

        # Return the count of unique subarrays modulo (10^9 + 7)
        return count % (10**9 + 7)


# Time Complexity
'''
The time complexity of this solution is O(N), where N is the length of the array A.
This is because we are iterating through the array A once and using a dictionary to store the last occurrence of each element, which takes O(1) time on average for each insertion and lookup.
'''

# Space Complexity
'''
The space complexity of this solution is O(N), where N is the number of unique elements in the array A.
This is because we are using a dictionary to store the last occurrence of each element, which can take up to O(N) space in the worst case.
'''

# Solution
'''
This solution uses a sliding window approach to count the number of unique subarrays in the given array A.
The last occurrence of each element is stored in a dictionary, and the start index of the current subarray is updated whenever a duplicate element is encountered.
The count of unique subarrays is calculated by adding the number of unique subarrays ending at each index to the total count.
'''


import sys

if __name__ == "__main__":
    s = Solution()
    if len(sys.argv) == 1:
        # Test case 1
        A = [1, 1, 3]
        print("Test case 1: Finding unique subarrays of A=[1, 1, 3]")
        print("Number of unique subarrays:", s.solve(A))
        # Test case 2
        A = [2, 1, 2]
        print("Test case 2: Finding unique subarrays of A=[2, 1, 2]")
        print("Number of unique subarrays:", s.solve(A))
    else:
        try:
            # Read the input array from command line arguments
            A = list(map(int, sys.argv[1:]))
            print("Input array:", A)
            print("Number of unique subarrays:", s.solve(A))
        except Exception as e:
            print("Invalid input. Please provide a list of integers separated by commas.")
            print("Error:", e)
            print("Usage: python AP3-CountSubarrays.py [1,2,3]")
            print("Where [1,2,3] is the input array.")