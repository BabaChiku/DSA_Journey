# Problem Description
'''
You have given a string A having Uppercase English letters.
You have to find how many times subsequence "AG" is there in the given string.
NOTE: Return the answer modulo 10^9 + 7 as the answer can be very large.
'''

# Problem Constraints
'''
1 <= length(A) <= 10^5
'''

# Input Format
'''
First and only argument is a string A.
'''

# Output Format
'''
Return an integer denoting the answer.
'''

class Solution:
    # @param A : string
    # @return an integer
    def solve(self, A):
        # Initialize the length of the string A
        n = len(A)
        # Initialize the count of 'A' characters to zero
        count_A = 0
        # Initialize the count of subsequences "AG" to zero
        count_AG = 0

        # Loop through the string A to count the number of subsequences "AG"
        for i in range(n):
            if A[i] == 'A':
                # Increment the count of 'A' characters
                count_A += 1
            elif A[i] == 'G':
                # Increment the count of subsequences "AG" by the number of 'A' characters seen so far
                count_AG += count_A

        # Return the count of subsequences "AG" modulo 10^9 + 7
        return count_AG % (10**9 + 7)


# Time Complexity
'''
The time complexity of this solution is O(N), where N is the length of the string A.
This is because we are iterating through the string A once to count the number of subsequences "AG".
'''

# Space Complexity
'''
The space complexity of this solution is O(1), as we are using a constant amount of space to store the counts.
'''

# Solution
'''
This solution uses a single loop to count the number of subsequences "AG" in the given string A.
The count of 'A' characters is maintained in a variable, and the count of subsequences "AG" is updated whenever a 'G' character is encountered.
'''


import sys

if __name__ == "__main__":
    s = Solution()
    if len(sys.argv) == 1:
        # Test case 1
        A = "ABCGAG"
        print("Test case 1: Finding subsequences AG in A='ABCGAG'")
        print("Number of subsequences AG:", s.solve(A))
        # Test case 2
        A = "GAB"
        print("Test case 2: Finding subsequences AG in A='GAB'")
        print("Number of subsequences AG:", s.solve(A))
    else:
        try:
            # Read input from command line arguments
            A = sys.argv[1]
            print("Finding subsequences AG in A='{}'".format(A))
            print("Number of subsequences AG:", s.solve(A))
        except Exception as e:
            print("Invalid input. Please provide a string.")
            print("Error:", e)
            print("Usage: python P4-SpecialSubsequences.py ABCGAG")
            print("Where 'ABCGAG' is the input string.")