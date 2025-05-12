# Problem Description
'''
You are given an array A of N integers.
Return a 2D array consisting of all the subarrays of the array
Note : The order of the subarrays in the resulting 2D array does not matter.
'''

# Problem Constraints
'''
1 <= N <= 100
1 <= A[i] <= 10^5
'''

# Input Format
'''
First argument A is an array of integers.
'''

# Output Format
'''
Return a 2D array of integers in any order.
'''

class Solution:
    # @param A : list of integers
    # @return a list of list of integers
    def solve(self, A):
        # Initialize the length of the array A
        n = len(A)
        # Initialize the list to store the subarrays
        subarrays = []
        
        # Loop through the array A to find all subarrays
        for i in range(n):
            for j in range(i, n):
                # Append the subarray from index i to j to the list of subarrays
                subarrays.append(A[i:j + 1])    # This is the subarray from index i to j, and will be considered an loop of O(N). Python provides slicing, may not be avaliable in other languages.
        
        # Return the list of subarrays
        return subarrays


# Time Complexity
'''
The time complexity of this solution is O(N^3), where N is the length of the array A.
This is because we are using two nested loops to find all subarrays, and for each subarray, we are creating a new list which takes O(N) time.
'''

# Space Complexity
'''
The space complexity of this solution is O(N^2), where N is the length of the array A.
'''

# Solution
'''
This solution uses two nested loops to find all subarrays of the given array A.
The outer loop iterates through the starting index of the subarray, and the inner loop iterates through the ending index of the subarray.
The subarray is created using slicing, which is a built-in feature of Python.
This may not be available in other languages, and you may need to create a new list and copy the elements from the original array to the new list.
'''


import sys

if __name__ == "__main__":
    s = Solution()
    if len(sys.argv) == 1:
        # Test case 1
        A = [1, 2, 3]
        print("Test case 1: Finding all subarrays of A=[1, 2, 3]")
        print("Subarrays:", s.solve(A))
        # Test case 2
        A = [5, 2, 1, 4]
        print("Test case 2: Finding all subarrays of A=[5, 2, 1, 4]")
        print("Subarrays:", s.solve(A))
    else:
        try:
            # Read the input from command line arguments
            A = list(map(int, sys.argv[1].strip("[]").split(",")))
            print("Finding all subarrays of A =", A)
            print("Subarrays:", s.solve(A))
        except Exception as e:
            print("Invalid input. Please provide a list of integers separated by commas.")
            print("Error:", e)
            print("Usage: python P3-GenerateAllSubarrays.py [1,2,3]")
            print("Where [1,2,3] is the input array.")