# Problem Description
'''
Given an integer array A of size N. In one second, you can increase the value of one element by 1.

Find the minimum time in seconds to make all elements of the array equal.
'''

# Problem Constraints
'''
1 <= N <= 1000000
1 <= A[i] <= 1000
'''

# Input Format
'''
First argument is an integer array A.
'''

# Output Format
'''
Return an integer denoting the minimum time to make all elements equal.
'''

class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        # Find length of the array A
        n = len(A)
        # Initialize the minTime, max_value, i, j and elements variables
        minTime = 0
        max_value = A[0]
        i = 0
        j = n - 1
        elements = 0

        # Loop through the array A to find minimum time to make all elements equal
        while i < j:
            # Check if A[i] is greater or A[j] is greater
            if A[i] > A[j]:
                # If A[i] is greater, check if it is greater than max_value
                if A[i] > max_value:
                    minTime += (A[i] - A[j]) + (elements * (A[i] - max_value))
                    max_value = A[i]
                else:
                    minTime += (max_value - A[j]) + (max_value - A[i])
            else:
                # If A[j] is greater, check if it is greater than max_value
                if A[j] > max_value:
                    minTime += (A[j] - A[i]) + (elements * (A[j] - max_value))
                    max_value = A[j]
                else:
                    minTime += (max_value - A[i]) + (max_value - A[j])

            # Move the pointers towards each other
            i += 1
            j -= 1
            # Increment the elements variable
            elements += 2
        # If i is equal to j
        if i == j:
            # Check if A[i] is greater than max_value
            if A[i] > max_value:
                minTime += (elements * (A[i] - max_value))
                max_value = A[i]
            else:
                minTime += (max_value - A[i])
        # Return the minimum time to make all elements equal
        return minTime


# Time Complexity
'''
The time complexity of the solution is O(N) where N is the length of the array A.
This is because we are iterating through the array A once to find the minimum time to make all elements equal.
'''

# Space Complexity
'''
The space complexity of the solution is O(1) because we are using a constant amount of extra space.
This is because we are only using a few variables to store the minimum time, maximum value, and other variables.
'''

# Solution
'''
The solution is to loop through the array A and for each pair of elements (i, j), check if A[i] is greater than A[j].
If A[i] is greater, we need to increase A[j] to make it equal to A[i], and vice versa.
We keep track of the maximum value and the number of elements we have processed so far.
If we find an element that is greater than the maximum value, we need to increase all previous elements to make them equal to the maximum value.
We also keep track of the minimum time required to make all elements equal.
Finally, we return the minimum time required to make all elements equal.
'''


import sys

if __name__ == "__main__":
    s = Solution()
    if len(sys.argv) == 1:
        # Example input: [1, 2, 3, 4, 5]
        A = [1, 2, 3, 4, 5]
        print("Test case 1: Finding minimum time to make all elements equal in A=[1, 2, 3, 4, 5]")
        print("Output:", s.solve(A))
        # Expected output: 10
        # Example input: [2, 4, 1, 3, 2]
        A = [2, 4, 1, 3, 2]
        print("Test case 2: Finding minimum time to make all elements equal in A=[2, 4, 1, 3, 2]")
        print("Output:", s.solve(A))
        # Expected output: 8
    else:
        try:
            A = list(map(int, sys.argv[1].strip('[]').split(',')))
            print("Finding minimum time to make all elements equal in A={}".format(A))
            print("Output:", s.solve(A))
        except Exception as e:
            print("Invalid input, please provide a valid array as input.")
            print("Error:", e)
            print("Usage: python AP2-TimeToEquality.py [1,2,3,4,5]")
            print("Where [1, 2, 3, 4, 5] is the array.")
