# Problem Description
'''
Given an array A and an integer B, find the number of occurrences of B in A.
'''

# Problem Constraints
'''
1 <= B, A(i) <= 10^9
1 <= length(A) <= 10^5
'''

# Input Format
'''
Given an integer array A and an integer B.
'''

# Output Format
'''
Return an integer, number of occurrences of B in A.
'''

class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        # Initialize the count variable to 0
        count = 0

        # Initialize two pointers i and j to 0 and length of A - 1 respectively
        i = 0
        j = len(A) - 1
        # Loop until i is less than j
        while i < j:
            # Check if A[i] is equal to B
            if A[i] == B:
                count += 1
            # Check if A[j] is equal to B
            if A[j] == B:
                count += 1
            # Move the pointers towards each other
            i += 1
            j -= 1

        # If i is equal to j, check if A[i] is equal to B
        if i == j and A[i] == B:
            count += 1

        # Return the count of occurrences of B in A
        return count
    

# Time Complexity
'''
The time complexity of the solution is O(N) where N is the length of the array A.
This is because we are iterating through the array A once to count the occurrences of B.
'''

# Space Complexity
'''
The space complexity of the solution is O(1) because we are using a constant amount of extra space.
This is because we are not using any extra space to store the result.
'''

# Solution
'''
This solution is a brute force solution to find the number of occurrences of B in A.
The optimization is on number of iterations we need to do to find the occurrences of B in A. Using two pointers i and j, we can find the occurrences of B in A in O(N) time complexity, but iteration is reduced to half.
'''


import sys

if __name__ == "__main__":
    s = Solution()
    if len(sys.argv) == 1:
        # Example input: [1, 2, 2], B = 2
        A = [1, 2, 2]
        B = 2
        print("Test case 1: Finding occurrences of B=2 in A=[1, 2, 2]")
        print("Output:", s.solve(A, B))
        # Expected output: 2
        # Example input: [1, 2, 1], B = 3
        A = [1, 2, 1]
        B = 3
        print("Test case 2: Finding occurrences of B=3 in A=[1, 2, 1]")
        print("Output:", s.solve(A, B))
        # Expected output: 0
    else:
        try:
            A = list(map(int, sys.argv[1].strip('[]').split(',')))
            B = int(sys.argv[2])
            print("Finding occurrences of B={} in A={}".format(B, A))
            print("Output:", s.solve(A, B))
        except Exception as e:
            print("Invalid input, please provide a valid array and an integer.")
            print("Error:", e)
            print("Usage: python AP1-LinearSearchMultipleOccurences.py [1,2,3] 2")
            print("Where [1,2,3] is the array and 2 is the integer to find occurrences of.")