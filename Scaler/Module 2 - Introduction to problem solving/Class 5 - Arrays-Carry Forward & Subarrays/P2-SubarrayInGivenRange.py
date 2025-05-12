# Problem Description
'''
Given an array A of length N, return the subarray from B to C.
'''

# Problem Constraints
'''
1 <= N <= 10^5
1 <= A[i] <= 10^9
0 <= B <= C < N
'''

# Input Format
'''
The first argument A is an array of integers
The remaining argument B and C are integers.
'''

# Output Format
'''
Return a subarray
'''


class Solution:
    # @param A : list of integers
    # @param B : integer
    # @param C : integer
    # @return a list of integers
    def solve(self, A, B, C):
        # # Return the subarray from B to C
        # return A[B:C + 1]  # Not this easy ;)

        # Initialize the length of the subarray to be returned
        n = C - B + 1
        # Initialize the subarray to be returned
        subarray = [0] * n
        # Initialize the index of the subarray to be returned
        index = 0
        # Loop through the array A from B to C
        for i in range(B, C + 1):
            # Add the element at index i of A to the subarray
            subarray[index] = A[i]
            # Increment the index of the subarray
            index += 1
        # Return the subarray
        return subarray
    

# Time Complexity
'''
The time complexity of this solution is O(N), where N is the length of the subarray to be returned.
'''

# Space Complexity
'''
The space complexity of this solution is O(N), where N is the length of the subarray to be returned.
This is because we are using an additional array to store the subarray.
'''

# Solution
'''
This solution is a brute force solution to the problem of finding the subarray from B to C in an array A.
'''


import sys

if __name__ == "__main__":
    s = Solution()
    if len(sys.argv) == 1:
        # Test case 1
        A = [4, 3, 2, 6]
        B = 1
        C = 3
        print("Test case 1: Finding subarray of A=[4, 3, 2, 6] from B=1 to C=3")
        print("Subarray:", s.solve(A, B, C))  # This should return [3, 2, 6]
        # Test case 2
        A = [4, 2, 2]
        B = 0
        C = 1
        print("Test case 2: Finding subarray of A=[4, 2, 2] from B=0 to C=1")
        print("Subarray:", s.solve(A, B, C))  # This should return [4, 2]
    else:
        try:
            # Read the input from command line arguments
            A = list(map(int, sys.argv[1].strip("[]").split(",")))
            B = int(sys.argv[2])
            C = int(sys.argv[3])
            print("Input array A =", A)
            print("Finding subarray of A from B =", B, "to C =", C)
            print("Subarray:", s.solve(A, B, C))
        except Exception as e:
            print("Invalid input. Please provide a list of integers separated by commas.")
            print("Error:", e)
            print("Usage: python P2-SubarrayInGivenRange.py [1,2,3] 0 2")
            print("Where [1,2,3] is the input array and 0 and 2 are the indices B and C.")