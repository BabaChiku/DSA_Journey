# Problem Description
'''
You are given a 2D matrix A of integers.
Your task is to compute the sum of elements in each row and return a 1D array where each element represents the sum of a corresponding row in the matrix.
'''

# Problem Constraints
'''
1 <= A.size() <= 10^3
1 <= A[i].size() <= 10^3
1 <= A[i][j] <= 10^3
'''

# Input Format
'''
First argument A is a 2D array of integers.(2D matrix).
'''

# Output Format
'''
Return an array containing row-wise sums of original matrix.
'''


class Solution:
    # @param A : list of list of integers
    # @return a list of integers
    def solve(self, A):
        num_rows = len(A)
        num_cols = len(A[0]) if num_rows > 0 else 0

        row_sums = [0] * num_rows

        # Calculate sum for each row
        for i in range(num_rows):
            for j in range(num_cols):
                row_sums[i] += A[i][j]

        return row_sums



# Time Complexity
'''
The time complexity of this solution is O(N*M), where N is the number of rows and M is the number of columns in the matrix A.
This is because we are iterating through each element of the matrix once to calculate the row sums.
'''

# Space Complexity
'''
The space complexity of this solution is O(N) as we are using extra space to store the row sums in the list row_sums.
'''

# Solution
'''
This solution iterates through each element of the given matrix A using a nested loop. The outer loop iterates over the rows, while the inner loop iterates over the columns of each row.
For each element, it adds the value to the corresponding row sum in the row_sums list. At the end of the iteration, the row_sums list contains the sum of each row, which is then returned.
'''